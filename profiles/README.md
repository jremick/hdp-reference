# Profiles

Profiles add obligations to the core HDP contract without changing core field
semantics. Draft 0.1 defines the intent of `core`, `development`, and
`controlled` profiles in the specification. `production` and `high-assurance`
remain reserved draft labels.

Domain and implementation profiles may specialize task distributions,
capability requirements, evaluation expectations, or runtime bindings. They
must not silently weaken core requirements or widen authority.

- [Software development](software-development.md) is an informative domain
  profile associated with the complete software example.
- [Document review](document-review.md) is an informative domain profile for a
  bounded human-in-the-loop knowledge workflow.

Draft 0.1 does not yet define a canonical machine-readable profile package.
That is a planned 0.2 design item. Implementations should identify profile name,
version, owner, added obligations, compatibility, and unsupported semantics.
