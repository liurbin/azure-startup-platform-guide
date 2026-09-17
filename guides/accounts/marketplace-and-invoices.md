# Check Marketplace purchase conditions and invoice access

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

## Scope and prerequisites

Mode: reference or authorized read-only. No invoice contents, addresses, payment details or secrets in Git. Commercial terms and billing changes require the authorized customer's approval.
Identify cloud, billing agreement, billing account/profile, subscription, seller, offer and plan. Do not equate an Azure role with a billing role.

## Official policy and live state

Marketplace purchase and private-offer acceptance are distinct actions; permission requirements depend on agreement and offer type. Purchase policies can prevent acquisition even when a resource role is present. Invoice access and generation also depend on the agreement.

## Read-only checks

For acquisition, open the actual offer and its availability/eligibility details. Check Marketplace purchase controls on the applicable billing profile or enrollment, private Marketplace restrictions, and the roles for both acceptance and subscription/purchase. Capture only a redacted offer reference, outcome and blocker.

For invoices, open Cost Management + Billing > the appropriate billing scope > Invoices. Select the relevant invoice/period, not merely a similarly named subscription. Check the current documented agreement-specific role. Locate Download and the authorized bill-to/PO-number change surface; do not download or alter documents during a reference-only review.

## Interpretation and decisions

Classify blocked purchase as role, policy, agreement, market/offer eligibility, or unaccepted private offer. Do not route all failures to "grant Owner".
A missing invoice can mean it is not generated, access/tenant is wrong, or the account does not issue one in that situation. No invoice does not prove no usage. Tax documents and local invoicing requirements need the relevant billing support, not invented global rules.

## Changes and approval

Prepare separate acceptance and purchase handoffs, including who must act and the possible charge. Never accept legal terms for the customer. An authorized billing owner must approve invoice-detail changes; do not promise retroactive changes for every account or jurisdiction.

## Verification and escalation

After customer action, verify offer/order status, exact billed subscription and actual invoice details at the right scope. Reconcile credit coverage separately. Send disputed eligibility or document corrections through official billing/program channels with minimal identifiers.

## Sources

### Azure website

- Subscription offer classification and applicable offer terms: https://azure.microsoft.com/en-us/support/legal/offer-details/
- Billing/subscription support and purchase-related support conditions: https://azure.microsoft.com/en-us/support/legal/faq/

### Technical documentation

- https://learn.microsoft.com/en-us/marketplace/roles-permissions
- https://learn.microsoft.com/en-us/marketplace/purchase-control-options
- https://learn.microsoft.com/en-us/azure/cost-management-billing/understand/download-azure-invoice

## Scenario coverage

S02-Q2, S05-Q5
