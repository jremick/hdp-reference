# Informative software-development profile

This profile demonstrates how an HDP may describe an agent working in a source
repository without selecting a specific coding agent or model provider.

Additional concerns usually include:

- repository instruction authority and scope;
- exact source, test, and generated-artifact boundaries;
- workspace, process, network, and remote-operation permissions;
- deterministic build, test, lint, and diff verification;
- independent functional acceptance outside agent-editable tests;
- evidence that required verification actually ran;
- regression across feature, defect, refactor, and prohibited-action cases; and
- reassessment after model, toolchain, sandbox, evaluator, or dependency change.

See [`../examples/software-development/hdp.yaml`](../examples/software-development/hdp.yaml).
