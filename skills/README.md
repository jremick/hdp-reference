# Agent Skills

These skills package HDP authoring and reconstruction guidance using the
portable Agent Skills directory convention. They are implementation-neutral and
do not require Harness Factory.

## Available skills

- [`create-hdp`](create-hdp/SKILL.md) — create an honest HDP draft from
  requirements, operating context, and evidence.
- [`analyse-existing-harness`](analyse-existing-harness/SKILL.md) — reconstruct
  an evidence-qualified HDP from an existing harness.

## Installation

Copy the complete skill directory into an Agent Skills-compatible directory
recognized by your agent platform. Keep `SKILL.md`, `references/`, `scripts/`,
and `assets/` together.

```bash
cp -R skills/create-hdp /path/to/your/skills/create-hdp
cp -R skills/analyse-existing-harness \
  /path/to/your/skills/analyse-existing-harness
```

Consult the platform's documentation for its skill discovery path and invocation
syntax. Platform-specific metadata MAY be added by an installer, but it is not
part of the HDP specification or these portable source packages.

The validation helpers require Python 3.12, `PyYAML==6.0.3`, and
`jsonschema[format]==4.25.1` when used. The procedural guidance remains useful
without running the helpers, provided validation limits are reported honestly.
