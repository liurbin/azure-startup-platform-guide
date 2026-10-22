# Check platform, data-plane, and billing permissions separately

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Task guide

| Task card | |
|---|---|
| Use this for | Separate model invocation, deployment and billing access; Identify the narrow missing permission without defaulting to Owner |
| Reader | Platform administrators and authorized resource or finance users |
| Applies to | Azure resource and data-plane roles; Microsoft Entra and billing-role boundaries |
| Prepare | Intended principal and operation; Exact resource or billing scope and sanitized failure |
| You will get | An operation-to-scope permission matrix and a least-privilege administrator request. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference or authorized read-only. No directory exports, keys or customer identities in Git. Role changes require approval.
Identify the principal and requested operation, then its exact resource or billing scope. Do not enumerate unrelated users or tenants.

## Official policy and live state

Azure resource roles, Microsoft Entra directory roles and billing roles solve different access problems. Creating a deployment and invoking an existing model are different actions. A resource Reader role must not be assumed to expose every agreement's billing data.

## Read-only checks

1. Open the exact resource or subscription > Access control (IAM) > Check access. Inspect the selected principal's direct and inherited assignments, scope, conditions and applicable deny assignments.
2. Check whether an eligible role needs activation through the organization's approved process. Record that as a pending action, not active access.
3. For model access, identify the resource generation, target model operation and current service role definitions. Compare management-plane creation with data-plane invocation.
4. For finance-only access, inspect the agreement-specific billing account/profile or Cost Management scope. Request the narrow read capability needed, not resource creation rights.

## Interpretation and decisions

Build a small operation matrix: view cost, read configuration, create project/deployment, invoke model, assign access. For each, record the governing scope, observed role and missing action. Distinguish authentication failure, insufficient authorization, policy denial and network refusal.

## Changes and approval

Give the responsible administrator the exact principal, scope, action and proposed least-privilege role after checking the current role definition. Do not make Owner or Global Administrator the default fix. Do not assign yourself permission merely because a guide asks for a check.

## Verification and escalation

Recheck effective access as the intended principal, including any activation/propagation state. Validate the requested operation without creating a resource or sending a billable model request unless separately authorized. A recorded role assignment alone is not conclusive proof of usable access.

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](../shared/context-and-tools.md)

**Related tasks:** [Federation, credential lifecycle and ownership](identity-lifecycle.md); [Foundry model access security and credential containment](../models/access-security.md)

**If blocked:** [Private endpoints, DNS, access and policy denials](../network/connectivity-and-policy.md); [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

### Azure website

- Resource roles, organization and access-control overview: https://azure.microsoft.com/en-us/get-started/azure-portal/resource-manager/
- Billing and cost-management capability context: https://azure.microsoft.com/en-us/products/cost-management/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access
- https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/assign-access-acm-data
- https://learn.microsoft.com/en-us/entra/fundamentals/how-subscriptions-associated-directory

## Scenario coverage

S01-Q6, S08-Q5, S09-Q1, S13-Q1
