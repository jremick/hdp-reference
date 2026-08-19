---
name: analyse-existing-harness
description: Inspect an existing AI harness and reconstruct an evidence-annotated, provider-neutral Harness Definition Package while preserving observed behavior, declared intent, inference, uncertainty, omissions, contradictions, confidence, and human-confirmation needs.
---

# Analyse an existing harness

Reconstruct only what the available artifacts and authorized observations
support. Never convert implementation mechanics into invented business outcomes
or assurance claims.

## Workflow

1. Establish the harness root, output directory, access boundary, and whether
   runtime observation is authorized. Keep analysis output outside the subject.
2. Run `scripts/inventory_harness.py HARNESS --output inventory.json`. Review
   symlinks, oversized files, binary files, skipped paths, and secret-like file
   names before opening content. Do not print secret values or execute subject
   code merely to inspect it.
3. Inspect applicable artifacts:
   - system, developer, role, and project instructions;
   - packaged skills, agent or workflow definitions, and tool interfaces;
   - orchestration code, hooks, middleware, state, memory, and context logic;
   - permissions, sandboxes, approvals, budgets, failure handling, and stops;
   - tests, evaluators, traces, CI/CD, deployment configuration, and operating
     procedures.
4. Author a candidate using `references/hdp.schema.json` and the core HDP field
   families. Do not use a domain example as evidence. Provider-specific
   artifacts may be cited, but reconstructed semantics remain provider-neutral
   unless the source establishes a genuine provider constraint.
5. For every reconstructed leaf field, add one evidence-map record following
   `references/reconstruction-contract.md`. Use exactly one status:
   `observed`, `declared`, `inferred`, or `unknown`.
6. Preserve exact declared strings when the schema permits. Keep qualifiers,
   time horizons, frequencies, actors, retention, and trace relation types.
   Do not paraphrase merely to make a mapping look cleaner.
7. Record contradictions, missing evidence, alternatives, confidence, and
   whether human confirmation is required. Missing outcome intent, authority,
   acceptance, or evaluator independence blocks generation.
8. Run `scripts/validate_hdp.py DEFINITION` in a Python environment containing
   `PyYAML==6.0.3` and `jsonschema[format]==4.25.1`. Report semantic and profile
   checks not performed by this helper as explicit limits.
9. Retain the reconstructed HDP, evidence map, inventory, coverage summary,
   uncertainty report, contradictions, omissions, and review summary together.

## Evidence statuses

- **observed** — directly exercised or read back under an authorized procedure;
  cite the observation and subject.
- **declared** — explicitly stated in an artifact; cite file and location.
- **inferred** — the best explanation of multiple artifacts; state alternatives
  and require confirmation when material.
- **unknown** — absent, inaccessible, contradictory without resolution, or
  incapable of establishing intent.

Runtime behavior that was not authorized and exercised is not observed. A test
inside the harness is not automatically an independent evaluator. Hidden
fixtures and evaluator secrets remain outside the inspection boundary.

## Completion

Complete when coverage and uncertainty are explicit, evidence locations resolve
or are marked unavailable, contradictions remain visible, intended outcomes are
supported or unknown, and generation-blocking gaps remain blocking. Distinguish
definition conformance, implementation behavior, outcome fitness, and
operational assurance in the final summary.
