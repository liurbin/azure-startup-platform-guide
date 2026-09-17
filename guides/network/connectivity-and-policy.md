# Separate network, identity, private-endpoint, and policy failures

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

## Scope and prerequisites

Mode: reference or authorized read-only. No secrets, packet payloads or private configuration exports in Git. DNS, network, identity, endpoint approvals and policy exemptions need explicit approval.
Identify source network/client, destination resource/FQDN, cloud, permitted connection path and sanitized error.

## Official policy and live state

A private endpoint resource existing is not proof of approved connection or correct DNS. Policy assignment can be inherited independently of resource RBAC. An external agent may be unable to reach a private endpoint even when a customer-side host can.

## Read-only checks

1. On the resource, inspect public-network access, firewall rules and private-endpoint connections with their actual approval/provisioning state.
2. Inspect the endpoint's DNS configuration, private DNS zone links and resolver path relevant to the approved source network. Use only that network's authorized DNS diagnostic; do not probe arbitrary address ranges.
3. Compare the expected service hostname and resolution route. Do not publish private IPs or resolver topology.
4. For an authorization error, check the intended principal and operation separately from connectivity.
5. For `RequestDisallowedByPolicy` or another policy denial, read the failed operation's assignment/definition references. Inspect effective scope, parameters, exemptions and the responsible governance owner.

## Interpretation and decisions

Classify DNS, endpoint approval, routing/firewall, service authorization, organizational policy, or unknown. A network timeout does not mean missing RBAC; a policy denial is not fixed by granting Owner. If the agent is outside the approved network, return a customer-side read-only checklist instead of bypassing isolation.

## Changes and approval

Propose minimal, scoped DNS/network/role changes. Policy exceptions go to the governance owner with justification and intended duration. Do not make the resource public, allow all addresses, or bypass an organizational denial to finish onboarding.

## Verification and escalation

From the approved network and identity, repeat the specific permitted connectivity/read check. Confirm actual endpoint approval and effective policy. Preserve sanitized operation/assignment IDs and timestamps for support. Application protocol or code defects are handed back explicitly.

## Sources

### Azure website

- Private Link capability and connectivity context: https://azure.microsoft.com/en-us/products/private-link/
- Azure Policy governance and enforcement context: https://azure.microsoft.com/en-us/products/azure-policy/

### Technical documentation

- https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns
- https://learn.microsoft.com/en-us/azure/private-link/manage-private-endpoint
- https://learn.microsoft.com/en-us/azure/governance/policy/how-to/determine-non-compliance
- https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security

## Scenario coverage

S05-Q2, S05-Q3, S09-Q2
