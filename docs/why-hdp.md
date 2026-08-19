# Why HDP exists

AI harness engineering has a specification gap.

Prompts describe instructions. Tool schemas describe calls. Workflow graphs
describe control flow. Runtime configuration describes a host. Tests describe
selected checks. Traces describe events. None of those, alone, defines the
whole outcome-bearing system.

## The missing contract

When a harness fails, the cause may be the task definition, context, model,
tool, state, permission, workflow, evaluator, runtime, environment, or a change
in their interaction. Without a shared definition, teams often cannot tell:

- whether the implementation matched its intended design;
- whether a test measures the intended outcome;
- whether a passing result came from an independent evaluator;
- whether a deployment has the permissions and controls assumed by evaluation;
- which claim is invalidated when a component changes; or
- which missing business fact was guessed during generation.

HDP treats the harness as a system, not a prompt bundle. It joins intent,
mechanics, governance, evaluation, and evidence using stable identities and
typed trace relationships.

## Why not adopt one existing format?

Existing specifications solve valuable adjacent problems: API contracts, tool
transport, agent discovery, executable agent graphs, portable skills, tracing,
requirements, risk management, and assurance cases. HDP does not replace them.
It provides the integration layer that says which parts are required, how much
authority they have, what outcome they serve, and how the result is evaluated.

## Intended uses

- Author a harness before selecting a provider or framework.
- Generate provider-specific harness artifacts from a governed definition.
- Compare implementations against the same outcome and constraint contract.
- Reconstruct an HDP from an existing harness and expose missing intent.
- Build independent evaluation plans and traceable evidence.
- Review permissions, assumptions, limitations, and residual risks before use.
- Determine when a material change requires regression or reassessment.

## Non-goals

HDP is not a model format, agent runtime, workflow engine, tool protocol,
benchmark, or certification scheme. It does not make probabilistic behavior
deterministic, and a valid HDP does not make an implementation trustworthy.
