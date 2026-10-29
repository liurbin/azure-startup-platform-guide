# Azure Startup Platform Guide

[中文说明](README.zh-CN.md)

Platform knowledge for startup founders, technical leaders, finance owners, Cloud Ops teams and their LLM agents using **Azure Global**. The 22 guides are written in Chinese; this English directory links to the same articles, not an English article edition. Readers who do not read Chinese can use an agent that supports translation.

> **Use it:** give your agent this README URL and your question, ask it to read 1–3 relevant guides and answer in your question's language (or a language you specify), preserving applicability conditions, uncertainty and source links.

When translating or adapting an explanation, keep exact role names, error codes and field names, explain necessary terms on first use, and do not turn a service example into an Azure-wide rule. If the guides do not answer the question, state the gap rather than fill it with an unsupported claim.

## Purpose and boundaries

The library explains accounts and billing, identity, spending, governance policy, platform security and audit, quotas, capacity and support. It is a reference, not an execution procedure.

Each article begins with a plain-language answer. Facts state whether they apply generally, to a particular agreement, or only to a named example. Related articles add a different answer rather than repeat the same policy.

It does **not** cover application architecture, service configuration/deployment/operations, network configuration, backups, domains or certificates. Other Azure clouds are outside scope.

Stable mechanisms can be explained from the articles. A balance, current capacity, exact contract eligibility or unresolved incident still needs its own account/contract evidence; the library does not invent these values. Sources document the basis and current-information lookup points, not a requirement to reread every source for every conceptual question.

## Directory

| Governance layer | Guide | What it answers | Full URL |
|---|---|---|---|
| Foundations | [Resource hierarchy](guides/00-foundations/resource-hierarchy.md) | What each container means and which management boundaries justify grouping or splitting. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/00-foundations/resource-hierarchy.md |
| Foundations | [Billing hierarchy](guides/00-foundations/billing-hierarchy.md) | Which agreement, billing object and role govern payment access. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/00-foundations/billing-hierarchy.md |
| Foundations | [Provider registration](guides/00-foundations/resource-providers.md) | Whether a registration error really concerns registration, permission or unsupported API/location. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/00-foundations/resource-providers.md |
| Credits and billing | [Credits](guides/01-credits-and-billing/credits.md) | How credit types, balance fields, eligible use and expiry conditions differ. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/01-credits-and-billing/credits.md |
| Credits and billing | [Purchases and terms](guides/01-credits-and-billing/purchases-and-terms.md) | Who accepts/buys an offer and where to find and assess contract documents and reports. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/01-credits-and-billing/purchases-and-terms.md |
| Credits and billing | [Invoices](guides/01-credits-and-billing/invoices.md) | How invoice scope, billing cadence and usage details explain the amount due. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/01-credits-and-billing/invoices.md |
| Credits and billing | [Ownership and transfers](guides/01-credits-and-billing/subscription-and-billing-transfer.md) | How billing transfers, directory changes and resource moves differ. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/01-credits-and-billing/subscription-and-billing-transfer.md |
| Governance: identity | [Access types](guides/02-governance/identity/access-types.md) | Which identity, action and scope explain an access refusal. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/identity/access-types.md |
| Governance: identity | [Identity lifecycle](guides/02-governance/identity/identity-lifecycle.md) | How people, application identities, federation and ownership survive a handoff. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/identity/identity-lifecycle.md |
| Governance: cost | [Spend and budgets](guides/02-governance/cost/spend-and-budgets.md) | How to compare spending, budget notifications and shared-cost allocation. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/cost/spend-and-budgets.md |
| Governance: cost | [Unexpected charges](guides/02-governance/cost/unexpected-charges.md) | How to locate a cost change and separate current state from charge timing. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/cost/unexpected-charges.md |
| Governance: policy | [Policy denials](guides/02-governance/policy/policy-denials.md) | Which governance assignment/effect applies and what an exception actually means. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/policy/policy-denials.md |
| Governance: policy | [Platform controls](guides/02-governance/policy/platform-controls.md) | How service content controls, abuse monitoring and access eligibility differ from Policy. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/policy/platform-controls.md |
| Governance: security | [Security signals](guides/02-governance/security/security-alerts.md) | What an alert or exposed credential proves, and what remains unconfirmed. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/security/security-alerts.md |
| Governance: audit | [Audit evidence](guides/02-governance/audit/change-history.md) | Which changes, data calls, LLM telemetry and log queries can be traced. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/audit/change-history.md |
| Quota and capacity | [Availability](guides/03-quota-and-capacity/availability.md) | Whether a product/version/type is supported for the intended context. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/03-quota-and-capacity/availability.md |
| Quota and capacity | [Quotas and limits](guides/03-quota-and-capacity/quotas-and-limits.md) | Which allowance, unit, model pool and tier apply. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/03-quota-and-capacity/quotas-and-limits.md |
| Quota and capacity | [Capacity](guides/03-quota-and-capacity/capacity.md) | Why enough allowance can still result in allocation failure. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/03-quota-and-capacity/capacity.md |
| Quota and capacity | [429 throttling](guides/03-quota-and-capacity/throttling.md) | How management requests and model-call limits require different evidence. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/03-quota-and-capacity/throttling.md |
| Support | [Notices and retirements](guides/04-support/notices-and-retirements.md) | How to identify future changes, affected objects and action owners. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/04-support/notices-and-retirements.md |
| Support | [Service health](guides/04-support/service-health.md) | What public, personalized and single-resource health can establish. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/04-support/service-health.md |
| Support | [Support requests](guides/04-support/support-requests.md) | Which support path, evidence, severity and follow-up fit the actual problem. | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/04-support/support-requests.md |

Maintenance rules: [AGENTS.md](AGENTS.md), [CLAUDE.md](CLAUDE.md). The [questions](scenarios/questions.md) and [coverage](scenarios/coverage.md) files are maintenance regression material, not another reader index or proof of tenant validation.

**Last updated: 2026-10-29**
