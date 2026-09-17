# Find platform changes and establish audit evidence

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

## Scope and prerequisites

Mode: reference or authorized read-only. No raw audit exports, personal identities or secrets in Git. Enabling export or changing retention requires approval.
Obtain the exact resource/scope, operation of interest, UTC interval and authorized evidence recipient.

## Official policy and live state

Azure Activity Log covers control-plane activity; resource/data-plane logs and Entra logs are separate evidence surfaces. Activity Log's standard retention is finite, and longer retention requires an appropriate existing export/destination. Missing capture cannot be repaired retroactively.

## Read-only checks

1. Open Monitor > Activity log, or the resource's Activity log. Filter the approved scope/time and relevant write, role-assignment, policy or network operations. Inspect status, operation/correlation ID and authorized caller information.
2. For a guardrail, follow the exact resource/provider and deployment association. Determine whether the change is represented in the control-plane record or requires a configured service-specific audit surface.
3. Inspect diagnostic settings, selected categories, destination, destination access controls and retention. Check collection start time and ingestion status where available.
4. If a role/directory change concerns Entra rather than Azure RBAC, use its authorized audit surface. Do not infer "who changed it" solely from the current role membership.

## Interpretation and decisions

Distinguish recorded attempt, successful operation, and effective after-state. A timestamped caller entry is evidence within its logging scope, not proof about unrecorded actions. Report gaps and expiry explicitly; never assert that no change occurred because no accessible log exists.

## Changes and approval

Propose required categories, approved destination, access restrictions, retention and estimated logging cost. Do not enable prompt/content capture by default. For evidence export, minimize identities and properties and agree on a private storage location.

## Verification and escalation

Verify collection status with an existing permitted event; creating a new test event/change needs separate consent. Deliver an evidence timeline with provenance and gaps. Preserve original private evidence through the customer's approved process, not a public issue or unapproved LLM upload.

## Sources

### Azure website

- Azure Monitor collection, observation and investigation capabilities: https://azure.microsoft.com/en-us/products/monitor/
- Log ingestion and retention pricing context: https://azure.microsoft.com/en-us/pricing/details/monitor/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log
- https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings

## Scenario coverage

S05-Q6, S07-Q4
