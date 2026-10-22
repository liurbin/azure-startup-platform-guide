# Find contractual and compliance evidence without deciding legal applicability

Policy checked: [set on review]. Status: draft; sources not re-verified; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Task guide

| Task card | |
|---|---|
| Use this for | Locate provider DPA, BAA or regional contract evidence; Route a customer or investor due-diligence request |
| Reader | Founders and customer legal, compliance or contract owners |
| Applies to | Agreement-specific provider evidence; Service/model scope and report access conditions |
| Prepare | Exact evidence request and agreement/channel; Relevant service/model and responsible contract owner |
| You will get | A private evidence index and owner questions, not a legal or compliance verdict. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference only while draft. Do not execute the read-only checks or changes below until source review and explicit customer authorization. Changes and document acceptance always require approval.

This is a "where to look and who decides" route for BAA, DPA, service-scope, data-location and due-diligence questions. It does not determine legal compliance, interpret a contract, prepare the startup's own DPA, or recommend an architecture.

Ask for the exact customer question, intended cloud, agreement/offer reference, direct/CSP channel, relevant service/model/deployment identifiers, and the customer's contract owner. Keep actual contracts, customer names, private service inventories and legal correspondence out of Git and unapproved LLM contexts.

## Official policy and live state

Distinguish a published provider document, its applicability to the customer's agreement, a service's documented scope, the actual deployed configuration, and the startup's own obligations. Finding a document or a model in a catalog does not establish all five.

The links below are proposed evidence routes, not newly verified policy conclusions. A page's current version is not automatically the version governing an existing agreement. An authorized contract owner must establish the applicable documents.

<!-- REVIEW: The draft says HIPAA Business Associate terms are included in Product Terms / DPA instead of requiring a separate signature for most commercial customers. No such default is asserted here; a human must verify the agreement, channel, service scope and applicable signature process. -->

## Read-only checks

1. Classify the request using the table below. Separate "our startup's DPA" from "our cloud provider's DPA", and a request for evidence from a request to sign or attest.
2. Ask the authorized billing/contract owner to identify the agreement and channel. Use billing properties as supporting evidence where available; do not infer a legal agreement from a subscription display name or credits balance.
3. Locate the applicable document through its official source. Record title, version/effective date, relevant section, access conditions and observation time. Do not invent an interpretation when a clause or service listing is absent.
4. Match the exact service and deployed configuration. For models, use the [availability and deployment guide](../models/availability-and-deployments.md) to separate model/version, processing location and deployment type. Do not infer HIPAA or EU-scope suitability just from "Global" or "Data Zone".
5. Return a private evidence index and unresolved questions to the responsible owner. Do not download or redistribute restricted reports, accept portal terms, sign documents, or submit a customer questionnaire as part of these checks.

| Customer question | Where to look | What to record | Who resolves applicability |
|---|---|---|---|
| Where are the provider's DPA and sub-processor terms? | DPA landing page, Product Terms, and the customer agreement's referenced documents | Document/version, cited sections, requested provider versus startup document | Customer legal/contract owner |
| Do we need a BAA and who signs? | HIPAA/HITECH offering documentation, applicable Product Terms and agreement/channel records | Service scope evidence, relevant terms, any unresolved acceptance/signature requirement | Customer legal/signatory; provider or CSP contract contact for missing documents |
| Where are any regional addenda relevant to this agreement? | The applicable agreement/offer documents and Product Terms selection | Contracting entity/channel, the identified annex/version and unresolved applicability; do not infer contract terms from the resource region | Customer contract owner and provider/CSP contract contact |
| Does this deployed model meet the requested framework or data-location constraint? | Service-specific scope documentation plus observed deployment settings | Exact service/model/type, evidence of processing locations, requirements still unconfirmed | Customer compliance/legal owner, informed by the platform owner |
| Can we share SOC/ISO reports in a data room? | Service Trust Portal and the particular report's access/reuse conditions | Report title/period, documented scope and sharing conditions; not the report contents | Authorized evidence owner/signatory |
| Which terms apply to a Marketplace model? | Actual seller, offer/plan, purchase record and applicable provider terms | Parties, terms/version and unresolved scope; not an assumption based on a catalog badge | Procurement/contract owner |

## Interpretation and decisions

Report `document located`, `scope not established`, `access unavailable`, or `contract-owner decision required` as findings, not a compliance verdict. Absence from a listing is an unresolved applicability issue, not proof of permission or a basis for an improvised waiver.

<!-- REVIEW: The draft says a provider-DPA citation plus the startup's processor obligations usually satisfies a request for "your DPA". Keep provider evidence and the startup's own contractual documents separate; human review must establish what the requester actually needs. -->

<!-- REVIEW: The draft treats written acceptance of an unlisted-service gap by a legal/compliance owner as ending the blocker. This route does not equate a signoff with legal compliance or permission to process regulated data. -->

Do not present a report, a signed form, a deployment region or a Microsoft/Azure catalog label as a universal assurance. Unresolved questions go to the owner's qualified reviewers; the agent supplies traceable pointers.

## Changes and approval

Prepare a checklist only. Signing, accepting terms, negotiating amendments and committing answers to a customer require the authorized signatory and appropriate review. Procurement permissions are covered in [Marketplace and invoices](marketplace-and-invoices.md); they are not legal approval.

Region, deployment-type or data-movement changes require the separate platform change process and explicit approval. Do not make a technical change as a substitute for resolving applicability.

## Verification and escalation

Before an authorized customer submission, the owner rechecks the applicable document versions and the actual service/configuration scope. Contract gaps go to the provider/CSP contract contact; legal interpretations go to the customer's legal owner.

<!-- REVIEW: The draft describes Service Trust Portal access and NDA-style acceptance as uniform. Verify access and redistribution conditions for the actual portal action and report; do not assume every artifact has identical requirements. -->

Keep report contents and agreement evidence in the customer's approved location. Use [audit](../network/audit.md), [permissions](permissions.md) and [support handoff](../support/escalation.md) for scoped operational evidence, not a public upload of protected materials.

Source-check observations and unresolved human decisions are tracked in the [draft review packet](../../reference/source-review.md). The packet does not promote this guide or establish contractual applicability.

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](../shared/context-and-tools.md)

**Related tasks:** [Available models and deployment options](../models/availability-and-deployments.md); [Platform changes, audit coverage and retention](../network/audit.md)

**If blocked:** [Marketplace acquisition and invoice access](marketplace-and-invoices.md); [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

These addresses are carried forward or proposed from the input material. They have not been fetched or re-verified in this change.

### Azure website

- Identify the applicable offer before selecting contract routes: https://azure.microsoft.com/en-us/support/legal/offer-details/
- Sponsorship offer reference only when that exact offer applies: https://azure.microsoft.com/en-us/pricing/offers/ms-azr-0036p/

### Technical documentation

- HIPAA/HITECH offering and service-scope route: https://learn.microsoft.com/azure/compliance/offerings/offering-hipaa-us
- Service-specific compliance documentation index: https://learn.microsoft.com/azure/compliance/

### Contract and evidence portals

- DPA document/version landing page: https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA
- Product Terms and agreement selection: https://www.microsoft.com/licensing/terms/
- Report discovery and report-specific access/reuse conditions: https://servicetrust.microsoft.com/

## Scenario coverage

S13-Q1, S13-Q2, S13-Q3, S13-Q4, S13-Q5
