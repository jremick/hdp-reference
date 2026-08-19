# Harness Definition Package 0.1

Status: **draft specification**
Version: **0.1.0**
Schema identifier: **`urn:hdp:schema:0.1.0`**

HDP is an implementation-neutral information contract for defining, generating,
operating, evaluating, and governing an AI harness. This document is normative
for Draft 0.1 except where a section is explicitly marked informative.

HDP is not an accredited standard and this repository does not operate a
certification program.

## 1. Normative language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**,
and **MAY** express requirement strength. A SHOULD requirement may be departed
from only when the reason and consequence are documented.

The canonical structural contract is
[`schema/hdp.schema.json`](schema/hdp.schema.json). Cross-field requirements are
identified in [`schema/semantic-rules.yaml`](schema/semantic-rules.yaml).

## 2. Definitions

### 2.1 AI harness

An **AI harness** is the engineered control system around one or more models
that constructs context, exposes capabilities, coordinates execution, manages
state, constrains authority, observes behavior, handles failure, and produces
verifiable outputs and evidence within a runtime and environment.

A prompt alone is not a complete harness. A harness may include prompts, roles,
tools, workflows, adapters, memory, policy, permissions, tests, tracing, human
approval, deployment configuration, and operating procedures.

### 2.2 Harness Definition Package

A **Harness Definition Package (HDP)** is a versioned, machine-readable set of
linked definitions that states:

1. the outcomes a model-harness-environment system is intended to achieve;
2. the operating context, assumptions, constraints, and exclusions;
3. the functional, quality, safety, security, privacy, and governance
   requirements imposed on the harness;
4. the capabilities, contracts, control flow, state, resources, and runtime
   properties needed to implement it;
5. the evaluation boundary, scenarios, measures, tests, and evidence needed to
   judge it; and
6. the traceability, change-control, compatibility, limitation, and residual
   risk information needed to interpret claims over time.

An HDP MUST be understandable without undocumented implementation assumptions.
Unknown intent MUST remain unknown or explicitly unresolved; an author or tool
MUST NOT invent business outcomes merely to complete the structure.

### 2.3 System boundaries

- **Model** — a model or model service that produces inferences. A model is not
  the harness that controls its use.
- **Harness** — the control system described above. It may call one or more
  models.
- **Runtime** — the process, agent host, workflow engine, container, service, or
  other execution substrate that realizes harness behavior.
- **Environment** — the surrounding systems, data, users, organizational
  procedures, infrastructure, and conditions that affect operation.
- **Task** — a bounded unit of work sampled from an intended task distribution.
- **Evaluator** — a component or operator that applies defined measures and
  acceptance logic to a named subject.
- **Evidence** — a recorded observation with subject identity, provenance,
  collection method, integrity information, and links to the claims or
  requirements it bears on.

The final acceptance evaluator SHOULD be external to the model-harness system.
Hidden fixtures, labels, answers, prompts, or acceptance logic MUST NOT be made
available to the harness merely because the HDP describes their public
contract.

## 3. Assurance vocabulary

- **Generation** transforms an HDP into implementation artifacts for a target
  runtime or framework.
- **Verification** determines whether an artifact or behavior satisfies a
  specified requirement.
- **Validation** determines whether a definition or system is suitable for its
  intended use and outcomes.
- **Structural conformance** means a resolved document satisfies the canonical
  JSON Schema.
- **Semantic conformance** means applicable cross-field rules, references,
  trace paths, and declared invariants are satisfied.
- **Profile conformance** means the additional obligations of a named profile
  are satisfied.
- **Fitness for outcome** is evidence that the complete
  model-harness-runtime-environment system meets its declared outcome
  thresholds over the intended task distribution.
- **Operational assurance** is justified confidence that required controls and
  outcomes continue to hold during operation and change.

Conformance is not fitness for outcome. Passing generated tests is not, by
itself, independent validation. A conforming HDP is not proof that its proposed
harness is safe, secure, effective, or deployed as declared.

## 4. Conceptual model

The normative entity and relation catalogue is
[`schema/ontology.yaml`](schema/ontology.yaml). The central relationships are:

```text
Purpose -> Outcome -> Measure -> Threshold
                  \
                   -> Requirement -> Component -> Test -> Evidence

Environment -> Task distribution -> Scenario
Capability requirement -> Model / Tool / Human / External system binding
Governance -> Permission / Data class / Approval / Prohibition
Evaluation contract -> Dataset / Fixture / Metric / Evaluator / Test
Change -> Compatibility claim -> Reassessment trigger
```

Every material completion claim SHOULD be traceable from an intended outcome
through requirements and implementation components to tests and evidence.

## 5. Canonical document

### 5.1 Serialization

The canonical interchange representation is a JSON object conforming to JSON
Schema Draft 2020-12. YAML MAY be used as an authoring syntax when it resolves
without loss to the same JSON data model.

Implementations accepting YAML SHOULD reject duplicate keys, aliases, merge
keys, non-string mapping keys, unsupported tags, and resource-exhaustion input.
They SHOULD document scalar-typing behavior and canonicalization rules.

### 5.2 Resolved authority

Draft 0.1 defines one fully resolved HDP document as the validation authority.
An implementation MAY provide modular files, includes, overlays, or governed
subpackages, but it MUST:

- define deterministic resolution and precedence;
- identify every source artifact and version;
- produce the resolved document used for validation and generation; and
- retain provenance from resolved values to authoring sources.

### 5.3 Stable identity

Entities that participate in references or traceability MUST have stable IDs.
Names and labels MUST NOT be treated as identity. References MUST resolve to the
required entity kind. Implementations MUST report duplicates and unresolved or
kind-incompatible references.

## 6. Required information families

A Draft 0.1 `HarnessDefinition` contains these top-level families:

| Family | Normative purpose |
| --- | --- |
| `metadata` | Identity, ownership, version, status, and provenance |
| `purpose` | Summary, target users, intended outcomes, non-goals, excluded uses |
| `operationalContext` | Environments, task distribution, assumptions, dependencies, exclusions |
| `success` | Measures, thresholds, and acceptance criteria |
| `requirements` | Functional and quality obligations with verification references |
| `models` | Capability requirements, provider constraints, routing, and fallback policy |
| `contracts` | Input, output, artifact, and interface contracts |
| `context` | Context construction, knowledge sources, and conflict policy |
| `tools` | Tool interfaces and external systems with side-effect declarations |
| `orchestration` | Roles, stages, delegation, and control flow |
| `state` | Working state, durable memory, and lifecycle |
| `governance` | Permissions, data classification, prohibitions, and human approvals |
| `resources` | Budgets, timeouts, rate limits, and stopping conditions |
| `failures` | Failure taxonomy, recovery, retry, and escalation |
| `observability` | Tracing, events, interventions, redaction, and retention |
| `safety` | Security, privacy, safety, and compliance constraints |
| `evaluation` | Boundary, datasets, fixtures, scenarios, metrics, evaluators, and tests |
| `runtime` | Abstract profile, deployment targets, and sandbox expectations |
| `monitoring` | Baselines, drift rules, alerts, and reassessment triggers |
| `traceability` | Typed nodes and edges linking outcomes to evidence |
| `evolution` | Compatibility, change control, and deprecation |
| `limitations` | Known limitations that qualify interpretation or use |
| `risks` | Risk, likelihood, impact, treatment, and residual exposure |
| `extensions` | Namespaced, explicitly governed non-core information |

The schema defines exact field types and cardinalities. Authors MUST NOT use an
empty value to imply evidence of absence when the information is merely
unknown.

## 7. Outcomes, requirements, and measures

Intended outcomes MUST name the effect for a user, operator, organization, or
environment rather than only an implementation activity. Each outcome MUST
reference one or more measures.

Every MUST-priority requirement MUST:

- be necessary to a declared outcome, constraint, or governance obligation;
- have a stable ID and an unambiguous normative statement;
- reference at least one verification method or test; and
- participate in a complete trace path appropriate to the active profile.

Measures MUST define method, unit, and interpretation direction. Hard
acceptance thresholds MUST be machine-evaluable or identify the controlled
human or inferential procedure used to decide them.

## 8. Capabilities and bindings

The core HDP declares required capabilities and constraints, not vendor product
names. A binding maps abstract requirements to concrete models, tools, human
roles, interfaces, protocols, runtimes, or deployment systems.

A binding MUST NOT widen authority beyond the HDP. It MUST fail or record an
explicit unresolved requirement when:

- a required capability has no compatible target;
- the target needs undeclared network, filesystem, process, data, or human
  authority;
- a hard budget or prohibition cannot be enforced; or
- translation drops semantics that affect safety, security, evaluation, or
  outcome claims.

Provider-specific identifiers MAY appear in a non-normative binding or
implementation profile. They MUST NOT be required by the core schema.

## 9. Governance and enforcement

Permissions MUST default to deny unless the active profile explicitly defines a
different baseline. Filesystem, network, tool, data, process, and approval
authority SHOULD be independently enumerable.

A declaration is not enforcement. An implementation claiming an enforced
permission, timeout, budget, sandbox, or stopping condition MUST identify the
enforcement boundary and retain evidence that the control was active for the
evaluated subject.

Secrets MUST NOT appear in HDPs, templates, generated artifacts, examples, or
evidence. Secret requirements SHOULD name an injection mechanism or secret
reference, never a credential value.

## 10. Evaluation boundary

An HDP MUST distinguish:

- tests available to the harness for development or verification;
- public acceptance interfaces;
- restricted or hidden evaluator material; and
- the independent authority that decides outcome acceptance.

The public HDP MAY include opaque fixture IDs, commitments, metrics, custody,
and evidence artifact contracts. It MUST NOT expose hidden fixture content,
answers, evaluator-only prompts, labels, or secrets to the harness.

If an LLM judge is used, the HDP MUST declare the rubric, model capability or
controlled identity, repetitions, aggregation, and uncertainty treatment.

## 11. Traceability and evidence

Trace edges use typed relations. Implementations MUST NOT substitute relation
types merely to create a connected graph.

For controlled and stronger profiles, every MUST requirement MUST participate
in an ordered path equivalent to:

```text
outcome -> requirement -> component -> test -> evidence
```

An evidence record SHOULD identify:

- the exact subject and relevant versions or digests;
- the proposition, requirement, or outcome it bears on;
- collector and collection method;
- time and environment;
- completeness, access class, and retention;
- integrity information; and
- contradictions, gaps, or uncertainty.

Trace or log existence alone does not prove authorization, correctness, or
outcome success.

## 12. Conformance levels

Draft 0.1 defines document conformance layers and named assurance profiles.

### 12.1 Validation layers

1. **Transport validation** — safe parsing, bounded input, and supported
   serialization.
2. **Structural validation** — canonical JSON Schema validation.
3. **Semantic validation** — rule catalogue, reference, trace, and invariant
   validation.
4. **Profile validation** — obligations introduced by a named profile.
5. **Implementation verification** — generated or implemented artifacts match
   the resolved HDP and binding.
6. **Outcome validation** — independent acceptance over declared scenarios and
   task distribution.
7. **Operational assurance** — monitoring and reassessment of the deployed
   subject.

An implementation MUST state which layers it performed. It MUST NOT summarize a
lower-layer pass as a higher-layer claim.

### 12.2 Profiles

- **core** — structurally and semantically coherent HDP.
- **development** — adds implementable requirements, components, tests, and
  development evidence.
- **controlled** — adds deny-by-default authority, independent evaluation,
  complete MUST trace paths, hard-resource handling, and intervention records.
- **production** — reserved draft profile for deployment, monitoring, support,
  compatibility, and operational controls.
- **high-assurance** — reserved draft profile requiring a separately governed
  assurance case and stronger evidence custody.

Draft 0.1 fully specifies core, development, and controlled intent. Production
and high-assurance are labels for experimentation and MUST NOT be treated as
certification claims.

### 12.3 Conformance statement

A conformance statement MUST include:

- HDP version and profile;
- resolved document digest;
- validator or implementation name and version;
- validation layers performed;
- passed, failed, skipped, and unsupported rules;
- evidence references; and
- known limitations.

## 13. Extensions

Extensions MUST be placed under `extensions` and use a collision-resistant
namespace. An extension MUST declare its owner, schema or contract, version,
criticality, and fallback behavior when those properties affect generation or
interpretation.

An implementation MUST fail closed when an unknown required extension could
change authority, safety, evaluation, evidence, or outcome meaning. It MAY
retain an unknown optional extension without interpreting it.

Extensions MUST NOT redefine core field semantics invisibly.

## 14. Versioning and compatibility

HDP uses semantic versioning for the contract:

- patch — clarification or correction that does not change valid document
  meaning;
- minor — backward-compatible optional vocabulary or profile addition;
- major — incompatible syntax or semantic change.

Pre-1.0 drafts may make incompatible changes with an explicit migration record.
Implementations MUST preserve the source HDP version and SHOULD report the
highest version and profiles they support.

Generated artifacts, bindings, evaluator packages, and evidence have identities
and versions independent from the HDP version. Changing any material subject
component SHOULD trigger reassessment according to the HDP's monitoring rules.

## 15. Interoperability

Interoperability formats MAY represent parts of an HDP, including model or
agent topology, tool interfaces, external-agent discovery, HTTP APIs, skills,
traces, or assurance claims.

Every translation SHOULD record source and target versions, mapped entities,
dropped or approximated semantics, artifact digests, and whether loss affects
execution or assurance. No particular provider, protocol, framework, model, or
agent host is required by Draft 0.1.

## 16. Security and privacy considerations

HDP consumers should treat definitions and analysed harnesses as untrusted
input. Parsers, analysers, generators, and validators SHOULD:

- bound bytes, depth, items, aliases, CPU time, and output;
- reject traversal and symlink escapes;
- avoid executing inspected harness content;
- redact secret-like values without printing them;
- separate evaluator custody from the harness workspace;
- validate bindings before enabling tools or external systems;
- preserve negative results and interventions; and
- bind evidence to immutable subject identities where practical.

## 17. Open design questions

Draft 0.1 intentionally leaves these questions open for public review:

- canonical modular package and resolution semantics;
- registration and governance of profile and extension namespaces;
- a portable semantic-rule expression and execution model;
- minimum evidence required for production and high-assurance profiles;
- standard machine-readable conformance-report format;
- compatibility with future versions of adjacent specifications; and
- governance needed before describing HDP as more than a draft specification.
