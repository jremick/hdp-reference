#!/usr/bin/env python3
"""Perform a small provider-neutral structural check of an Agent Skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_skill.py SKILL_DIRECTORY", file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).resolve()
    entrypoint = root / "SKILL.md"
    errors: list[str] = []
    if not entrypoint.is_file():
        errors.append("SKILL.md is missing")
    else:
        text = entrypoint.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            errors.append("SKILL.md must begin with YAML frontmatter")
        else:
            end = text.find("\n---\n", 4)
            frontmatter = yaml.safe_load(text[4:end])
            if not isinstance(frontmatter, dict):
                errors.append("frontmatter must be a mapping")
            else:
                name = frontmatter.get("name")
                description = frontmatter.get("description")
                if name != root.name:
                    errors.append(f"frontmatter name {name!r} must equal directory {root.name!r}")
                if not isinstance(name, str) or not NAME.fullmatch(name):
                    errors.append("name must use lowercase letters, digits, and hyphens")
                if not isinstance(description, str) or not description.strip():
                    errors.append("description is required")
                elif len(description) > 1024:
                    errors.append("description exceeds 1024 characters")
        if re.search(r"\b(TODO|TBD|PLACEHOLDER)\b", text):
            errors.append("unfinished scaffold marker found in SKILL.md")

    for path in root.rglob("*"):
        if path.is_symlink():
            errors.append(f"symlink is not portable: {path.relative_to(root)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"VALID {root.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
