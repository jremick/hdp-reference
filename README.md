# Harness Definition Package

**A draft, implementation-neutral specification for describing what an AI
harness is intended to achieve, how it may operate, and how its outcomes should
be independently evaluated.**

An HDP is a versioned, machine-readable contract that connects intended
outcomes, requirements, operating context, model capabilities, tools,
orchestration, permissions, evaluation, evidence, risks, and change control.
It gives people, models, runtimes, generators, and evaluators a shared source of
truth without prescribing a particular provider or agent framework.

> **Draft 0.1:** HDP is an early community specification proposed for
> experimentation and feedback. It is not an accredited standard,
> certification scheme, or claim that a harness is safe or effective.

## Why HDP?

Most harnesses are assembled from prompts, tool configuration, agent roles,
workflow code, permissions, memory, tests, and operational conventions. Those
parts explain mechanics, but usually do not provide one answer to questions
such as:

- What outcome is the whole system responsible for?
- Which assumptions and exclusions make that claim valid?
- What may the model and its tools access or change?
- Which tests are independent from the generated harness?
- What evidence links an outcome to a requirement, component, test, and result?
- When does a model, runtime, evaluator, or environment change require
  re-evaluation?

HDP makes those relationships explicit and machine-readable.

```text
intent + environment + constraints
                |
                v
      Harness Definition Package
        |          |           |
        v          v           v
   generator    runtime     evaluator
        |          |           |
        +----------+-----------+
                   |
                   v
        traceable outcome evidence
```

The evaluator is deliberately outside the model-harness system. Hidden cases,
answers, evaluator-only prompts, and acceptance secrets are not part of an HDP
that the harness can consume.

## What is included?

- [Draft specification](SPECIFICATION.md) — normative definitions, field
  families, conformance, versioning, and extension rules.
- [JSON Schema](schema/hdp.schema.json) — the canonical structural contract.
- [Semantic rules](schema/semantic-rules.yaml) — cross-field constraints that
  JSON Schema cannot express.
- [Ontology](schema/ontology.yaml) — entities and relationships in the HDP
  conceptual model.
- [Profiles](profiles/) — provider-neutral assurance and domain overlays.
- [Templates](templates/) — provider-neutral starting points.
- [Examples](examples/) — minimal, document-review, and software-development
  definitions.
- [Conformance material](conformance/) — fixtures and expected results for
  implementers.
- [Agent Skills](skills/) — portable authoring and reconstruction workflows.

## Quick start

Start from the smallest complete template:

```bash
cp templates/hdp-starter.yaml my-harness.hdp.yaml
```

Edit the purpose, outcomes, requirements, operating context, capabilities,
permissions, evaluation contract, and traceability graph. Then run the
repository's reference checks:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-validation.txt
.venv/bin/python scripts/validate_reference.py
```

The validation script is repository maintenance tooling. It is not a harness
runtime or a normative implementation of every semantic rule.

## Use the Agent Skills

The repository includes two portable skills:

- [`create-hdp`](skills/create-hdp/SKILL.md) turns supported requirements and
  operational context into an HDP draft without inventing missing intent.
- [`analyse-existing-harness`](skills/analyse-existing-harness/SKILL.md)
  reconstructs an evidence-qualified HDP from prompts, configuration, workflow
  code, tools, tests, permissions, and operating documentation.

Install a skill by copying its complete directory into an Agent
Skills-compatible location supported by your agent platform. The skills do not
assume a particular model provider, coding agent, orchestration framework, or
tool protocol.

## Provider and framework neutrality

HDP describes required capabilities and observable contracts. A separate
binding or implementation profile maps them to concrete models, runtimes,
tools, protocols, sandboxes, deployment targets, and evaluators.

MCP, A2A, OpenAPI, Agent Spec, Agent Skills, or provider-specific formats may be
used as interoperability surfaces. None is the root HDP model, and none is
required for conformance.

[`jremick/harness-factory`](https://github.com/jremick/harness-factory) is an
initial implementation and experimental compiler for HDP. It is non-normative:
the specification in this repository defines the contract, not the factory.

## Documentation

- [Why HDP](docs/why-hdp.md)
- [Conceptual model](docs/concepts.md)
- [Authoring guide](docs/authoring-guide.md)
- [Adoption guide](docs/adoption-guide.md)
- [Standards and specification mapping](docs/standards-mapping.md)
- [Design decisions](docs/design-decisions.md)
- [Governance](GOVERNANCE.md)
- [FAQ](docs/faq.md)
- [Roadmap](ROADMAP.md)

## Current status

The 0.1 contract is a draft intended for public review. The vocabulary,
profiles, semantic-rule expression language, modular package layout, and
conformance levels may change incompatibly before 1.0. No implementation should
claim more than the exact validation layers and profile it has demonstrated.

## Contributing and support

- [Contributing](CONTRIBUTING.md) explains proposal and compatibility
  expectations.
- GitHub Issues are intended for specification defects, use cases, examples,
  and concrete change proposals.
- [Security policy](SECURITY.md) explains how to report vulnerabilities or
  unsafe guidance privately once the repository is public.

## License

Licensed under the [Apache License 2.0](LICENSE).
