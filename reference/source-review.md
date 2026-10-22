# Draft source-check packet

Checked on **2026-10-22 (Asia/Shanghai)**. This is an **AI-assisted preliminary source check**, not human approval, an exhaustive review of every assertion, a legal opinion or tenant execution evidence. Relevant public sections were read; no customer agreement, restricted report, account or live API response was inspected.

All six guides below remain `draft`; all 12 existing `REVIEW` comments remain in their original guides. No policy-check date, catalog maturity or tenant-test claim was promoted. Publication/merge, source review, customer authorization and execution evidence are separate.

## Individual guide checks

| Guide | Public-source observation | Still required before promotion |
|---|---|---|
| [Contract/compliance routes](../guides/accounts/compliance-terms.md) | S9 describes an in-scope Azure BAA route through Product Terms. S10 exposes DPA versions/languages, not which version governs a customer | Contract owner checks agreement/channel, exact service scope, applicable document/version, signature/access/sharing conditions and the startup's own obligations; R1-R4 remain open |
| [Costs](../guides/accounts/costs.md) | S7 explicitly separates budget notifications from stopping resources. S4 describes post-consumption cost visibility; S12 lists hierarchy, tags and allocation rules as distinct tools | Review every new assertion and agreement-specific presentation, attribution, expiry/continuation and alert behavior; R5-R8 remain open |
| [Quota](../guides/models/quotas-tiers-and-capacity.md) | S8 describes model/deployment-specific subscription-pool rollout, Global Standard/shared-region and Data Zone pools, tier eligibility and the preview tier API. It says approved extra quota need not change tier | Match exact model/version/type and rollout, quota units and approval. The retained GET example was compared with the public API route, not executed; R9-R12 remain open |
| [Foundry overview](../guides/models/access-audit-and-cost-controls.md) | S1, S4 and S7 support keeping access, observable usage and financial controls separate | Human review of routing/boundaries and the selected tasks. Overview remains reference/routing only regardless of maturity |
| [Model access security](../guides/models/access-security.md) | S1 separates inference authorization from role administration. S2 explains immediate invalidation and staged two-key rotation. S3 distinguishes network settings and connectivity | Confirm applicability to the actual endpoint/client, resource/gateway/provider credential, legitimate consumers, propagation and recovery limits; no generic rotation or network approval is implied |
| [LLM logs](../guides/models/audit-and-llm-logs.md) | S4 separates metrics and configured diagnostics; S5 describes workspace/resource/table access models; S6 distinguishes metadata/content in one SDK; S11 distinguishes control-plane events from data-plane logs | Inspect actual SDK/exporters/schema, sampling, collection start, identity attribution, readers/exports/retention and data-owner decisions. S6 is not a platform-wide default |

S4 describes an approximately five-hour cost-display example; S7 describes different typical cost/budget evaluation timing. These concern different surfaces and are not a universal freshness guarantee. Keep actual scope/time/freshness in observations instead of freezing one delay for every offer.

## Pending human decisions

The IDs below identify existing comments for review; they do not replace or resolve those comments.

| ID | Decision to record privately | Current disposition |
|---|---|---|
| R1 | Applicable BAA/terms, channel, in-scope service and any signature process | S9 supports a general Product Terms route, not a conclusion about an unseen agreement |
| R2 | Whether the requester needs provider evidence or the startup's own DPA | Not determined by locating Microsoft's DPA landing page |
| R3 | Handling of an unlisted-service gap and actual regulatory obligations | Owner signoff alone is not evidence of legal permission; qualified review pending |
| R4 | Access and redistribution terms for the actual Service Trust Portal artifact | Restricted artifact/access terms were not inspected |
| R5 | Actual cost/invoice/Marketplace treatment for the relevant agreement and offer | No customer bill or agreement inspected; no universal credit-offset model established |
| R6 | Supported allocation and reporting alternatives for untagged/shared spend | S12 lists multiple tools; applicability and residual attribution require review |
| R7 | Supported cause of a cost change and meaning of absent Activity Log events | S11 is control-plane evidence, not proof about request usage, prices or metering correctness |
| R8 | Offer-specific credit exhaustion, expiry and continued charging arrangements | Not established; do not assume automatic continuation, shutdown or refund |
| R9 | Exact quota pool scope for the model/version/deployment type and rollout | S8 contradicts a universal independent-per-region assumption; exact applicability remains open |
| R10 | Actual entitlement for the subscription/offer, rather than a guessed normal limit | S8 describes several eligibility factors; no live entitlement was read |
| R11 | Unallocated allowance versus runtime headroom and cross-region alternatives | Exact dimensions and live evidence are missing; no automatic traffic diagnosis |
| R12 | Cause of persistent 429s despite an apparently available quota | Requires scoped errors, effective limits and utilization; not classified as a service fault here |

## Promotion and execution gates

For each guide, the human reviewer records the actual applicable sources/version/date, checks all changed assertions (not only the 12 conflicts), resolves its comments, and records remaining limitations. Only then update its header and catalog status together. Do not silently turn this packet's check date into a policy-check date.

| Required record | Default |
|---|---|
| Guide and responsible human reviewer role | Pending |
| Applicable cloud, service generation, endpoint/model/type and agreement scope | Unknown until established |
| Source versions/sections and claim-by-claim decision | Pending human review |
| REVIEW dispositions, unresolved scope and approval reference | Pending; keep private correspondence out of Git |
| Scoped tenant procedure, date, redacted evidence and limitations | Not performed |

After source review, any controlled tenant exercise needs its own exact-scope permission, approved targets and cost/data limits. Use the [Cloud Ops records](cloud-ops-records.md). A `tenant-tested` label requires the scoped sanitized evidence defined in [AGENTS](../AGENTS.md#guide-maturity), not a successful command or this source packet.

## Sources

These links identify the public sections inspected, not wholesale incorporation of their content or confirmation of a customer's eligibility.

- **S1:** [Foundry Models keyless authentication](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/configure-entra-id) - inference roles versus role-assignment administration.
- **S2:** [Foundry Tools key rotation](https://learn.microsoft.com/en-us/azure/ai-services/rotate-keys) - old-value invalidation and the staged two-key procedure; verify resource applicability.
- **S3:** [Foundry private connectivity](https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link) - inbound/outbound scope, public-access settings and client/network prerequisites.
- **S4:** [Foundry model monitoring](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/monitor-models) - supported resource context, metrics, access and post-consumption costs.
- **S5:** [Log Analytics access](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/manage-access) - access modes and workspace/resource/table boundaries.
- **S6:** [OpenTelemetryChatClient.EnableSensitiveData](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.ai.opentelemetrychatclient.enablesensitivedata?view=net-11.0-pp) - the returned .NET prerelease API view describes one SDK's content controls, not every Foundry component.
- **S7:** [Cost Management budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets) - notification, consumption-stop and evaluation-delay distinctions.
- **S8:** [Azure OpenAI quotas and limits](https://learn.microsoft.com/en-us/azure/foundry/openai/quotas-limits) - subscription pools, rollout, tiers and preview tier lookup.
- **S9:** [Azure HIPAA/HITECH offering](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us) - general BAA route and in-scope-service caveat; not a legal opinion.
- **S10:** [DPA version landing page](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) - version/language discovery only; no agreement-specific DPA text was reviewed.
- **S11:** [Activity Log](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/activity-log) - control-plane management events versus configured resource logs.
- **S12:** [Cost allocation introduction](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-allocation-introduction) - hierarchy, billing, tags and rules as distinct allocation tools.
