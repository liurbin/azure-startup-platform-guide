# Inspect storage access, request limits, and transfer costs

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Task guide

| Task card | |
|---|---|
| Use this for | Inspect Blob access or storage throttling; Attribute storage and transfer charges to actual meters |
| Reader | Storage/platform operators and authorized cost investigators |
| Applies to | Azure Blob Storage; Account/network/data-plane permission and meter boundaries |
| Prepare | Account type, region, redundancy/tier and access path; Sanitized error or aligned metric/cost interval |
| You will get | A scoped access/limit or meter-cost finding without inspecting object contents. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference or authorized read-only. No object contents, keys, SAS URLs or customer exports in Git. Authorization, networking, lifecycle and diagnostic changes require approval.
Concrete service: Blob Storage. Identify account type, region, redundancy, access tier, namespace mode and the requested access path.

## Official policy and live state

Account management access, blob data authorization and network access are separate. Service targets depend on the actual account/workload dimensions; a generic request-count number is not a universal limit. Costs can include capacity, operations, retrieval, replication and transfer.

## Read-only checks

1. Open the storage account's configuration, Networking and IAM surfaces. Inspect public access settings, private endpoints, identity-based role scope and the authorization method used by the approved client.
2. Inspect the appropriate service Metrics for response types, request volume, throttling and transfer over the incident interval. Do not browse blobs as an access diagnostic.
3. Follow the current account scalability and Blob limits pages for the exact dimension: account, service, partition or object. Capture units and applicability.
4. In Cost analysis, group the selected account by meter and time. Identify the source/destination boundary relevant to transfer charges; do not assume an app and its storage share a billing boundary because they belong to one team.

## Interpretation and decisions

Differentiate an expired credential, missing data permission, networking refusal, platform limit and capacity issue from the actual error. Do not disclose or regenerate account keys to answer an IAM question. Separate storage price-list possibilities from charges observed on this account.

## Changes and approval

Propose the narrow role/network/lifecycle or capacity change needed. Public access, tier changes, replication and logging can affect exposure, access behavior and charges; obtain approval for their exact scope.

## Verification and escalation

Recheck effective configuration and the relevant metrics. Reading or writing a test blob needs explicit data-plane authorization and a non-sensitive test object. Escalate unresolved throttling with request IDs, response codes, account type and aggregation interval.

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](../shared/context-and-tools.md)

**Related tasks:** [Private endpoints, DNS, access and policy denials](../network/connectivity-and-policy.md); [PostgreSQL and Blob Storage: backups and retained data](backup-and-retention.md); [Cost visibility, allocation and spending controls](../accounts/costs.md)

**If blocked:** [Resource, data-plane and billing permissions](../accounts/permissions.md); [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

### Azure website

- Blob Storage capabilities and account context: https://azure.microsoft.com/en-us/products/storage/blobs/
- Capacity, operations, retrieval and transfer pricing context: https://azure.microsoft.com/en-us/pricing/details/storage/blobs/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security
- https://learn.microsoft.com/en-us/azure/storage/common/scalability-targets-standard-account
- https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-access-azure-active-directory

## Scenario coverage

S02-Q3
