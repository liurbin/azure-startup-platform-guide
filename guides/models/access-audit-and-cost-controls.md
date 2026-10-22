# Choose a Foundry access, audit, or cost-control task

Policy checked: [set on review]. Status: draft; sources not re-verified; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Scenario overview (reference/routing only)

| Task card | |
|---|---|
| Use this for | Choose a route for model access, audit/logging or cost monitoring; Triage an unexplained model-cost increase without assuming key theft |
| Reader | Founders and platform, security/data and FinOps owners |
| Applies to | Foundry model platform controls; Routing to endpoint-specific task guides |
| Prepare | Question and intended outcome; Known service/endpoint and desired reference or inspection mode |
| You will get | A reading path, selected task owners and missing inputs; this overview does not authorize execution. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference only. Do not execute read-only checks or changes from this overview. It selects reading paths, not operations; each selected task has its own maturity, scope and approval requirements.

Start with the question and known cloud/service context. For a live task, its responsible owner confirms the exact endpoint, permitted scope and needed evidence. Reference-only readers may leave account-specific values unknown. Never request secrets or customer prompts to choose a guide.

This is the scenario overview for the three control areas below. Detailed instructions belong to the linked task guides, not a second copy here.

## Official policy and live state

Separate **who can access models**, **what is recorded and who can access those records**, and **how usage and money are monitored**. One successful check does not establish all three.

An unexpected charge does not establish key theft. Management events do not describe every inference request, and a budget alert is not proof of a consumption stop. Use the appropriate evidence route rather than treating these as one problem.

## Read-only checks

These are reading choices, not instructions to query an account.

| Your question | Start with | Expected handoff |
|---|---|---|
| Who can invoke models, and how should identities, keys and network access be controlled? | [Model access security (draft)](access-security.md) | Access-path inventory, control gaps and an approval/verification plan |
| What should be audited, including LLM logs, and who may see or retain it? | [Request auditing and safe LLM logs (draft)](audit-and-llm-logs.md) | Coverage/privacy matrix and a scoped logging decision |
| How should spending, allocation, budgets and alert ownership be monitored? | [Cost monitoring (draft)](../accounts/costs.md) | Scoped cost/credit reconciliation and an owned control proposal |
| Do model metrics explain a spike or throttling? | [Usage, cost and throttling](usage-and-throttling.md) | Aligned usage/cost evidence, uncertainty and escalation |
| Where are the actual remaining credits and expiry? | [Credits](../accounts/credits.md) | Offer-specific balance and validity observations, if authorized |

For an unexplained fee increase, first route to usage and cost reconciliation. If credible exposure or unexplained access evidence emerges, add the access-security and logging routes. Do not require a customer to complete every branch to answer a narrow question.

## Interpretation and decisions

| Observation | Supported finding and next step |
|---|---|
| Multiple control areas need attention | Assign a platform/identity owner, security/data owner and FinOps owner; select only their relevant tasks |
| Service, endpoint or authorization is unclear | Start with context and permissions; leave customer-specific state unknown |
| A selected task is draft | Reference/review only; do not execute it |
| Evidence supports suspected compromise | Hand off to the authorized incident owner without waiting for a final invoice |

## Changes and approval

This overview authorizes no operation. Any selected task requires its own maturity check, current applicable sources and exact customer approval. Use [safe operations](../shared/safe-operations.md) for a separately approved change; never infer permission to rotate keys, capture content, export logs or disable resources from this reading path.

## Verification and escalation

The output of this overview is a selected reading path, responsible owners and missing inputs, not verified account findings. Return `reference_only`. A later authorized task reports its own evidence, limits and result status using the [result contract](../../reference/result-contract.md).

Keep access containment, safe logging and financial reconciliation as separate completion checks. A successful action in one area does not close the other two.

Founders can use the [short handoff card](../../start/founder.md); administrators can use [private inspection and acceptance records](../../reference/cloud-ops-records.md). The [source-check packet](../../reference/source-review.md) documents preliminary observations, not execution authority or human approval.

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](../shared/context-and-tools.md)

**Related tasks:** [Foundry model access security and credential containment](access-security.md); [Foundry request auditing and safe LLM logs](audit-and-llm-logs.md); [Cost visibility, allocation and spending controls](../accounts/costs.md)

**If blocked:** [Resource, data-plane and billing permissions](../accounts/permissions.md); [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

Candidate sources were consulted on 2026-10-21 to prepare this draft. Human review of the claims and service-specific applicability remains pending; this is not a source-reviewed or tenant-tested procedure.

### Azure website

- Secret-storage capabilities, not revocation of an already copied key: https://azure.microsoft.com/en-us/products/key-vault/
- Cost visibility and budget capabilities, not an automatic hard cap: https://azure.microsoft.com/en-us/products/cost-management/

### Technical documentation

- Access-control entry point; use the selected task for scope-specific interpretation: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/configure-entra-id
- Model monitoring and cost visibility: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/monitor-models
- Budgets are notifications, not an automatic consumption stop: https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets

## Scenario coverage

S14-Q1, S14-Q2, S14-Q3
