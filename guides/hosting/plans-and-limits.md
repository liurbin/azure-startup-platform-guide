# Inspect hosting plans, platform limits, and idle cost

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Task guide

| Task card | |
|---|---|
| Use this for | Inspect hosting replicas, plan constraints or idle charges; Separate an app setting from environment quota and capacity |
| Reader | Container Apps operators and authorized cost owners |
| Applies to | Azure Container Apps only; Other hosts require their own service documentation |
| Prepare | Selected app/environment, region and workload profile; Requested limit or aligned billing/metric interval |
| You will get | A plan/settings/observed-state comparison with attributable costs and supported next steps. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference or authorized read-only. No configuration secrets or customer exports in Git. Plan, scaling, diagnostic and resource changes need approval.
The concrete example is Azure Container Apps. For App Service, Functions, AKS or another host, identify it first and load its own current limits/billing documentation. Do not copy Container Apps semantics across services.

## Official policy and live state

Container Apps has distinct consumption/dedicated billing arrangements and platform quotas. Environment/workload-profile capacity and an application's replica settings are different constraints. No requests does not establish that all hosting charges stop.

## Read-only checks

1. Open the selected app and its environment. Inspect region, environment type, workload profile, CPU/memory configuration, active revisions and actual replicas.
2. Inspect minimum/maximum replica settings and the current quota/limit view for the relevant scope. Record units and whether each value is a service limit, customer setting or observed utilization.
3. Open Cost analysis for the app, environment and attached resources. Separate idle allocations, dedicated profile capacity, requests, logs, registry, networking and other billed resources actually present.
4. Read current platform documentation for the chosen profile and region before presenting an expansion option. Do not assume that a configured maximum can be allocated.

## Interpretation and decisions

Distinguish an app setting from an environment/subscription quota or physical capacity constraint. Unexpected idle cost needs meter evidence, not a guess that scale-to-zero failed. Unsupported hosts are routed to their own service guide, not marked healthy.

## Changes and approval

Present proposed minimum/maximum replicas, profile/plan changes, effects on availability and cost, and who can approve them. Do not rewrite application concurrency logic or choose a new hosting architecture for the customer.

## Verification and escalation

Confirm saved settings, actual platform state and the applicable quota after a change. Inspect costs for a later aligned period; do not claim immediate invoice reconciliation. Escalate unexplained allocation failures with environment/profile/replica evidence.

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](../shared/context-and-tools.md)

**Related tasks:** [Container Apps: deployment access and domains](deployment-and-domains.md); [Cost visibility, allocation and spending controls](../accounts/costs.md)

**If blocked:** [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

### Azure website

- Container Apps plan and platform capability overview: https://azure.microsoft.com/en-us/products/container-apps/
- Hosting-plan, resource and request pricing: https://azure.microsoft.com/en-us/pricing/details/container-apps/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/container-apps/quotas
- https://learn.microsoft.com/en-us/azure/container-apps/billing

## Scenario coverage

S06-Q5, S08-Q3
