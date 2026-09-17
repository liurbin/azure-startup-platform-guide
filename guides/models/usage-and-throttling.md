# Reconcile model usage, cost, and throttling

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

## Scope and prerequisites

Mode: reference or authorized read-only. No prompts, completions, keys or raw customer logs in Git. Metric/export changes, extra capacity and billable tests require approval.
Identify the deployment, model/version/type, subscription, UTC incident interval, cost period and affected endpoint.

## Official policy and live state

Model metrics, rated charges and credit balance are different measurements. Rate-limit estimation and short-window enforcement can differ from billed-token metrics. Quota pressure, effective temporary limits and provisioned utilization need different evidence.

## Read-only checks

1. Open the selected deployment's Metrics view, or Azure Monitor scoped to that resource. Inspect request/status counts, usage and the metrics appropriate to its deployment type. Record aggregation and time granularity.
2. Open its Cost Management view. Select the authorized billing scope and period, group by resource/meter and deployment dimensions where available. Record data freshness; do not claim real-time billing.
3. From an already authorized diagnostic sample, retain only error code/message, timestamp, deployment alias and request ID. Record supplied `x-ratelimit-limit-*`, `x-ratelimit-remaining-*`, and retry/reset headers; missing headers remain unknown.
4. Compare effective limits with configured allocation. For provisioned capacity, inspect the service's utilization metric. Check relevant Service Health events before asserting a customer configuration defect.

## Interpretation and decisions

| Observation | Platform decision |
|---|---|
| Effective limit reached at configured allocation | Review allocation and the applicable quota request path |
| Low aggregate usage but bursts or request-time estimation | Explain the platform measurement mismatch; hand application pacing changes to its owner |
| Effective limits below configuration or persistent unexplained failures | Preserve evidence and escalate possible platform capacity/temporary enforcement |
| Idle model with charges | Inspect deployment billing type and separate compute, storage, tools and logging meters |
| Cost view empty | Check authorization, scope, filters and posting delay before claiming zero cost |

## Changes and approval

Honor returned retry guidance for an authorized request; no infinite retries or quota evasion across accounts. Do not purchase PTUs, change allocation or send test load without explicit approval. This guide diagnoses the platform; it does not redesign application retries.

## Verification and escalation

Compare before/after configured and effective limits in the same scope. For sustained production incidents, supply sanitized error/header samples, aggregation window, allocation and utilization evidence. Never close the issue solely because a dashboard's average is low.

## Sources

### Azure website

- Azure OpenAI pricing basis; not the current customer's bill: https://azure.microsoft.com/en-us/pricing/details/azure-openai/
- Foundry component pricing and purchasing context: https://azure.microsoft.com/en-us/pricing/details/microsoft-foundry/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/quota
- https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/monitor-models
- https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs

## Scenario coverage

S03-Q5, S06-Q3, S06-Q4, S10-Q3
