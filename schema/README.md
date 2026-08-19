# Normative machine artifacts

- `hdp.schema.json` is the Draft 2020-12 structural contract for the resolved
  Draft 0.1 document.
- `semantic-rules.yaml` identifies cross-field rules that structural validation
  cannot establish.
- `ontology.yaml` defines the conceptual classes and typed relations used by
  the specification and traceability graph.

The JSON Schema is necessary but not sufficient for semantic or profile
conformance. Implementations must report which semantic rule identifiers they
evaluate and which are unsupported.

Provider, model, runtime, and framework bindings are intentionally outside
these core artifacts.
