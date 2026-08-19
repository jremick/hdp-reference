#!/usr/bin/env python3
"""Validate the HDP draft specification's maintained machine artifacts."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "hdp.schema.json"
DOCUMENTS = (
    ROOT / "examples" / "minimal" / "hdp.yaml",
    ROOT / "examples" / "document-review" / "hdp.yaml",
    ROOT / "examples" / "software-development" / "hdp.yaml",
    ROOT / "templates" / "hdp-starter.yaml",
)
SKILL_SCHEMA_COPIES = (
    ROOT / "skills" / "create-hdp" / "references" / "hdp.schema.json",
    ROOT / "skills" / "analyse-existing-harness" / "references" / "hdp.schema.json",
)
REFERENCE_KEYS = {
    "allowedIds",
    "evaluatorId",
    "evaluatorIds",
    "evidenceArtifactId",
    "expectedOutcomeIds",
    "failureIds",
    "fixtureIds",
    "from",
    "measureId",
    "measureIds",
    "metricIds",
    "ref",
    "requirementIds",
    "roleIds",
    "scenarioIds",
    "taskClassId",
    "testId",
    "to",
    "toolIds",
    "verificationIds",
}
FORBIDDEN_NORMATIVE_NAMES = re.compile(
    r"\b(codex|openai|anthropic|claude|gemini)\b", re.IGNORECASE
)
MACHINE_PATHS = (
    "/" + "Users" + "/",
    "/" + "private" + "/" + "var" + "/",
    "Documents" + "/" + "New project",
)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class StrictLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects aliases, merges, and duplicate keys."""

    def compose_node(self, parent: Any, index: Any) -> Any:
        if self.check_event(yaml.AliasEvent):
            event = self.peek_event()
            raise yaml.constructor.ConstructorError(
                None, None, "YAML aliases are not supported", event.start_mark
            )
        return super().compose_node(parent, index)


def construct_mapping(loader: StrictLoader, node: yaml.MappingNode, deep: bool = False) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "mapping keys must be strings",
                key_node.start_mark,
            )
        if key == "<<":
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "YAML merge keys are not supported",
                key_node.start_mark,
            )
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"duplicate key: {key}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
)


def load_yaml(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    if len(text.encode("utf-8")) > 2_000_000:
        raise ValueError(f"{path}: document exceeds 2 MB validation limit")
    return yaml.load(text, Loader=StrictLoader)


def walk(value: Any, pointer: str = ""):
    yield pointer or "/", value
    if isinstance(value, dict):
        for key, item in value.items():
            escaped = key.replace("~", "~0").replace("/", "~1")
            yield from walk(item, f"{pointer}/{escaped}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from walk(item, f"{pointer}/{index}")


def semantic_checks(document: dict[str, Any], path: Path) -> list[str]:
    errors: list[str] = []
    ids: dict[str, str] = {}
    references: list[tuple[str, str]] = []

    for pointer, value in walk(document):
        if not isinstance(value, dict):
            continue
        entity_id = value.get("id")
        if isinstance(entity_id, str):
            if entity_id in ids:
                errors.append(
                    f"{path}:{pointer}/id duplicates {entity_id!r} first seen at {ids[entity_id]}"
                )
            else:
                ids[entity_id] = f"{pointer}/id"

        for key, item in value.items():
            if key not in REFERENCE_KEYS:
                continue
            if key == "ref" and value.get("kind") not in {
                "outcome",
                "requirement",
                "component",
                "test",
                "evidence",
                "risk",
                "control",
            }:
                continue
            if isinstance(item, str):
                references.append((f"{pointer}/{key}", item))
            elif isinstance(item, list):
                references.extend(
                    (f"{pointer}/{key}/{index}", ref)
                    for index, ref in enumerate(item)
                    if isinstance(ref, str)
                )

    for pointer, reference in references:
        if reference not in ids:
            errors.append(f"{path}:{pointer} has unresolved reference {reference!r}")

    for index, requirement in enumerate(document.get("requirements", [])):
        if requirement.get("priority") == "must" and not requirement.get("verificationIds"):
            errors.append(
                f"{path}:/requirements/{index}/verificationIds is required for MUST requirements"
            )

    return errors


def check_schema_copies(schema_bytes: bytes) -> list[str]:
    errors: list[str] = []
    expected = hashlib.sha256(schema_bytes).hexdigest()
    for path in SKILL_SCHEMA_COPIES:
        if not path.is_file():
            errors.append(f"missing portable skill schema copy: {path.relative_to(ROOT)}")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            errors.append(
                f"schema copy drift: {path.relative_to(ROOT)} has {actual}, expected {expected}"
            )
    return errors


def check_portable_asset_copies() -> list[str]:
    errors: list[str] = []
    pairs = (
        (
            ROOT / "templates" / "hdp-starter.yaml",
            ROOT / "skills" / "create-hdp" / "assets" / "hdp-starter.yaml",
        ),
        (
            ROOT / "templates" / "reconstruction-evidence-map.yaml",
            ROOT / "skills" / "analyse-existing-harness" / "assets" / "evidence-map.yaml",
        ),
    )
    for canonical, portable in pairs:
        if canonical.read_bytes() != portable.read_bytes():
            errors.append(
                f"portable asset drift: {portable.relative_to(ROOT)} differs from {canonical.relative_to(ROOT)}"
            )
    return errors


def check_provider_neutrality() -> list[str]:
    errors: list[str] = []
    paths = [ROOT / "SPECIFICATION.md"]
    paths.extend((ROOT / "schema").rglob("*"))
    paths.extend((ROOT / "templates").rglob("*"))
    paths.extend((ROOT / "examples").rglob("*"))
    for path in paths:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        match = FORBIDDEN_NORMATIVE_NAMES.search(text)
        if match:
            errors.append(
                f"provider-specific name {match.group(0)!r} appears in normative/example artifact {path.relative_to(ROOT)}"
            )
    return errors


def check_public_surface() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or ".venv" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".txt", ".py"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for marker in MACHINE_PATHS:
            if marker in text:
                errors.append(f"machine-specific path marker {marker!r} in {path.relative_to(ROOT)}")
    return errors


def check_markdown_links() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or ".venv" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip()
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"link escapes repository in {path.relative_to(ROOT)}: {raw_target}")
                continue
            if not resolved.exists():
                errors.append(f"broken local link in {path.relative_to(ROOT)}: {raw_target}")
    return errors


def check_conformance_cases(
    validator: Draft202012Validator,
) -> tuple[list[str], int]:
    errors: list[str] = []
    manifest_path = ROOT / "conformance" / "manifest.yaml"
    manifest = load_yaml(manifest_path)
    cases = manifest.get("cases", []) if isinstance(manifest, dict) else []
    for case in cases:
        case_id = case.get("id", "UNKNOWN")
        path = (manifest_path.parent / case["path"]).resolve()
        expected_status = case["expectedStatus"]
        expected_layer = case["expectedLayer"]
        try:
            document = load_yaml(path)
        except Exception:
            actual_status = "fail"
            actual_layer = "transport"
        else:
            structural = list(validator.iter_errors(document))
            if structural:
                actual_status = "fail"
                actual_layer = "structural"
            else:
                semantic = semantic_checks(document, path.relative_to(ROOT))
                actual_status = "fail" if semantic else "pass"
                actual_layer = "baseline-semantic"
        if (actual_status, actual_layer) != (expected_status, expected_layer):
            errors.append(
                f"conformance case {case_id}: got {actual_status}/{actual_layer}, "
                f"expected {expected_status}/{expected_layer}"
            )
    return errors, len(cases)


def main() -> int:
    errors: list[str] = []
    schema_bytes = SCHEMA_PATH.read_bytes()
    schema = json.loads(schema_bytes)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    for path in DOCUMENTS:
        document = load_yaml(path)
        structural = sorted(validator.iter_errors(document), key=lambda error: list(error.path))
        errors.extend(
            f"{path.relative_to(ROOT)}:{'/'.join(map(str, error.path)) or '/'}: {error.message}"
            for error in structural
        )
        if not structural and isinstance(document, dict):
            errors.extend(semantic_checks(document, path.relative_to(ROOT)))

    json.loads((ROOT / "docs" / "standards-sources.json").read_text(encoding="utf-8"))
    errors.extend(check_schema_copies(schema_bytes))
    errors.extend(check_portable_asset_copies())
    errors.extend(check_provider_neutrality())
    errors.extend(check_public_surface())
    errors.extend(check_markdown_links())
    conformance_errors, conformance_cases = check_conformance_cases(validator)
    errors.extend(conformance_errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} reference validation error(s)", file=sys.stderr)
        return 1

    print(
        json.dumps(
            {
                "status": "pass",
                "schema": str(SCHEMA_PATH.relative_to(ROOT)),
                "schemaSha256": hashlib.sha256(schema_bytes).hexdigest(),
                "documents": [str(path.relative_to(ROOT)) for path in DOCUMENTS],
                "conformanceCases": conformance_cases,
                "skillSchemaCopies": len(SKILL_SCHEMA_COPIES),
                "providerNeutrality": "pass",
                "publicSurface": "pass",
                "localLinks": "pass",
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
