# Standards and specification mapping

HDP is an original integration proposal. It adopts concepts from established
standards and emerging specifications where they fit, while retaining gaps as
explicit HDP responsibilities.

| Source | Classification | Reused concepts | HDP responsibility retained |
| --- | --- | --- | --- |
| JSON Schema Draft 2020-12 | Mature open specification | Structural types and validation | Cross-field semantics, runtime, outcome evidence |
| ISO/IEC/IEEE 29148:2018 | Formal standard | Requirements quality and traceability | AI capability, runtime, evaluator custody |
| NIST AI RMF 1.0 and AI 600-1 | Government framework and guidance | Risk and TEVV framing | Portable executable information contract |
| OMG SACM 2.3 | Formal standard | Claim, argument, evidence concepts | Harness generation and operational binding |
| OpenAPI | Industry specification | HTTP interface contracts | Harness purpose, authority, lifecycle, evaluation |
| MCP | Emerging protocol | Model/tool/context transport | Authorization, stopping, recovery, outcome fitness |
| A2A | Emerging protocol | External agent interface and discovery | Internal harness governance and evidence |
| Agent Spec | Emerging specification | Portable agent and flow representation | Purpose, permissions, independent assurance |
| Agent Skills | Emerging portable format | Procedural instructions and packaged resources | Enforcement and system-level outcome contract |
| OASF | Emerging schema framework | Agent discovery and capability metadata | Verified capability and assurance state |

The detailed source registry is
[`standards-sources.json`](standards-sources.json). Versions in that registry
record the research baseline for Draft 0.1; implementers should verify current
versions when building adapters.

Adjacent formats should be mapped through versioned adapters. A translation
should state what was mapped, dropped, approximated, or made implementation
specific. No adjacent format is required for HDP conformance.
