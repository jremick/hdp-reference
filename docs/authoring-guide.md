# Authoring guide

Start with [`templates/hdp-starter.yaml`](../templates/hdp-starter.yaml). The
template is intentionally complete so omitted sections are deliberate rather
than undocumented.

## 1. Begin with outcomes

Write the user, operator, organizational, or environmental effect the complete
system should produce. Avoid implementation activities such as “call a model”
or “run tests.” For each outcome, define a measure and threshold.

If the outcome is not known, stop and record the question. Do not infer it from
the existing mechanism.

## 2. Bound the operating context

Describe intended environments and task distribution. Record assumptions,
dependencies, exclusions, criticality, frequency, and important variations.
Evaluation scenarios should sample this distribution rather than only the
easiest happy path.

## 3. Derive requirements

Write functional, quality, governance, safety, and evidence obligations.
Reserve MUST for obligations necessary to the outcome or an active constraint.
Every MUST requirement needs a verification reference and a trace path.

## 4. Specify abstract capabilities

Describe the capability needed from a model, tool, external system, or human.
Keep provider identifiers in bindings. Declare side effects and interface
contracts explicitly.

## 5. Define control and state

Describe roles, stages, transitions, delegation, working state, durable memory,
lifecycle, recovery, and escalation. State how concurrent or repeated work is
coordinated when it matters.

## 6. Deny authority by default

Enumerate filesystem, network, tool, data, process, and approval authority.
Add hard budgets, timeouts, rate limits, stopping conditions, and prohibited
actions. Identify which outer runtime is expected to enforce each hard control.

## 7. Design evaluation independently

Define datasets, scenarios, metrics, evaluators, tests, visibility, and evidence
artifacts. Keep evaluator-only material in a separately controlled package. If
an inferential judge is used, define its rubric and uncertainty treatment.

## 8. Complete traceability

Link every critical outcome through requirements and components to tests and
evidence. Use the exact relation types from the ontology. Record limitations
and residual risks that qualify the claim.

## 9. Validate in layers

Run transport, structural, semantic, and profile checks separately. A schema
pass is not a semantic or outcome pass. Record unsupported checks instead of
silently skipping them.

## Authoring checklist

- Outcomes describe effects rather than mechanics.
- Measures and thresholds are interpretable.
- The task distribution and exclusions are explicit.
- Every MUST requirement has verification and trace coverage.
- Provider choices are bindings, not core requirements without justification.
- Permissions and hard controls identify enforcement boundaries.
- Hidden evaluation material is not present.
- Unknowns, contradictions, limitations, and residual risks remain visible.
- Versioning and reassessment rules identify material subject changes.
