# Adoption guide

HDP can be adopted incrementally. A team does not need a generator or new
runtime to gain value from the definition.

## New harness

1. Use the `create-hdp` skill or starter template to capture outcomes and
   constraints.
2. Review unknowns and decisions with the people who own the intended outcome.
3. Validate the resolved definition.
4. Create a runtime binding without widening HDP authority.
5. Implement or generate the harness.
6. Evaluate the exact model-harness-runtime-environment subject independently.
7. retain traceable evidence and reassess after material change.

## Existing harness

1. Use `analyse-existing-harness` to inventory prompts, tools, workflows,
   permissions, tests, traces, deployment configuration, and operating docs.
2. Classify every reconstructed value as observed, declared, inferred, or
   unknown.
3. Do not infer business outcomes from mechanics.
4. Validate the candidate HDP and identify generation-blocking unknowns.
5. Obtain human confirmation for intent, acceptance, authority, and risk.
6. Use the resulting gaps to prioritize harness improvements.

## Implementer responsibilities

An HDP implementation should publish:

- supported HDP and schema versions;
- supported profiles and semantic rules;
- parsing and canonicalization behavior;
- binding and translation loss;
- validation layers performed;
- generated artifact provenance;
- runtime enforcement boundaries; and
- known unsupported semantics.

## Relationship to Harness Factory

Harness Factory is an experimental implementation that can validate and compile
HDPs into runtime-specific artifacts. It is useful for testing the standard,
but its behavior is not automatically normative. A discrepancy should be
resolved against this repository's versioned specification and recorded as a
specification defect, implementation defect, or open design question.
