# Interpret model warnings, upgrades, and retirement notices

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Task guide

| Task card | |
|---|---|
| Use this for | Classify a model warning or retirement notice; Identify affected deployments, owners and deadlines |
| Reader | Model platform owners and notice recipients |
| Applies to | Foundry model lifecycle notices; Platform, billing and safety-notice routing |
| Prepare | Sanitized notice, origin, timestamp and deadline; Approved target deployment scope |
| You will get | An affected/unaffected deployment list and an owner/deadline handoff with unresolved facts. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference or authorized read-only. No raw customer messages, secrets or account exports in Git. Version changes, control changes and support submissions need approval.
Obtain a sanitized notice, its origin, timestamp, deadline, target scope and intended recipient. Verify notices through official surfaces rather than trusting email links.

## Official policy and live state

Lifecycle policy, availability of a replacement and the deployed version are different facts. New versus classic portal experiences must not be mixed. Do not freeze model retirement dates in this repository.

## Read-only checks

1. Open the official lifecycle policy and the affected model/version's current schedule.
2. Inspect matching deployments, including their exact version, type, region and update settings. Do not scan unrelated subscriptions.
3. Classify the notice: retirement/update, quota/capacity, resource/service health, billing, guardrail compliance, or abuse review. Read the actual deadline and requested action.
4. For lifecycle changes, identify the responsible resource operator, whether an automatic update is configured, the supported replacement choices and any approval required.

## Interpretation and decisions

Return affected versus unaffected deployments with evidence. A general announcement is not proof that every deployment is affected. An update policy is not a guarantee that a replacement meets application requirements.
For compliance or abuse notices, use the designated review/support process. Do not reclassify them as transient failures or advise bypassing controls.

## Changes and approval

Prepare a platform change plan with exact version/type, expected billing/processing implications, owner and deadline. Application compatibility is an explicit handoff, not something this guide assumes or fixes. Do not replace or delete a model deployment automatically.

## Verification and escalation

After customer approval and execution, inspect actual version, update policy, provisioning state and continued notice applicability. Any inference test is separately authorized. Escalate contradictory dates, unavailable replacements or unclear policy scope with notice/reference IDs and sanitized deployment details.

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](../shared/context-and-tools.md)

**Related tasks:** [Available models and deployment options](availability-and-deployments.md); [Support eligibility, warning routing and evidence](../support/escalation.md)

**If blocked:** [Resource, data-plane and billing permissions](../accounts/permissions.md); [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

### Azure website

- Current model-service capability context: https://azure.microsoft.com/en-us/products/ai-foundry/models/openai
- Azure support channels for platform notices and incidents: https://azure.microsoft.com/en-us/support/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements
- https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/working-with-models
- https://learn.microsoft.com/en-us/azure/service-health/overview

## Scenario coverage

S06-Q6, S10-Q4, S10-Q6
