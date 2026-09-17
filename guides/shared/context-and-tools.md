# Confirm cloud context and available tools

Policy checked: 2026-09-17. Status: source-reviewed; not tenant-tested.

## Scope and prerequisites

Mode: reference or authorized read-only. No secrets or customer exports in Git. Changes need explicit approval.
Use before a platform task. Obtain the intended cloud, tenant, subscription, target, and allowed actions; identifiers are private operational data, not public examples.

## Official policy and live state

Azure China uses cloud-specific endpoints and documentation. Team location is not a cloud selector. This release does not establish China offer or service eligibility.
Provider registration, resource-type locations, and available API versions are subscription/platform facts to inspect.

## Read-only checks

If no tools exist, provide the portal path and mark live state unknown. Do not silently install a CLI, extension, MCP server, or browser helper.

```text
az version
az cloud show --query "{name:name,resourceManager:endpoints.resourceManager}"
az account show --subscription "<subscription-id>" --query "{id:id,tenantId:tenantId,state:state}"
az provider show --namespace "<provider-namespace>" --subscription "<subscription-id>" --query "{namespace:namespace,state:registrationState}"
```

Run only after scoped authorization; replace placeholders. Compare the cloud endpoint and account tuple with the portal's directory/subscription context. In the portal: Subscriptions > selected subscription > Resource providers. For API versions, inspect the exact resource type in provider metadata or Resource Explorer.

## Interpretation and decisions

Stop on a cloud/tenant mismatch, inaccessible subscription, or unknown target. Distinguish missing tools, unauthenticated sessions, insufficient permission, and unsupported cloud. Do not equate any of these with an empty account.
For China, report the detected context and route to China-specific official documentation; do not reuse a global Foundry endpoint.

## Changes and approval

Interactive sign-in is performed by the customer; never request their password or token. Changing local cloud context, installing tools, or registering a provider requires approval. Register only a provider needed for an approved task, using a role allowed to perform its registration action.

## Verification and escalation

Return the confirmed tuple, tool capability/version, provider state, and observation time. Recheck registration for the requested resource type and region; a pending operation is not a blanket failure or success. Escalate contradictory contexts with sanitized IDs and error text.

## Sources

### Azure website

- Portal capabilities and entry points: https://azure.microsoft.com/en-us/get-started/azure-portal/
- Resource organization and platform access context: https://azure.microsoft.com/en-us/get-started/azure-portal/resource-manager/

### Technical documentation

- https://learn.microsoft.com/en-us/cli/azure/cloud
- https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli
- https://learn.microsoft.com/en-us/azure/china/resources-developer-guide
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types

## Scenario coverage

S01-Q2, S01-Q5, S02-Q1, S04-Q2, S05-Q1
