# Manage automation identities and ownership handoffs

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Task guide

| Task card | |
|---|---|
| Use this for | Check GitHub-to-Azure federation or credential lifecycle; Plan a departing person's access and ownership handoff |
| Reader | Identity/platform administrators and ownership approvers |
| Applies to | GitHub Actions OIDC and Azure authorization; Azure identity, billing ownership and directory transfer boundaries |
| Prepare | Automation or ownership-handoff task; Principal/workflow, current scope and intended owner |
| You will get | A scoped identity/access inventory and an approved-owner transition checklist. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference or authorized read-only. No credentials, invoices, identity exports or customer secrets in Git. Federation, rotation, revocation and ownership changes need separate approval.
Identify whether the task concerns automation login, a departing person's access, billing ownership, resource management ownership, or tenant association.

## Official policy and live state

GitHub Actions can federate its workflow identity to Azure through OIDC. Trust constraints and Azure authorization must both be configured; token permission in GitHub alone does not grant Azure resource access.
Changing a subscription's directory is not a simple billing-owner edit. It can invalidate access and requires a service-specific dependency plan. Inspect current transfer policies; do not assume historical defaults.

## Read-only checks

For automation, inspect the approved repository/workflow/environment, federated credential issuer/subject/audience, Azure principal and resource-role scope. Examine credential metadata and expiry only, never credential values. Confirm the actual automation identity rather than testing as an administrator.

For a handoff, inventory the current and intended principals, billing agreement, tenant association, managed identities, role assignments and credential-based access paths. Determine whether the required change can stay within the current directory. Read applicable transfer support and restrictions before proposing a move.

## Interpretation and decisions

Separate federation trust failure from Azure RBAC failure. Do not widen workflow trust to all repositories or branches.
Separate removing a person from transferring a subscription. Removing a role does not establish that every key-based or external access path has been revoked.

## Changes and approval

Use the official OIDC setup with a narrow repository/environment subject and explicit deployment scope. A permitted new credential is verified before retiring the old one, unless incident response requires immediate revocation.
Ownership/tenant transfers need the billing and directory owners, an access-recreation plan, and a customer-approved maintenance/recovery process. Do not execute transfers from this reference guide.

## Verification and escalation

Check the intended workflow's least-privilege access and the revoked principal's access through approved tests. For handoffs, verify both billing and resource ownership and dependent service identities. Missing transfer support or unclear effects are blockers for billing/directory support.

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](../shared/context-and-tools.md)

**Related tasks:** [Resource, data-plane and billing permissions](permissions.md); [Foundry model access security and credential containment](../models/access-security.md)

**If blocked:** [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

### Azure website

- Resource management and access ownership context: https://azure.microsoft.com/en-us/get-started/azure-portal/resource-manager/
- Credential lifecycle context when an existing solution uses stored secrets; not an OIDC prerequisite: https://azure.microsoft.com/en-us/products/key-vault/

### Technical documentation

- https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-azure
- https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy
- https://learn.microsoft.com/en-us/entra/fundamentals/how-subscriptions-associated-directory
- https://learn.microsoft.com/en-us/azure/role-based-access-control/transfer-subscription

## Scenario coverage

S04-Q5, S09-Q3, S09-Q4
