# Security policy

HDP is a draft specification and set of reusable templates and Agent Skills.
Security issues may include unsafe default permissions, evaluator-boundary
leaks, examples that encourage secret exposure, validation bypasses, or scripts
that read outside their declared analysis root.

Do not include credentials, private harness content, hidden evaluation material,
or exploit details in a public issue. Once the repository is public, use
GitHub's private vulnerability reporting feature. Until then, contact the
maintainer through the private repository access channel.

Reports should identify the affected file or specification section, the
security consequence, a minimal reproduction where safe, and any known
workaround. A specification-compliant document is not automatically secure;
implementations must still enforce permissions and runtime isolation.
