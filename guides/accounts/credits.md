# Activate and inspect startup credits

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Task guide

| Task card | |
|---|---|
| Use this for | Find activation, binding, remaining credits or expiry; Check whether the actual offer covers a model purchase |
| Reader | Founders, finance owners and authorized benefit owners |
| Applies to | Microsoft for Startups/Azure credit offers; Offer-specific benefit and billing views |
| Prepare | Cloud, program/offer and joining date; Intended account and subscription; authorization for live values |
| You will get | A benefit/binding checklist with separately sourced balance, validity and unresolved eligibility. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference or authorized read-only. No payment details, referral codes, identity documents, or customer exports in Git. Activation and commercial acceptance require explicit customer approval and action.
Obtain cloud, program/offer name, application or joining date, intended account, and target subscription. Do not assume acceptance or a particular credit amount.

## Official policy and live state

The activation guidance reviewed here branches at **2026-05-29**: earlier participants use the startup-portal path; participants joining on or after that date use the Azure-portal path. Recheck this branch and the actual offer before acting.
Model catalog presence does not establish credit eligibility. Match the actual seller, billing route, offer, and meter against the current credit-use guidance.

## Read-only checks

1. Have the customer open the applicable program page and record application/activation status, linked account, benefit identifier, and activation deadline. Mask identifying details in shared output.
2. In Azure Portal, confirm directory and subscription. Open Cost Management + Billing at the authorized billing scope; inspect the credits/payment-methods surface offered for that account. For a sponsorship-specific experience, follow the official offer's link rather than assuming the same UI for every account.
3. Record awarded/remaining credit, displayed consumption, currency, validity dates, and observation time separately. Mark an unavailable field unknown.
4. For a model purchase, identify seller, offer/plan, subscription and billing route before deciding whether credits apply.
5. Read the offer's expiry and post-credit billing arrangements. Do not infer automatic free continuation or automatic shutdown.

## Interpretation and decisions

No displayed credit can mean incomplete activation, the wrong identity/scope, missing billing access, or delayed posting. An "already redeemed" message needs the program's documented support route, not a second fabricated identity. Joining a startup team does not itself prove Azure billing access.

## Changes and approval

Prepare a checklist only. The customer signs in, supplies personal/payment information, accepts terms, chooses the binding, and confirms activation. Do not transfer subscriptions or remove spending controls as an activation workaround.

## Verification and escalation

Reopen the benefit and billing views; confirm the intended binding, status and actual balance. An activation click alone is not proof. Hand off conflicting offer/account states to program support with sanitized status and reference IDs; billing discrepancies go to billing support.

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](../shared/context-and-tools.md)

**Related tasks:** [Cost visibility, allocation and spending controls](costs.md); [Marketplace acquisition and invoice access](marketplace-and-invoices.md)

**If blocked:** [Resource, data-plane and billing permissions](permissions.md); [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

### Azure website

- Sponsorship offer terms; first verify that this is the customer's actual offer: https://azure.microsoft.com/en-us/pricing/offers/ms-azr-0036p/
- Offer directory for matching other subscription offers: https://azure.microsoft.com/en-us/support/legal/offer-details/

### Technical documentation

- https://learn.microsoft.com/en-us/startups/build/azure-getting-started/activate
- https://learn.microsoft.com/en-us/startups/benefits/azure-credits/use-azure-credits
- https://learn.microsoft.com/en-us/startups/microsoft-for-startups/mfs-program-page
- https://learn.microsoft.com/en-us/microsoft-for-startups/azure-credits-team-member

## Scenario coverage

S01-Q1, S01-Q3, S01-Q4, S02-Q5, S08-Q1, S08-Q4
