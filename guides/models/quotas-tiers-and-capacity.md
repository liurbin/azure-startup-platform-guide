# Inspect the current tier, quota allocation, and capacity

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

## Scope and prerequisites

Mode: reference or authorized read-only. No tokens or customer exports in Git. Quota allocation, upgrade-policy changes and applications require approval.
This guide's API example is for global Azure OpenAI/Foundry, not all model providers or clouds. Confirm subscription, model/version, deployment type, resource and region/data zone.

## Official policy and live state

Treat tier, approved limit, allocation, available capacity and actual traffic as separate facts. Current policy describes shared subscription pools with model/deployment-specific rollout; do not assume every region supplies another independent allowance. Additional quota approval need not change the tier.

## Read-only checks

The currently documented tier GET uses a **preview** API. Recheck its version and applicability before use:

```text
az rest --method get --subscription "<subscription-id>" --url "https://management.azure.com/subscriptions/<subscription-id>/providers/Microsoft.CognitiveServices/quotaTiers?api-version=2025-10-01-preview" --query "value[].properties.{tier:currentTierName,assigned:assignmentDate,upgrade:tierUpgradePolicy}"
```

Authorization remains inside the customer's CLI; never extract a bearer token into a report. If this API is unavailable or unauthorized, record the error and leave the tier unknown.

Open the applicable quota view for the selected subscription/model. Record quota dimension and pool scope, unit, approved limit, allocated amount, remaining allocation and observation time. Follow the current official Usages and Model Capacities references to inspect the specific requested deployment; record the response's meaning rather than relabeling allocation as billed traffic.

## Interpretation and decisions

Compare live state with the policy table for that exact model/version/type, not a generic model family. An empty capacity response is not a promise of future availability. If an approval increased quota but the tier is unchanged, compare the actual approved dimension and allocation before reporting failure.

## Changes and approval

Prepare the official quota application with requested model, scope, amount/unit, workload justification, current usage and date needed. Do not inflate consumption to force an upgrade. Reallocation can reduce another deployment's entitlement: show that impact first. Never silently change the automatic-upgrade policy.

## Verification and escalation

After approval, reread the corresponding limit and deployment allocation. Check effective service behavior only with authorization. Report policy source/date, preview API, returned tier fields, pool scope, remaining unknowns and the exact support/application status.

## Sources

### Azure website

- Azure OpenAI model service and deployment overview; not the customer's live quota: https://azure.microsoft.com/en-us/products/ai-foundry/models/openai
- Product-level regional availability; not a capacity guarantee: https://azure.microsoft.com/en-us/explore/global-infrastructure/products-by-region/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/foundry/openai/quotas-limits
- https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/quota

## Scenario coverage

S03-Q6, S06-Q1, S06-Q3, S10-Q1
