# Frequently asked questions

## Is HDP a formal standard?

No. Draft 0.1 is a proposed open specification for experimentation and review.
Calling it a formal or accredited standard would be misleading.

## Is HDP only for coding agents?

No. The core model is intended for any outcome-bearing AI harness, including
knowledge work, operations, research, support, document processing, and
human-in-the-loop workflows. Software development is one example profile.

## Does HDP require a particular model or provider?

No. It declares capability requirements. Provider and model selections belong
in bindings unless an intended use genuinely requires a named service.

## Does HDP replace MCP, A2A, OpenAPI, Agent Spec, or Agent Skills?

No. Those formats can provide interface, discovery, topology, or procedural
artifacts. HDP connects them to outcomes, governance, evaluation, and evidence.

## Is a schema-valid HDP safe to run?

No. Schema validity proves structure only. Semantic validation, binding review,
implementation verification, runtime enforcement, independent outcome
evaluation, and operational monitoring are separate obligations.

## Can the evaluator be generated from the same HDP?

The public evaluation contract can be generated or checked. Hidden fixtures,
answers, judge prompts, and final acceptance authority must remain outside the
harness's control and context.

## Why are all top-level families present in the starter template?

The complete shape makes absence explicit. An empty collection means the author
has considered that family and asserts no entries; it must not be used when the
information is simply unknown.

## Where is the runnable implementation?

[`jremick/harness-factory`](https://github.com/jremick/harness-factory) contains
an experimental implementation. This repository remains the versioned draft
contract and adoption surface.
