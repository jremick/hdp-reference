# Conformance material

The manifest defines small deterministic cases for parser, structural, and
baseline reference behavior. It is intended to help independent implementations
compare diagnostics without treating this repository's validator as the
standard itself.

```bash
python scripts/validate_reference.py
```

Draft 0.1 contains only a starter set. The full semantic-rule catalogue in
[`../schema/semantic-rules.yaml`](../schema/semantic-rules.yaml) remains the
normative source for cross-field behavior. A conforming implementation must
state which rules and profiles it supports and must not promote this baseline
suite into a certification claim.
