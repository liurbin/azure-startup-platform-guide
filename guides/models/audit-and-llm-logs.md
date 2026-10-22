# Establish model request auditing and safe LLM logs

Policy checked: [set on review]. Status: draft; sources not re-verified; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Task guide

| Task card | |
|---|---|
| Use this for | Establish model request and trace audit coverage; Decide whether LLM content is collected and who may access or export it |
| Reader | Security/data owners and authorized platform/log administrators |
| Applies to | Foundry model diagnostics and application/gateway telemetry; Log Analytics access, query auditing and retention |
| Prepare | Resource/endpoint, UTC interval and audit purpose; Existing telemetry destinations, approved readers and retention requirements |
| You will get | A coverage/privacy matrix, evidence gaps and a minimal approved logging and access-control plan. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference only while draft. Do not execute read-only checks or changes until human source review and explicit customer authorization. Collection, content capture, export, access and retention changes require separate approval.

Confirm the exact resource/endpoint, audit purpose, UTC interval, existing telemetry destinations, authorized readers and data/retention owner. Cover platform diagnostics and application/gateway/agent exporters separately. Never request keys, authorization headers, customer prompts/completions, attachments or raw private logs in chat, Git or an unapproved agent.

## Official policy and live state

Management Activity Log, request/trace metadata and LLM content serve different purposes. They are not interchangeable or automatically all enabled. [Platform audit](../network/audit.md) handles management-event evidence; this task adds request-level coverage and safe log handling.

Recommended baseline: collect the approved metadata needed for accountability and monitoring; keep prompt/response, retrieved material and tool-content capture off unless separately justified and approved. Check actual settings in every SDK and exporter rather than assuming one content flag covers all services. Missing or newly enabled logs cannot reconstruct unrecorded history.

## Read-only checks

Build this matrix from existing, authorized evidence:

| Layer | Inspect | Boundary |
|---|---|---|
| Management audit | Role, key, deployment, network and logging changes; actor, target, UTC time and result where available | Activity Log is not an inference ledger |
| Request/trace metadata | Application alias, authenticated principal where available, deployment/model/version, request/trace ID, UTC time, status, latency and token counts | Verify actual schema/source; shared keys and aggregate charts do not identify a person by themselves |
| LLM content | Whether prompts, responses, retrieved data, tool arguments/results or attachments are captured anywhere | Default recommendation is off; collection needs an approved purpose, fields, redaction, audience, destination and retention |
| Access to logs | Readers, export paths, configuration/retention privileges and existing query auditing | Query text and audit records may themselves be sensitive; query auditing does not cover every downstream export |

Inspect diagnostic settings and application/gateway instrumentation independently. Record selected categories, collection start, ingestion state, correlation fields, sampling, region/destination, retention and blind spots. Sampled traces are not a complete security audit trail.

Inspect the actual workspace/resource/table access model and who can change collection, retention or data. Do not call a log store immutable or tamper-proof merely because collection is enabled. Do not turn on full content or a paid export as an automatic investigation step.

## Interpretation and decisions

| Observation | Supported conclusion |
|---|---|
| No relevant Activity Log entry exists | No control-plane correlation found; inference use is not excluded |
| Identity, correlation or historical logs are absent | Attribution gap; identify the minimum approved instrumentation rather than inventing caller history |
| Content is collected without a documented purpose/access/retention decision | Escalate the data-collection risk without copying the content |
| Readers or destinations exceed the approved audience | Propose a scoped access/export correction; do not expose evidence to demonstrate the issue |
| Only sampled traces exist | State sampling and coverage limits; do not report a complete request ledger |

## Changes and approval

Agree on a minimal metadata allowlist and correlation IDs. Redact or exclude sensitive content before export; an SDK's sensitive-data flag is implementation-specific, not a universal Foundry setting. Any content capture needs its own limited purpose, audience, retention decision and data-owner approval.

Separately approve destinations, reader versus configuration/retention privileges, query auditing and ingestion/retention cost. Apply resource/workspace/table controls only where supported by the actual configuration. Shortening retention, purging data or changing an export is not a generic incident cleanup step. Use [safe operations](../shared/safe-operations.md), and include logging spend in [cost monitoring](../accounts/costs.md).

## Verification and escalation

Verify that approved metadata is collected and correlatable, prohibited content is excluded, and actual readers, destinations and retention match the decision. Use existing permitted events or separately approved synthetic evidence, not customer messages. Any billable inference or new test event requires separate approval.

A successful setting save is not collection evidence. Keep the approved private evidence timeline, provenance, gaps and unknowns. Route content/access concerns to the data/security owner and unsupported collection behavior to platform support. Never claim a compliance verdict or publish raw evidence.

Use the [private inspection and handoff templates](../../reference/cloud-ops-records.md) for permitted evidence. The [draft source-check packet](../../reference/source-review.md) distinguishes public-source observations from pending human/data-owner decisions.

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](../shared/context-and-tools.md)

**Related tasks:** [Platform changes, audit coverage and retention](../network/audit.md); [Resource, data-plane and billing permissions](../accounts/permissions.md); [Cost visibility, allocation and spending controls](../accounts/costs.md)

**If blocked:** [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

References are carried forward from the original draft and existing platform guides. Candidate technical sources were consulted on 2026-10-21; human source/applicability review remains pending. No tenant operation was performed.

### Azure website

- Monitor collection and investigation capabilities: https://azure.microsoft.com/en-us/products/monitor/
- Log ingestion and retention pricing context: https://azure.microsoft.com/en-us/pricing/details/monitor/

### Technical documentation

- Model metrics and diagnostic settings: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/monitor-models
- Control-plane versus data-plane logs: https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/activity-log
- Workspace/resource/table access: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/manage-access
- Query auditing and sensitive query text: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/query-audit
- Table retention: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-retention-configure
- SDK-specific metadata/content example, not a platform-wide default: https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.ai.opentelemetrychatclient.enablesensitivedata

## Scenario coverage

S14-Q2
