# Inspect the current tier, quota allocation, and capacity

Policy checked: [set on review]. Status: draft; sources not re-verified; not tenant-tested.

Previous source-reviewed baseline: 2026-09-17. Existing policy text and the tier-query example are retained; additions and conflicts require human source review.

## Scope and prerequisites

Mode: reference only while draft. Do not execute the read-only checks or changes below until source review and explicit customer authorization. No tokens or customer exports in Git. Quota allocation, upgrade-policy changes and applications require approval.
This guide's API example is for global Azure OpenAI/Foundry, not all model providers or clouds. Confirm subscription, model/version, deployment type, resource and region/data zone.

Start with the customer's exact question: current tier, what can be allocated, deployment failure, or runtime throttling. Obtain the resource generation, target endpoint/deployment alias, error code/message and UTC interval where relevant. Do not request prompts or credentials.

## Official policy and live state

Treat tier, approved limit, allocation, available capacity and actual traffic as separate facts. Current policy describes shared subscription pools with model/deployment-specific rollout; do not assume every region supplies another independent allowance. Additional quota approval need not change the tier.

<!-- REVIEW: The draft describes all pay-as-you-go quota as a per-model, per-region, per-subscription pool. The existing scope/rollout statement is retained; a human must check the exact model/version and deployment type before adopting a universal regional rule. -->

<!-- REVIEW: The draft treats very low limits on sponsored/new subscriptions as expected rather than a fault. Retain live tier and quota inspection; offer type or low spend must not substitute for the customer's observed entitlement and applicable policy. -->

## Read-only checks

1. Confirm the cloud/subscription and the exact model/version/type. A resource's displayed region alone is not a complete quota-pool key. If context or authority is missing, stop with a scoped checklist instead of querying another subscription.

2. Read the current tier separately from a deployment's allocation. The baseline tier GET uses a **preview** API. Recheck its version and applicability before use:

```text
az rest --method get --subscription "<subscription-id>" --url "https://management.azure.com/subscriptions/<subscription-id>/providers/Microsoft.CognitiveServices/quotaTiers?api-version=2025-10-01-preview" --query "value[].properties.{tier:currentTierName,assigned:assignmentDate,upgrade:tierUpgradePolicy}"
```

Authorization remains inside the customer's CLI; never extract a bearer token into a report. If this API is unavailable or unauthorized, record the error and leave the tier unknown.

3. Open the applicable quota view for the selected subscription/model. Record quota dimension and pool scope, unit, approved limit, allocated amount, remaining allocation and observation time. Follow the current official Usages and Model Capacities references to inspect the specific requested deployment; record the response's meaning rather than relabeling allocation as billed traffic.

Capture the following fields separately; use `unknown` for absent or inaccessible fields, not zero:

| Question | Evidence surface | Fields to retain privately |
|---|---|---|
| What is my current tier? | Applicable tier GET or an official equivalent | `currentTierName`, `assignmentDate`, `tierUpgradePolicy`, subscription and time |
| What allowance is approved and how is it allocated? | Quota view / documented Usages operation | Pool scope, model/version/type, units, approved limit, allocated amount and unallocated amount |
| What is this deployment assigned? | Exact deployment's configuration | Resource/deployment identity, model/version, SKU/type, configured capacity and its units, provisioning state |
| Is the requested deployment currently allocatable? | Documented capacity/availability surface for that request | Model/type/location constraints, observed response and time; no guarantee inferred from quota |
| What happened to actual requests? | Existing authorized metrics and sanitized error/header evidence | UTC interval, aggregation, status/error, effective request/token limits where returned, retry guidance and request ID |

4. For an existing failure, distinguish deployment creation/allocation from inference traffic. Compare timestamps and scope before relating a quota number to a 429. Do not send billable traffic just to populate missing metrics.

5. Compare model availability and lifecycle separately. If a proposed region/type change raises contractual or data-location questions, provide the [contract evidence route](../accounts/compliance-terms.md), not a compliance conclusion.

## Interpretation and decisions

Compare live state with the policy table for that exact model/version/type, not a generic model family. An empty capacity response is not a promise of future availability. If an approval increased quota but the tier is unchanged, compare the actual approved dimension and allocation before reporting failure.

| Evidence | What to do next |
|---|---|
| Tier field is unavailable or the API is unauthorized/unsupported | Report tier unknown; identify the exact missing access/API applicability rather than inferring a tier |
| No unallocated allowance remains for a requested allocation | Review current assignments and the matching request path; this alone does not diagnose existing inference traffic |
| Allocation failed with capacity evidence despite adequate allowance | Record placement/capacity conditions and escalate; do not call the allowance a reservation |
| 429 occurs while a summary chart looks low | Use [runtime throttling checks](usage-and-throttling.md) to inspect effective limits, windows and utilization |
| Approval and live settings disagree | Match approval scope, dimension, units and deployment assignment; record pending or contradictory state |

<!-- REVIEW: The draft combines "remaining quota is zero" with a quota-bound traffic diagnosis and suggests another region as a remedy. Unallocated allowance and runtime headroom remain separate here; no independent cross-region pool is assumed. -->

<!-- REVIEW: The draft sends persistent 429s with available quota to support "as a service issue". Preserve that as an unconfirmed hypothesis until scoped error, effective-limit and utilization evidence supports the classification. -->

## Changes and approval

Prepare the official quota application with requested model, scope, amount/unit, workload justification, current usage and date needed. Do not inflate consumption to force an upgrade. Reallocation can reduce another deployment's entitlement: show that impact first. Never silently change the automatic-upgrade policy.

Give the responsible owner a before/requested table, supporting metric interval, application route, cost exposure, processing-location constraints and intended verification. The customer approves and submits any attestation. Record the request ID; submission is not approval.

Do not delete/recreate resources to reset a limit, scatter speculative deployments across regions, or switch deployment type without a separate approved change plan.

## Verification and escalation

After approval, reread the corresponding limit and deployment allocation. Check effective service behavior only with authorization. Report policy source/date, preview API, returned tier fields, pool scope, remaining unknowns and the exact support/application status.

Close the requested check only when its evidence exists: tier questions require a tier observation; allocation requests require the matching updated allocation; a runtime incident requires evidence from an appropriate subsequent interval. Do not substitute one for another.

For support, include sanitized scope, model/version/type, requested units, actual settings, UTC interval, error/request IDs and the approval reference. Keep customer identifiers in the customer's private evidence bundle.

## Sources

Existing sources are retained. Additional draft references below have not been fetched or re-verified in this change.

### Azure website

- Azure OpenAI model service and deployment overview; not the customer's live quota: https://azure.microsoft.com/en-us/products/ai-foundry/models/openai
- Product-level regional availability; not a capacity guarantee: https://azure.microsoft.com/en-us/explore/global-infrastructure/products-by-region/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/foundry/openai/quotas-limits
- https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/quota

### Proposed additional references

- https://learn.microsoft.com/azure/ai-services/openai/quotas-limits
- https://learn.microsoft.com/azure/ai-services/openai/how-to/quota
- https://learn.microsoft.com/azure/ai-services/openai/how-to/deployment-types
- https://learn.microsoft.com/azure/ai-services/openai/concepts/provisioned-throughput
- https://learn.microsoft.com/azure/ai-services/openai/concepts/models
- https://learn.microsoft.com/azure/quotas/quotas-overview

## Scenario coverage

S03-Q6, S06-Q1, S06-Q3, S10-Q1, S13-Q3
