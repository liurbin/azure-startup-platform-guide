# Check VM state, interruptions, and residual charges

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

## Scope and prerequisites

Mode: reference or authorized read-only. No raw logs or secrets in Git. Stop, deallocate, delete, resize and cleanup operations require explicit approval.
Confirm exact VM/scale-set instances, priority, attached resources, billing period and incident interval.

## Official policy and live state

Guest shutdown, stopped-but-allocated and deallocated are distinct states. Deallocation does not mean every associated storage, networking or commercial charge ends. An OS state is not a complete billing state.

## Read-only checks

```text
az vm get-instance-view --subscription "<subscription-id>" --resource-group "<resource-group>" --name "<vm-name>"
```

In the portal, inspect power/provisioning state, disks, addresses, scale-set membership and associated resources. Use Cost analysis grouped by resource/meter to identify actual charges and separately inspect any reservation/commitment.

For interruption, correlate Activity Log, Resource Health, Service Health and existing scheduled-event/Spot-eviction records where configured. Preserve timestamps and platform event IDs. A missing historical event cannot prove that no interruption occurred.

## Interpretation and decisions

Report compute allocation state and each residual billed resource separately. Classify an event as customer operation, platform maintenance, Spot/capacity event, resource health issue, or unknown based on evidence. Do not make application crashes a platform diagnosis without evidence.

## Changes and approval

Explain state transition, availability/data impact, retained resources and recovery limits before approval. List individual deletion targets; shared disks, IPs, backups and commitments are not automatically disposable. Never terminate a shared workload as a billing shortcut.

## Verification and escalation

After an approved transition, reread actual state and inspect remaining resources. Later cost records may still reflect earlier use; compare the operation timestamp with the meter period. Escalate unresolved charges or platform interruptions using sanitized state and event evidence.

## Sources

### Azure website

- VM product and purchasing context: https://azure.microsoft.com/en-us/products/virtual-machines/
- Linux VM billing options; match the actual OS and agreement when estimating: https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing
- https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms
- https://learn.microsoft.com/en-us/azure/service-health/overview
- https://learn.microsoft.com/en-us/cli/azure/vm

## Scenario coverage

S03-Q3, S03-Q4, S03-Q5
