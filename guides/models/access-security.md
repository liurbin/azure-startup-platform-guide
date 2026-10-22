# Inspect model access and contain credential exposure

Policy checked: [set on review]. Status: draft; sources not re-verified; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Task guide

| Task card | |
|---|---|
| Use this for | Inspect model identities, keys and network access; Plan authorized containment or rotation after credible credential exposure |
| Reader | Platform/identity administrators and incident owners |
| Applies to | Foundry/Azure OpenAI model endpoint access; Endpoint-supported Entra, resource-key and network controls |
| Prepare | Exact endpoint/resource and approved consumers; Authentication type, network path and exposure/incident interval if relevant |
| You will get | An access-path inventory, scoped control gaps and an approval/verification plan without secret values. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference only while draft. Do not execute read-only checks or changes until human source review and explicit customer authorization. Identity, key and network changes require separate approval.

Confirm cloud, tenant, subscription, exact model resource/endpoint, approved consumers, authentication type and network path. Distinguish Foundry resource keys, separate provider/serverless credentials, gateway credentials and Microsoft Entra identities. One endpoint's rotation or role procedure does not cover all others. Never request or print secret values.

## Official policy and live state

Model invocation, deployment management, key management and access administration are different operations. Use [permissions](../accounts/permissions.md) for their scope/role distinctions and [identity lifecycle](../accounts/identity-lifecycle.md) for federation and ownership handoffs.

Where supported, Entra authentication can replace stored application keys, but a client migration does not automatically disable remaining key access. Removing a role, deleting a visible key copy or moving the same leaked value into a vault does not revoke copied credentials. Network isolation and identity authorization are separate controls.

Unexpected charges do not establish credential theft. A credible exposure still warrants an authorized containment decision without waiting for a final invoice or complete forensic history.

## Read-only checks

1. Inventory approved consumers, authentication types and effective operation/scope permissions. Record credential metadata or slot, not values. Do not assume that a shared resource key is limited to one application or deployment.
2. Check the exact endpoint/client's Entra and managed/workload-identity support, remaining key-based consumers and local-authentication configuration. Do not infer that keyless capability means keys are disabled or that a compromised identity is harmless.
3. Inspect existing public-access settings, allowed networks and private endpoint approval. Use the [connectivity guide](../network/connectivity-and-policy.md) for approved client DNS/path evidence. A private endpoint object alone does not prove public ingress is disabled or legitimate clients can connect.
4. Ask the owner where necessary secrets are stored and whether they were exposed in browser/mobile code, shared source, notebooks, logs or unapproved tools. Record location/time and credential type, not the secret. Scope any repository investigation separately.
5. For an incident, preserve minimal existing request/time evidence privately and use [safe LLM audit evidence](audit-and-llm-logs.md). Missing attribution remains unknown; do not generate inference load or retrieve prompts to establish exposure.

## Interpretation and decisions

| Observation | Finding or handoff |
|---|---|
| Broad/shared access exists | Identify affected consumers and the least-privilege or keyless option actually supported |
| A key was exposed | Exposure established; the incident owner decides containment while unauthorized-cost attribution remains separate |
| No matching management event exists | Data-plane use is not excluded |
| Traffic persists after one credential change | Check other key slots, identities, gateways and provider paths within approved scope |
| An endpoint/client cannot support the proposed control | Report the limitation; do not silently change service or expose a private resource |

## Changes and approval

Obtain exact targets, intended deltas, affected consumers, acceptable outage/cost exposure and verification/recovery limits. Follow [safe operations](../shared/safe-operations.md). Never rotate unrelated subscription keys or delete deployments/resources as a generic stop-loss action.

For prevention, propose supported Entra authentication and least-privilege scope. Separately approve local-key disablement and network restrictions after compatibility/connectivity checks. If keys remain necessary, use a controlled server-side secret store such as Key Vault, not browser/mobile code or shared source. Do not restore an exposed credential as a rollback shortcut.

For credible exposure, the customer's incident owner chooses immediate revocation/restriction or a low-disruption migration. Immediate regeneration invalidates the old value and can interrupt clients. For resources covered by the documented two-key process: consolidate approved consumers on key 1, regenerate key 2, switch and verify consumers, then regenerate key 1. Assess both slots and other paths; do not rotate both simultaneously without an approved outage plan. Replacement values stay in the approved secret-delivery channel, never reports or chat.

## Verification and escalation

Use service-supported checks to establish intended-client access and rejection of revoked paths. If verification requires billable inference, obtain separate approval for a minimal test. A role assignment, saved network setting or successful regeneration alone is not proof of effective access.

Record change times and credential metadata privately, compare fresh request windows and route suspected compromise to the customer's security owner/platform support. Use [usage reconciliation](usage-and-throttling.md) and [cost analysis](../accounts/costs.md) for delayed or continuing charges. Never promise full caller attribution, a refund or credit restoration.

Keep any permitted inspection and change acceptance in the [private Cloud Ops records](../../reference/cloud-ops-records.md). See the [draft source-check packet](../../reference/source-review.md) for reviewed public sections and unresolved applicability; no maturity promotion or tenant check is implied.

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](../shared/context-and-tools.md)

**Related tasks:** [Resource, data-plane and billing permissions](../accounts/permissions.md); [Federation, credential lifecycle and ownership](../accounts/identity-lifecycle.md); [Private endpoints, DNS, access and policy denials](../network/connectivity-and-policy.md)

**If blocked:** [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

References are carried forward from the original draft and existing platform guides. Candidate technical sources were consulted on 2026-10-21; human source/applicability review remains pending. No tenant operation was performed.

### Azure website

- Secret-storage capabilities, not revocation of a copied key: https://azure.microsoft.com/en-us/products/key-vault/
- Private connectivity capability context: https://azure.microsoft.com/en-us/products/private-link/

### Technical documentation

- Foundry Models keyless authentication: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/configure-entra-id
- Network isolation and client requirements: https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link
- Resource-key scope for Foundry Tools; verify endpoint applicability: https://learn.microsoft.com/en-us/azure/ai-services/authentication
- Two-key rotation and immediate invalidation: https://learn.microsoft.com/en-us/azure/ai-services/rotate-keys

## Scenario coverage

S14-Q1
