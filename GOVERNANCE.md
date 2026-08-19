# Governance

HDP is currently a maintainer-led draft specification, not the output of an
accredited standards organization.

## Decision process

Normative changes should begin with a public issue describing the general use
case, current gap, proposed semantics, compatibility consequences, security and
evaluation implications, and alternatives. A pull request should update every
affected contract artifact and conformance case.

The maintainer records accepted decisions in the specification, changelog, and
design-decision documentation. Material objections and unresolved alternatives
should remain visible rather than being erased from the rationale.

## Compatibility

Before 1.0, incompatible changes are allowed only with explicit migration notes
and a version change. After 1.0, the semantic-versioning rules in the
specification govern the core contract.

## Implementations

No implementation has privileged authority over the specification. Harness
Factory is an initial experimental implementation. Independent implementations
and conformance reports are encouraged.

## Future governance

Moving beyond a maintainer-led draft will require transparent namespace
ownership, a proposal process, conflict-of-interest handling, versioned releases,
and participation from independent implementers and users. Draft 0.1 does not
claim that governance maturity.
