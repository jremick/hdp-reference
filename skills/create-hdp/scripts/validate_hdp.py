#!/usr/bin/env python3
"""Portable structural and baseline-reference validator for an HDP document."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker


class StrictLoader(yaml.SafeLoader):
    def compose_node(self, parent: Any, index: Any) -> Any:
        if self.check_event(yaml.AliasEvent):
            event = self.peek_event()
            raise yaml.constructor.ConstructorError(
                None, None, "YAML aliases are not supported", event.start_mark
            )
        return super().compose_node(parent, index)


def construct_mapping(loader: StrictLoader, node: yaml.MappingNode, deep: bool = False):
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str) or key == "<<" or key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"unsupported or duplicate mapping key: {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
)


REFERENCE_KEYS = {
    "allowedIds", "evaluatorId", "evaluatorIds", "evidenceArtifactId",
    "expectedOutcomeIds", "failureIds", "fixtureIds", "from", "measureId",
    "measureIds", "metricIds", "ref", "requirementIds", "roleIds",
    "scenarioIds", "taskClassId", "testId", "to", "toolIds",
    "verificationIds",
}


def walk(value: Any, pointer: str = ""):
    yield pointer or "/", value
    if isinstance(value, dict):
        for key, item in value.items():
            yield from walk(item, f"{pointer}/{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from walk(item, f"{pointer}/{index}")


def baseline_semantics(document: dict[str, Any]) -> list[str]:
    ids: set[str] = set()
    duplicates: set[str] = set()
    references: list[tuple[str, str]] = []
    for pointer, value in walk(document):
        if not isinstance(value, dict):
            continue
        entity_id = value.get("id")
        if isinstance(entity_id, str):
            if entity_id in ids:
                duplicates.add(entity_id)
            ids.add(entity_id)
        for key, item in value.items():
            if key not in REFERENCE_KEYS:
                continue
            if key == "ref" and value.get("kind") not in {
                "outcome", "requirement", "component", "test", "evidence",
                "risk", "control",
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
    errors = [f"duplicate ID: {value}" for value in sorted(duplicates)]
    errors.extend(
        f"{pointer}: unresolved reference {reference}"
        for pointer, reference in references
        if reference not in ids
    )
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_hdp.py DEFINITION", file=sys.stderr)
        return 2
    definition = Path(sys.argv[1])
    schema_path = Path(__file__).resolve().parents[1] / "references" / "hdp.schema.json"
    try:
        document = yaml.load(definition.read_text(encoding="utf-8"), Loader=StrictLoader)
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        structural = sorted(validator.iter_errors(document), key=lambda error: list(error.path))
        semantic = baseline_semantics(document) if not structural and isinstance(document, dict) else []
    except Exception as error:
        print(json.dumps({"status": "fail", "layer": "transport", "error": str(error)}, indent=2))
        return 1

    errors = [
        {"pointer": "/" + "/".join(map(str, error.path)), "message": error.message}
        for error in structural
    ]
    errors.extend({"pointer": "/", "message": message} for message in semantic)
    result = {
        "status": "pass" if not errors else "fail",
        "structuralValidation": "pass" if not structural else "fail",
        "baselineReferenceValidation": "pass" if not semantic else "fail",
        "errors": errors,
        "limits": [
            "The helper does not implement the complete semantic-rule catalogue.",
            "It does not establish profile conformance, implementation correctness, outcome fitness, or operational assurance.",
        ],
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
