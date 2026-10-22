# Determine which models and deployment options you can use

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Task guide

| Task card | |
|---|---|
| Use this for | Check whether a model/version can be used; Compare supported deployment and processing-location choices |
| Reader | Founders, model platform owners and compliance reviewers |
| Applies to | Microsoft Foundry model catalog and deployment choices; New/classic resource-generation identification |
| Prepare | Cloud, resource generation and model/version; Intended processing boundary and authorized subscription scope |
| You will get | An evidence-backed candidate table separating availability, permission, terms, quota and capacity. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference or authorized read-only. No customer payloads or secrets in Git. Deployment, purchase and terms acceptance require approval.
Identify the cloud, subscription, resource generation (new Foundry, classic hub/project, or another service), model/version and intended processing boundary.

## Official policy and live state

Catalog visibility, commercial eligibility, permission, deployment support, quota and capacity are separate checks. Hosting routes are not the same as regional/global/data-zone SKU choices. Managed compute, API-based access and instant-access previews must not be described as interchangeable.

## Read-only checks

1. Open the actual model card in the correct portal generation. Capture publisher/seller, version, lifecycle, access conditions, supported APIs/features and linked deployment availability.
2. Inspect the deployment chooser without submitting it. Record supported types, regions/data zones, displayed pricing basis and any eligibility or quota message.
3. Compare with current deployment-type and lifecycle documentation. Read at-rest and inference-processing conditions separately; neither is inferred from a resource's displayed location alone.
4. For an existing deployment, inspect its resource ID, model/version, SKU/type, capacity, status and update policy. Do not assume the current catalog describes its exact configuration.
5. For audio/realtime use, obtain feature-specific connection/concurrency limits from the selected model's current service documentation. Do not convert TPM into a guessed session count.

## Interpretation and decisions

Return one row per candidate: usable now, application required, blocked, unsupported, or unknown, with evidence. Do not deploy as a discovery probe. A quota API listing an old model does not prove that new deployments are supported. Model availability does not prove credits cover its meter.

## Changes and approval

Present only observed eligible options and their processing, cost and capacity differences. The customer decides and approves creation, commercial acceptance, or any region/type/version change. Do not silently substitute another model or cross a processing boundary.

## Verification and escalation

Verify the actual model/version/type/location and successful provisioning after an approved operation. Any inference test is a separate potentially billable action. Keep a timestamped availability decision, not a static repository-wide list of "available models".

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](../shared/context-and-tools.md)

**Related tasks:** [Current tier, quota allocation and capacity](quotas-tiers-and-capacity.md); [Marketplace acquisition and invoice access](../accounts/marketplace-and-invoices.md); [Contract and compliance evidence: where to look and who decides](../accounts/compliance-terms.md)

**If blocked:** [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

### Azure website

- Foundry platform and model capability overview: https://azure.microsoft.com/en-us/products/ai-foundry/
- Azure OpenAI deployment and model-service context: https://azure.microsoft.com/en-us/products/ai-foundry/models/openai
- Public pricing options; select the applicable model, region, currency and agreement: https://azure.microsoft.com/en-us/pricing/details/azure-openai/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview
- https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types?view=foundry-classic
- https://learn.microsoft.com/en-us/azure/foundry/how-to/deploy-models-managed
- https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements

## Scenario coverage

S06-Q2, S07-Q1, S10-Q1, S10-Q2, S13-Q3
