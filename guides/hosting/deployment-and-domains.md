# Diagnose platform deployment access and domain bindings

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

<!-- task-card:start -->
**At a glance**

**Guide type:** Task guide

| Task card | |
|---|---|
| Use this for | Investigate a Container Apps deployment or image-pull failure; Inspect hostname, DNS and certificate bindings |
| Reader | Container Apps operators and domain/registry owners |
| Applies to | Azure Container Apps; Selected registry, ingress and domain/certificate access paths |
| Prepare | Selected app/environment and deployment time; Image reference or hostname and sanitized platform error |
| You will get | A classified platform-access/binding finding and an exact owner/change or application handoff. |
<!-- task-card:end -->

## Scope and prerequisites

Mode: reference or authorized read-only. No registry secrets, environment-variable values or private logs in Git. Image access, identity, ingress, DNS, certificates and revisions require change approval.
Concrete host: Container Apps. Confirm the selected app/environment, image reference, deployment time and domain. Other hosts require their own deployment instructions.

## Official policy and live state

Registry authentication, permission to pull an image, host ingress and domain/certificate validation are separate checks. Certificate support depends on the actual host and configuration; do not promise a managed certificate for every setup.

## Read-only checks

1. Open deployment/revision status and platform/system logs for the incident interval. Retain sanitized pull/authentication/provisioning/health errors, not arbitrary application output.
2. Inspect image hostname/reference, selected registry identity and its scoped permissions. Check approved network access between the host and registry. Do not list credentials.
3. Compare configured platform port/ingress and platform health status with the deployment requirements supplied by the application owner. A code-level crash is a handoff boundary.
4. For domains, inspect ingress endpoint, hostname binding, verification records, certificate status, hostname coverage and expiry. Use the host's current documented validation records; do not invent DNS values.

## Interpretation and decisions

Classify a failed deployment as image not found, registry authorization, network reachability, platform resource allocation, platform configuration, application failure, or unknown. Treat domain ownership verification, DNS routing and TLS binding as separate states.

## Changes and approval

Propose exact identity/role changes, platform settings or DNS records with their owner. Do not expose a private app, rotate shared registry keys, replace a certificate or change traffic routing as a default fix. Preserve existing working revisions and the approved rollback route.

## Verification and escalation

Verify the new revision's platform status and actual hostname/certificate binding. A customer-approved endpoint check must not send sensitive content or imply application correctness. Supply platform operation IDs and redacted errors when escalation is necessary.

<!-- navigation:start -->
### Continue

**Before you start:** [Cloud context, tools and provider registration](../shared/context-and-tools.md)

**Related tasks:** [Federation, credential lifecycle and ownership](../accounts/identity-lifecycle.md); [Private endpoints, DNS, access and policy denials](../network/connectivity-and-policy.md); [Container Apps: plans, limits and idle costs](plans-and-limits.md)

**If blocked:** [Resource, data-plane and billing permissions](../accounts/permissions.md); [Support eligibility, warning routing and evidence](../support/escalation.md)

Check each linked guide's own status and scope. A link does not grant authorization.
<!-- navigation:end -->

## Sources

### Azure website

- Container Apps hosting capabilities: https://azure.microsoft.com/en-us/products/container-apps/
- Registry capabilities when Azure Container Registry is the selected image source: https://azure.microsoft.com/en-us/products/container-registry/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/container-apps/troubleshooting
- https://learn.microsoft.com/en-us/azure/container-apps/managed-identity-image-pull
- https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-certificates

## Scenario coverage

S04-Q3, S04-Q4
