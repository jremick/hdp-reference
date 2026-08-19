# Contributing

HDP is an early draft. Concrete use cases, contradictions, missing concepts,
interoperability mappings, examples, templates, and conformance cases are
welcome.

Before proposing a normative change:

1. Describe the user or implementer problem independently of a particular
   provider or framework.
2. Explain why the existing field model, semantic rules, profile mechanism, or
   extension envelope cannot represent it.
3. Identify compatibility, migration, security, evaluator-boundary, and
   traceability consequences.
4. Update the specification, schema, semantic rules, examples, skills, and
   conformance material together when they are affected.
5. Run `python scripts/validate_reference.py` in the documented validation
   environment.

Provider-specific behavior belongs in a non-normative binding or profile unless
it expresses a genuinely general semantic requirement. Contributions are
licensed under Apache-2.0 under the repository's inbound-equals-outbound terms.
