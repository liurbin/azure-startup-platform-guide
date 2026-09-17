# Inspect GPU eligibility, quota, and allocation failures

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

## Scope and prerequisites

Mode: reference or authorized read-only. No secrets or customer exports in Git. Provisioning, quota requests and reservations need approval.
Confirm cloud, subscription/offer, requested VM size/family, region/zone, regular or Spot priority, quantity and date needed.

## Official policy and live state

VM quota includes regional totals and family-specific limits. A quota allowance does not reserve physical capacity. SKU restriction metadata and allocation errors provide different evidence.

## Read-only checks

```text
az vm list-skus --subscription "<subscription-id>" --location "<region>" --resource-type virtualMachines --all --query "[].{name:name,family:family,restrictions:restrictions}"
az vm list-usage --subscription "<subscription-id>" --location "<region>"
```

`--all` includes restricted entries: a returned SKU is not proof that it is usable. Match the exact family, location/zone restrictions, current and requested units, and priority-specific quota where applicable. Do not translate vCPU quota into a GPU count without the requested size's specification.

For an existing failed attempt, open its deployment operation and Activity Log. Retain the sanitized error code, scope, SKU, zone, priority and UTC time. Do not repeatedly create instances to probe availability.

## Interpretation and decisions

Route insufficient allowance to the correct quota dimension; route quota-approved allocation failure to capacity/placement investigation. A supported SKU and adequate quota still do not guarantee immediate allocation. Alternative sizes, zones or regions must satisfy customer constraints and need approval.

## Changes and approval

Use Azure Portal's quota request surface for the correct compute family/region. Prepare current/requested amounts, intended use and timeline without exaggerating utilization. Paid capacity commitments, quota reallocation and region substitutions are separate decisions, not automatic troubleshooting.

## Verification and escalation

After approval, reread the exact total and family limits. Check actual allocation only as part of an approved deployment. If it still fails, provide the request reference and allocation error to support; do not describe the increase as a capacity reservation.

## Sources

### Azure website

- VM capabilities and size-family entry points: https://azure.microsoft.com/en-us/products/virtual-machines/
- Product availability by region; not a live SKU allocation guarantee: https://azure.microsoft.com/en-us/explore/global-infrastructure/products-by-region/
- Linux VM pricing example; use OS-matching prices for another guest: https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/quotas/per-vm-quota-requests
- https://learn.microsoft.com/en-us/azure/virtual-machines/quotas
- https://learn.microsoft.com/en-us/cli/azure/vm
- https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/windows/allocation-failure

## Scenario coverage

S03-Q1, S03-Q2
