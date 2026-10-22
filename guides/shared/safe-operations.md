# Preview, approve, execute, and recover platform changes

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Task guide

| Task card | |
|---|---|
| Use this for | Preview changes to existing resources; Recover a partial operation without deleting unrelated resources |
| Reader | Platform operators and change approvers |
| Applies to | Azure resource changes; ARM/Bicep preview and operation records |
| Prepare | Exact resource scope and desired delta; Cost, ownership and recovery constraints |
| You will get | A scoped change/approval plan and an evidence-based recovery or verification handoff. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference or authorized read-only until explicit approval is obtained for a separate change. No secrets or customer exports in Git.
This is cloud-resource change safety, not application request idempotency. Require exact scope, ownership, intended configuration, and recovery constraints.

## Official policy and live state

ARM/Bicep what-if predicts changes; it is not a completeness guarantee. Unresolved or ignored changes require review. Preview permission requirements can differ from ordinary Reader access; use the current documented validation mode, never automatic privilege escalation.

## Read-only checks

Inventory the approved scope, including IDs, owners, existing deployment records, locks, dependencies, and retention obligations. Do not export arbitrary resource properties that could contain secrets.

```text
az resource list --subscription "<subscription-id>" --resource-group "<resource-group>" --query "[].{id:id,type:type,location:location}"
```

If the customer supplied an IaC plan, use its native preview after confirming permissions:

```text
az deployment group what-if --subscription "<subscription-id>" --resource-group "<resource-group>" --template-file "<reviewed-template-file>"
```

Do not create a template merely to force existing resources into a different tool. Record uncertain preview entries, identities/permissions affected, and expected ongoing costs.

## Interpretation and decisions

Compare desired state with exact existing IDs. Reuse or deliberately modify matching resources; do not generate fresh names on every retry. A timeout can leave an operation running: inspect its status before resubmission.

## Changes and approval

Obtain approval for the resource list and deltas, cost exposure, irreversible actions, and recovery plan. Keep a private operation journal with before-state, approved plan identity, operation IDs, and newly created IDs. Never treat a previously approved plan as permission for a changed plan.

## Verification and escalation

Inspect actual after-state. Following partial failure, classify each resource as pre-existing, created by this operation, modified, or uncertain. Resume only a known-safe pending step. Cleanup requires an exact approved ID list and dependency/retention checks; never delete an entire shared resource group. Report unresolved remnants and ongoing charges. Do not promise automatic rollback of identity, billing, or data changes.

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](context-and-tools.md)

**Related tasks:** [Resource, data-plane and billing permissions](../accounts/permissions.md); [Platform changes, audit coverage and retention](../network/audit.md)

**If blocked:** [Resource, data-plane and billing permissions](../accounts/permissions.md); [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

### Azure website

- Declarative resource deployment overview: https://azure.microsoft.com/en-us/products/arm-templates/
- Resource lifecycle and access-control context: https://azure.microsoft.com/en-us/get-started/azure-portal/resource-manager/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types

## Scenario coverage

S04-Q6, S08-Q6
