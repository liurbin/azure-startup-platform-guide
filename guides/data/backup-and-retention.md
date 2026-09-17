# Verify backups, recoverable history, and retained data

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

## Scope and prerequisites

Mode: reference or authorized read-only. No customer database/blob contents or secrets in Git. Restore, retention, lifecycle, replication and deletion changes require approval.
Identify exact data service, resource, required recovery point and retention obligation. Concrete examples: PostgreSQL Flexible Server and Blob Storage.

## Official policy and live state

A configured retention value is not evidence that a particular recovery point exists. Database backups, blob soft delete, versioning, point-in-time restore and immutability are different features with distinct prerequisites. Do not treat them as interchangeable backups.

## Read-only checks

For PostgreSQL, inspect server Backup and restore settings, redundancy, displayed earliest/latest restore time and available backup/restore history. Identify the region and destination constraints for the contemplated restore.

For Blob Storage, inspect Data protection, versioning, delete retention, point-in-time restore configuration, lifecycle rules, and any immutability/legal-hold state applicable to the selected scope. Report whether a feature is enabled and when history actually starts, not just what the product supports.

For either, list resources and charges potentially retained after deletion. Read the service's exact deletion/recovery procedure before advising on recovery windows.

## Interpretation and decisions

Classify a requested point as observed recoverable, outside observed history, blocked by permissions/configuration, or unknown. Changes made now do not retroactively create historical backups. Do not infer the absence of retention controls from an empty unauthorized view.

## Changes and approval

Prepare a restore plan with exact point, destination, access controls, costs and data-owner approval. An isolated restore drill is a separate resource/data operation, never an automatic documentation check. Do not remove a hold, shorten retention or delete recoverable copies for generic cost reduction.

## Verification and escalation

Reinspect retained history after approved configuration changes. A completed restore resource does not establish business-data correctness; hand that verification to the data owner. Report inability to recover promptly with service/version, target time and sanitized operation IDs.

## Sources

### Azure website

- PostgreSQL service context for native database backup: https://azure.microsoft.com/en-us/products/postgresql/
- Blob Storage context for data-protection features: https://azure.microsoft.com/en-us/products/storage/blobs/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/postgresql/backup-restore/concepts-backup-restore
- https://learn.microsoft.com/en-us/azure/storage/blobs/data-protection-overview

## Scenario coverage

S05-Q4, S10-Q5
