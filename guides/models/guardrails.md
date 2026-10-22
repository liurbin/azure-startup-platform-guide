# Inspect effective guardrails and prepare legitimate modification requests

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Task guide

| Task card | |
|---|---|
| Use this for | Inspect which guardrail is actually associated with a deployment; Distinguish configurable controls from approval-required modifications |
| Reader | Platform operators and authorized safety/compliance owners |
| Applies to | Foundry model/agent guardrails; Separate modified-guardrail and abuse-monitoring application routes |
| Prepare | Cloud, resource generation and deployment/agent; Requested behavior and permitted read/change scope |
| You will get | An effective-control/assignment finding and a legitimate approval or support route. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference or authorized read-only. No customer prompts, safety test content, tokens or secrets in Git. Control changes and applications require the authorized owner's approval.
Identify cloud, resource/project generation, target deployment or agent, caller role and the stated business requirement.

## Official policy and live state

Ordinary threshold configuration, modified Guardrails approval and modified abuse-monitoring approval are different paths. The current limited-access page describes eligibility for managed customers or eligible programs plus additional requirements; startup credits alone do not prove qualification.

## Read-only checks

1. Open the correct project/resource's Guardrails and controls surface. Record policy identity, whether it is a default or customer configuration, intervention points, categories, thresholds and actions.
2. Inspect assignment to the exact deployment/agent. Where the resource API exposes it, compare the deployment's `raiPolicyName` with the configuration. A created policy or a saved editor page does not prove association.
3. Record read/edit permission, restrictions on default controls and any displayed compliance warning.
4. For requested modification, follow the official limited-access page's separate links for modified Guardrails and modified abuse monitoring. Read current eligibility and required evidence; do not use a remembered or unofficial form.

## Interpretation and decisions

Output current effective configuration, source of inherited/default behavior, desired change and whether it is self-configurable, approval-required, unsupported or unknown. A blocked request or annotation alone is insufficient to reconstruct the entire policy. Do not conflate content-policy handling with identity or network failures.

## Changes and approval

Prepare a business-use justification, exact scope, requested controls and compensating controls using non-sensitive descriptions. The designated customer submits attestations and terms. Never bypass monitoring or turn off protection to make a test pass.
After documented approval, compare its scope and conditions with the intended resource before proposing an edit.

## Verification and escalation

Reopen configuration and assignments after an approved change. Record approval reference, applied scope and state. A benign behavior check needs separate consent and cannot prove every guardrail path. Send unexpected compliance notices to the designated support/review channel; do not suppress the notice.

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](../shared/context-and-tools.md)

**Related tasks:** [Platform changes, audit coverage and retention](../network/audit.md); [Warnings, version changes and retirement](notifications.md)

**If blocked:** [Resource, data-plane and billing permissions](../accounts/permissions.md); [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

### Azure website

- Foundry governance and runtime-control capabilities; not proof of an effective assignment or exemption: https://azure.microsoft.com/en-us/products/ai-foundry/control-plane
- Related platform capability context: https://azure.microsoft.com/en-us/products/ai-foundry/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/foundry/guardrails/how-to-create-guardrails?view=foundry
- https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/limited-access

## Scenario coverage

S02-Q4, S07-Q2, S07-Q3
