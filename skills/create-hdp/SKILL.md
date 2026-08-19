---
name: create-hdp
description: Create or revise a provider-neutral Harness Definition Package from supported outcomes, requirements, operating context, constraints, evaluation needs, and evidence. Use when defining an AI harness before implementation or bringing an existing harness requirement set into the HDP draft format.
---

# Create an HDP

Produce an implementation-neutral definition that another capable person,
model, generator, runtime, and evaluator can interpret without undocumented
assumptions.

## Source hierarchy

1. Treat the user's supplied outcomes, requirements, policies, and operating
   facts as authoritative within their stated scope.
2. Use `references/field-guide.md` to map supported information into HDP field
   families.
3. Use `assets/hdp-starter.yaml` as the structural starting point and
   `references/hdp.schema.json` as the structural contract.
4. Preserve contradictions and unknowns. Do not invent business outcomes,
   acceptance thresholds, permissions, data classifications, evaluator
   independence, or runtime enforcement.

## Workflow

1. Establish the intended outcome, target users, operating environment, task
   distribution, exclusions, and decision owner.
2. Define measurable outcomes and hard acceptance thresholds before choosing
   implementation mechanisms.
3. Derive functional, quality, governance, safety, privacy, and evidence
   requirements. Every MUST requirement needs verification.
4. Describe abstract model, tool, human, interface, state, and orchestration
   capabilities. Keep provider and framework choices in a separate binding or
   clearly non-normative implementation note.
5. Declare permissions, prohibitions, approvals, budgets, timeouts, stopping
   conditions, failure handling, monitoring, and reassessment triggers.
6. Define an evaluator boundary outside the harness. Keep hidden cases,
   answers, judge prompts, and evaluator secrets out of the HDP.
7. Build typed trace paths from outcomes through requirements and components to
   tests and evidence.
8. Record assumptions, unresolved questions, limitations, residual risks, and
   the smallest human confirmations needed before generation or deployment.
9. Run `scripts/validate_hdp.py DEFINITION` in a Python environment containing
   `PyYAML==6.0.3` and `jsonschema[format]==4.25.1`. Report structural validation
   separately from semantic, profile, implementation, and outcome validation.

## Authoring rules

- Use stable IDs; names do not establish identity.
- Use MUST, SHOULD, and MAY only for normative statements.
- An empty collection asserts there are no entries. Use an explicit unresolved
  record when the truth is unknown.
- Do not name a provider in the core definition unless the intended outcome or
  external policy genuinely requires it; document the reason when it does.
- A declared control is not enforcement. Name the runtime boundary expected to
  enforce hard constraints.
- Generated or harness-editable tests are not an independent final oracle.
- Do not place credentials or secret values in the definition.

## Completion

Return the HDP, a short unresolved-decisions list, validation results by layer,
and any separate implementation binding. Do not call the HDP generation-ready
when a missing outcome, hard requirement, permission, evaluator boundary, or
acceptance threshold could materially change the harness.
