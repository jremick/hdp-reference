# Design decisions

## HDP is an information contract, not a runtime

The core defines semantics needed across authors, generators, runtimes, and
evaluators. Concrete execution belongs to implementations and bindings.

## The evaluator is outside the harness

Final acceptance must not be under the authority of the system being judged.
The public HDP carries the evaluation contract while hidden material remains in
separate custody.

## One resolved definition is authoritative in Draft 0.1

Modular authoring is useful, but include and overlay precedence can silently
change meaning. Draft 0.1 validates one deterministic resolved document while a
future version defines a standard modular package.

## JSON Schema is necessary but insufficient

JSON Schema provides broad interoperability for structural validation. Stable
ID resolution, trace paths, permission contradictions, profile obligations, and
evaluator-boundary rules require an additional semantic-rule catalogue.

## Bindings cannot widen authority

Provider and framework mappings are replaceable. A binding may satisfy or fail
abstract requirements, but it cannot silently add permission or weaken a hard
constraint.

## Evidence is not a claim

A trace, test output, or log is an observation. Its relevance depends on subject
identity, provenance, integrity, collection method, completeness, and the claim
it supports or refutes.

## Unknown intent remains unknown

Reconstruction tools must not turn implementation mechanics into invented
business outcomes. Incomplete but honest definitions are preferable to valid
documents containing false intent.
