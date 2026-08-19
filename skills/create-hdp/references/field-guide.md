# HDP field guide

Use this guide when deciding where source information belongs.

| Source information | HDP family |
| --- | --- |
| Identity, owner, version, provenance | `metadata` |
| Who benefits and what changes for them | `purpose` |
| Environments, task variation, assumptions, dependencies | `operationalContext` |
| Measures, thresholds, acceptance | `success` |
| Functional and quality obligations | `requirements` |
| Required inference capabilities and routing constraints | `models` |
| Inputs, outputs, artifacts, interfaces | `contracts` |
| Prompt/context assembly and knowledge sources | `context` |
| Tools and external systems | `tools` |
| Roles, stages, flow, delegation | `orchestration` |
| Working state, memory, lifecycle | `state` |
| Permissions, data handling, prohibitions, approvals | `governance` |
| Budgets, timeouts, rates, stop conditions | `resources` |
| Failures, retries, recovery, escalation | `failures` |
| Traces, events, interventions | `observability` |
| Security, privacy, safety, compliance | `safety` |
| Datasets, scenarios, metrics, evaluators, tests | `evaluation` |
| Abstract runtime profile, targets, sandbox expectation | `runtime` |
| Baselines, drift, alerts, reassessment | `monitoring` |
| Outcome-to-evidence graph | `traceability` |
| Compatibility, change control, deprecation | `evolution` |
| Known qualification of claims | `limitations` |
| Likelihood, impact, treatment, residual exposure | `risks` |
| Namespaced non-core information | `extensions` |

## Evidence threshold

Use a value only when it is declared by an authoritative source, directly
observed under an authorized procedure, or clearly identified as an inference.
Business intent, acceptance, authority, and risk normally require human owner
confirmation when not explicitly declared.
