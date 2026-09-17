# Inspect costs, allocate shared spending, and check controls

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

## Scope and prerequisites

Mode: reference or authorized read-only. No invoices, customer exports, or secrets in Git. Changing budgets, tags, allocation rules, or spending controls needs approval.
Confirm billing agreement, authorized billing/subscription scope, currency, date range, and whether the request concerns usage, charges, invoices, or credit balance.

## Official policy and live state

Budgets notify; they are not an automatic universal spending cap. Offer-specific spending limits and separately configured automation are different controls. Cost allocation changes analytical attribution, not ownership of the original bill. Check which allocation features the customer's agreement supports.

## Read-only checks

1. Open Cost Management + Billing > Cost Management > Cost analysis. Select the exact scope and date range; record filters and cost basis, including actual versus amortized where available.
2. Group by subscription, resource group, resource, service and meter as available. Inspect idle compute, provisioned capacity, storage, logs and network charges rather than blaming model calls alone.
3. Compare credits, cost details and invoice totals only after aligning scope, currency and period. Identify adjustments, posting delay, purchases and the fields excluded from each view. Preserve the observation timestamp.
4. For project allocation, inspect existing resource tags and supported Cost allocation rules. List untagged/shared charges and an explicit allocation method; do not pretend labels automatically cover every historical meter.
5. Open Budgets and review scope, thresholds, recipients and action groups. Separately inspect the offer's spending-limit status and any approved automation.

## Interpretation and decisions

A blank view is not zero spending: verify billing-scope access, filters and data freshness. A budget email does not establish that resources stopped. Missing allocation features require an explicitly labeled reporting approach, not invented portal settings.

## Changes and approval

Propose tag keys, assignment owners, allocation rules, thresholds and recipients. Preview reporting differences. Do not remove a spending limit, purchase a commitment, disable production resources, or enable paid diagnostic exports without specific approval.

## Verification and escalation

Return a resource/meter attribution and a separate balance comparison, with unknowns. Confirm saved controls and their actual notification/action behavior; do not trigger billable load to test a budget. Escalate unexplained charges with sanitized meter, scope, period and cost basis.

## Sources

### Azure website

- Cost analysis, allocation, export and budget capabilities: https://azure.microsoft.com/en-us/products/cost-management/
- Estimates for proposed usage, not a record of customer charges: https://azure.microsoft.com/en-us/pricing/calculator/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-allocation-introduction
- https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets
- https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit
- https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/assign-access-acm-data
- https://learn.microsoft.com/en-us/azure/cost-management-billing/understand/understand-usage

## Scenario coverage

S01-Q3, S02-Q5, S02-Q6, S08-Q2, S08-Q4, S09-Q5
