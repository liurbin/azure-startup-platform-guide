# Inspect costs, allocate shared spending, and check controls

Policy checked: [set on review]. Status: draft; sources not re-verified; not tenant-tested.

Previous source-reviewed baseline: 2026-09-17. Existing controls, source links and scenario IDs are retained; additions and conflicts require human source review.

## Scope and prerequisites

Mode: reference only while draft. Do not execute the read-only checks or changes below until source review and explicit customer authorization. No invoices, customer exports, or secrets in Git. Changing budgets, tags, allocation rules, or spending controls needs approval.
Confirm billing agreement, authorized billing/subscription scope, currency, date range, and whether the request concerns usage, charges, invoices, or credit balance.

Choose the immediate task: explain a number, investigate a change, allocate shared spend, or inspect a notification/control. This is not application optimization or a recommendation to resize production. Use [credits](credits.md) for benefit activation and [Marketplace and invoices](marketplace-and-invoices.md) for commercial documents.

## Official policy and live state

Budgets notify; they are not an automatic universal spending cap. Offer-specific spending limits and separately configured automation are different controls. Cost allocation changes analytical attribution, not ownership of the original bill. Check which allocation features the customer's agreement supports.

<!-- REVIEW: The draft describes sponsorship/credit-funded consumption as universally creating cost records with a credit offset against the invoice, and describes Marketplace presentation generically. Verify the actual agreement, view, charge type and visibility instead of applying one display/accounting model to every offer. -->

## Read-only checks

1. Open Cost Management + Billing > Cost Management > Cost analysis. Select the exact scope and date range; record filters and cost basis, including actual versus amortized where available.
2. Record actual cost for the period, the displayed forecast and its horizon if available, and the view's freshness information. Mark an absent forecast unknown; do not manufacture one from the current total.
3. Group by subscription, resource group, resource, service and meter as available. Record the top contributors and their quantities/units. Inspect idle compute, provisioned capacity, storage, logs and network charges rather than blaming model calls alone.
4. Compare credits, cost details and invoice totals only after aligning scope, currency and period. Identify adjustments, posting delay, purchases and the fields excluded from each view. Preserve the observation timestamp.
5. For a spike, compare equivalent before/after windows using the same filters and cost basis. Locate the first changed interval, then drill into resource, meter and quantity. Correlate authorized Activity Log evidence where relevant, but distinguish observations from hypotheses.
6. For project allocation, inspect existing resource tags and supported Cost allocation rules. Record untagged/shared charges and the denominator used to calculate any untagged share. Identify directly attributable, rule-allocated and still-unassigned amounts; do not pretend labels automatically cover every historical meter.
7. Open Budgets and review scope, thresholds, recipients, actual/forecast alert type and action groups where exposed. Record whether the relevant condition has fired and whether delivery/action evidence is available. Separately inspect the offer's spending-limit status and any approved automation.
8. Read remaining credits and expiry from the appropriate benefit view, not by subtracting Cost analysis from a remembered award. The [credits guide](credits.md) supplies the offer-specific handoff.

Use a small reconciliation record rather than one unexplained total:

| Item | Record |
|---|---|
| Comparison context | Scope, agreement/view, period, currency, filters, actual/amortized basis and observation time |
| Observed spending | Actual cost, displayed forecast/horizon if any, top resources/services/meters, quantities and adjustments visible |
| Benefit state | Credit balance and expiry, their own source/scope/time, and any unavailable fields |
| Allocation | Tag/rule method, directly assigned amount, allocated share, residual/unassigned amount and any estimate label |
| Controls | Budget condition/recipients, separate spending-limit or automation state, and unknown delivery/action evidence |

Keep raw cost exports and customer resource names private. Share aliases and minimal figures only with the customer's approval.

## Interpretation and decisions

A blank view is not zero spending: verify billing-scope access, filters and data freshness. A budget email does not establish that resources stopped. Missing allocation features require an explicitly labeled reporting approach, not invented portal settings.

| Finding | Next platform-use step |
|---|---|
| Two totals disagree | Align context and included charge categories first; identify residual differences without editing either amount |
| A recent interval is incomplete | Record freshness/unknowns and arrange a later comparison; do not conclude that an observed charge vanished |
| A resource/meter grew | Check quantity, configuration, period and pricing evidence before assigning cause |
| Allocation is incomplete | Identify unassigned spend and a supported, documented allocation/reporting method; do not fabricate precision |
| A budget fired | Check the configured notification and separate action/control evidence; do not assume a universal cap |
| Credits approach expiry or exhaustion | Confirm actual offer-specific continuation/stop/charging arrangements with the authorized owner |

<!-- REVIEW: The draft says high untagged spend makes allocation impossible and the fix is enforcement rather than a spreadsheet. Preserve supported allocation and explicitly labeled reporting alternatives; missing tags alone do not establish that no attribution method is available. -->

<!-- REVIEW: The draft uses resource-change correlation to favor a deployment explanation and lack of Activity Log correlation to escalate possible metering issues. Treat these as hypotheses; an absent control-plane change is not proof about usage, price or metering correctness. -->

<!-- REVIEW: The draft says exhausting credit automatically becomes invoiced cost on the next cycle and expiry forfeits the balance. No universal transition or loss rule is asserted here; human review must establish the actual offer and billing arrangements. -->

Do not treat a forecast as a guarantee or an authorization to spend. Do not alter a charge, change an agreement, or diagnose a billing defect just to make the views agree.

## Changes and approval

Propose tag keys, assignment owners, allocation rules, thresholds and recipients. Preview reporting differences. Do not remove a spending limit, purchase a commitment, disable production resources, or enable paid diagnostic exports without specific approval.

Provide the approver with exact scope, current/requested setting, account-type availability, expected reporting effect, possible cost/service impact and success evidence. A tagging/reporting change and a resource-sizing change are separate approvals. Keep this task focused on platform use.

## Verification and escalation

Return a resource/meter attribution and a separate balance comparison, with unknowns. Confirm saved controls and their actual notification/action behavior; do not trigger billable load to test a budget. Escalate unexplained charges with sanitized meter, scope, period and cost basis.

After approved allocation/tag changes, compare the same scoped report after applicable refresh and explain residual/unassigned costs. After a budget change, confirm the saved condition and recipients; delivery not yet observed remains unknown. For disputes, provide both view definitions, meter/quantity evidence and timestamps without uploading invoices or raw exports publicly.

## Sources

Existing sources are retained. Additional draft references below have not been fetched or re-verified in this change.

### Azure website

- Cost analysis, allocation, export and budget capabilities: https://azure.microsoft.com/en-us/products/cost-management/
- Estimates for proposed usage, not a record of customer charges: https://azure.microsoft.com/en-us/pricing/calculator/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-allocation-introduction
- https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets
- https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit
- https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/assign-access-acm-data
- https://learn.microsoft.com/en-us/azure/cost-management-billing/understand/understand-usage

### Proposed additional references

- https://learn.microsoft.com/azure/cost-management-billing/costs/
- https://learn.microsoft.com/azure/cost-management-billing/costs/quick-acm-cost-analysis
- https://learn.microsoft.com/azure/cost-management-billing/costs/tutorial-acm-create-budgets
- https://learn.microsoft.com/azure/cost-management-billing/costs/allocate-costs
- https://learn.microsoft.com/azure/cost-management-billing/costs/enable-tag-inheritance
- https://learn.microsoft.com/azure/cost-management-billing/costs/understand-cost-mgt-data
- https://learn.microsoft.com/azure/cost-management-billing/manage/spending-limit

## Scenario coverage

S01-Q3, S02-Q5, S02-Q6, S08-Q2, S08-Q4, S09-Q5
