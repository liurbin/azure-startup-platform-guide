# Inspect database versions, resource limits, and maintenance

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Task guide

| Task card | |
|---|---|
| Use this for | Inspect database version, storage/connection warnings or maintenance; Check platform-supported configuration and upgrade options |
| Reader | Database/platform operators and change approvers |
| Applies to | Azure Database for PostgreSQL Flexible Server only; Other engines require their own lifecycle and limit references |
| Prepare | Exact engine/resource, region, SKU/version and topology; Warning/maintenance interval and intended platform outcome |
| You will get | A version/configuration/limit finding and a supported owner-approved platform plan. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference or authorized read-only. No database rows, credentials or connection strings in Git. Scaling, upgrades, parameters and maintenance changes require approval.
Concrete service: PostgreSQL Flexible Server. First identify engine/resource type, region, SKU, version and replica/HA topology. SQL, MySQL, Cosmos DB and cache services require their own current limits and lifecycle references.

## Official policy and live state

Supported versions, configured resources, platform limits and observed metrics are distinct. Maintenance scheduling does not authorize a major-version upgrade. Do not infer available versions from the local client version.

## Read-only checks

1. In the server Overview/Compute + storage surfaces, record engine version, SKU/vCores, storage allocation, availability configuration and provisioning state.
2. Compare current regional offerings and supported versions against the service documentation. List upgrade targets only after checking the applicable path and restrictions.
3. Inspect platform Metrics over the warning interval: connections, storage and utilization relevant to the actual service. Record aggregation, configured threshold and the service's limit definition.
4. Open Maintenance and relevant Service Health notifications. Record schedule, pending events, customer-configurable settings and the responsible operator.

## Interpretation and decisions

Differentiate approaching storage/connection limits, a monitoring threshold, maintenance, and an actual service outage. An alert is not permission to enlarge a server. If evidence points to query/business behavior, hand the finding to the application/database owner without rewriting SQL.

## Changes and approval

Present supported scale or platform-configuration options, possible downtime, billing effects, backup requirements and rollback constraints. Do not promise in-place downgrades, instantaneous capacity, or an identical upgrade path across database products.

## Verification and escalation

After authorized work, reread engine/SKU/storage/state and observe the relevant metric window. Confirm the warning's actual condition; a dismissed notification is not proof of repair. Escalate inconsistencies with service type, version, SKU and sanitized metric/event evidence.

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](../shared/context-and-tools.md)

**Related tasks:** [PostgreSQL and Blob Storage: backups and retained data](backup-and-retention.md); [Cost visibility, allocation and spending controls](../accounts/costs.md)

**If blocked:** [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

### Azure website

- PostgreSQL service and configuration context: https://azure.microsoft.com/en-us/products/postgresql/
- Flexible Server compute, storage and backup pricing: https://azure.microsoft.com/en-us/pricing/details/postgresql/flexible-server/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/postgresql/configure-maintain/concepts-maintenance
- https://learn.microsoft.com/en-us/azure/postgresql/configure-maintain/concepts-supported-versions
- https://learn.microsoft.com/en-us/azure/postgresql/configure-maintain/concepts-limits
- https://learn.microsoft.com/en-us/azure/postgresql/backup-restore/concepts-backup-restore

## Scenario coverage

S04-Q1, S07-Q5
