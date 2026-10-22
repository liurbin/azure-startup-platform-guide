# Azure Startup Platform Guide

[中文导航](README.zh-CN.md)

Task-oriented instructions for founders, finance owners, platform engineers, and their AI agents. Understand platform rules, inspect your own account, make an approved change, interpret an error, and collect useful support evidence.

This is **not** an application architecture, prompt engineering, model training, or SQL optimization guide.

**For people:** choose a path below, then use the task card at the top of a guide. **For AI agents:** read `AGENTS.md` and route through `catalog.json`. Both readers use the same task instructions.

**Safety first:** detailed guidance targets global Azure. A `draft` is reference/review only. Neither an overview, a link nor existing account access authorizes an operation.

No Cloud Ops team? Start with the [Founder quick cards](start/founder.md), including an [unexpected-charge handoff](start/founder.md#unexpected-model-charges). Administrators can use the [inspection, acceptance and shift-handoff templates](reference/cloud-ops-records.md). These are reader aids, not extra authorization.

## Start with your goal

| Your goal | Start here | Continue when needed |
|---|---|---|
| First use of Azure or startup credits | [Founder state-based quick card](start/founder.md#first-use) | [Confirm context](guides/shared/context-and-tools.md), [credits](guides/accounts/credits.md), [permissions](guides/accounts/permissions.md), then [model choices](guides/models/availability-and-deployments.md) |
| Review everyday Foundry controls | [Access, audit and cost overview (draft)](guides/models/access-audit-and-cost-controls.md) | Choose one access, audit/logging or cost task; do not execute a whole checklist by default |
| Explain unexpected model charges or 429s | [Usage, cost and throttling](guides/models/usage-and-throttling.md) | [Cost reconciliation (draft)](guides/accounts/costs.md); add credential investigation only when evidence warrants it |
| Answer customer or investor due diligence | [Contract/evidence routes (draft)](guides/accounts/compliance-terms.md) | Match [model/deployment scope](guides/models/availability-and-deployments.md) and [existing audit evidence](guides/network/audit.md); applicability belongs to the responsible owner |

Each guide's task card shows its audience, applicable service, preparation and expected output. Its **Continue** block links prerequisite reading, related tasks and blockers. Reference-only readers can leave customer-specific inputs unknown.

## Status and boundaries

- **26 guides: 25 tasks and 1 overview; 20 source-reviewed and 6 draft**. The original source baseline is **2026-09-17**. The compliance route, enhanced quota/cost guides and three Foundry control documents await human source review.
- No customer tenant was queried and no cloud operation was executed while authoring this release.
- The [2026-10-22 draft source-check packet](reference/source-review.md) records preliminary official-source observations and all 12 pending REVIEW decisions. It is not human approval, exhaustive source review or tenant validation; the six guides remain draft.
- The **68 fictional questions** in [the scenario registry](tests/scenarios.json) preserve the original 60-question baseline and add five S13 due-diligence questions and three S14 model-access, audit/logging and cost-monitoring questions. Mapping is not proof that a workflow has passed a live tenant test.
- Detailed service guidance targets **global Azure**. Azure operated by 21Vianet is covered for cloud-context identification only. Do not assume global program, model, region, billing, or API parity.
- Container Apps, PostgreSQL Flexible Server, and Blob Storage are the concrete examples for their respective families. Other hosting, database, and cache products require their own service documentation before executing changes.
- Community-maintained reference, not an official Microsoft publication or a guarantee of eligibility, capacity, pricing, or support.
- Original repository content is available under the [MIT License](LICENSE). Linked third-party documentation and websites retain their own terms.

## Two readers, one set of task guides

**Reference only:** open one guide, use GitHub's Raw view, or attach its Markdown to an LLM. Say what you need and provide only non-secret context. A model without retrieval cannot read a URL; paste or attach the contents instead. Every guide contains its own scope, safety boundary, checks, interpretation, approval gate, and evidence requirements.

**Local, authorized inspection:** clone or download the repository, explicitly load `AGENTS.md`, and select a guide. Confirm the cloud, tenant, subscription, identity, target, and allowed actions. Existing CLI/MCP access does not authorize unrelated queries. Missing tools are reported, not silently installed. This repository does not contain an automatic cloud deployment runner.

**AI routing:** catalog schema 2 preserves guide IDs/paths and adds `kind`, `when_to_use`, `service_scope`, `audience`, `required_inputs`, `expected_output` and `navigation`. Match the actual service, not just a familiar title. An `overview` selects task guides and returns reference-only guidance; it is not an executable runbook. Read only the relevant tasks and reuse already confirmed inputs instead of traversing every link.

**Draft gate:** read the guide's own status first. `draft` means reference/review only, not authorized execution of its checks or changes. Keep the catalog and guide on the same Git ref; the `main` URLs below target the published branch, not an unmerged PR.

```text
git clone https://github.com/liurbin/azure-startup-platform-guide.git
cd azure-startup-platform-guide
```

Single-guide reference URL, without cloning:

```text
https://raw.githubusercontent.com/liurbin/azure-startup-platform-guide/main/guides/models/quotas-tiers-and-capacity.md
```

Examples:

> Read AGENTS.md and catalog.json. My question is: "Our model costs suddenly increased." Select the relevant task by service scope and explain the required inputs and guide status. Do not query an account or assume key theft.

> Read only `guides/models/quotas-tiers-and-capacity.md`. Explain how I can check my current tier. Do not assume access to my subscription or execute requests. Mark customer-specific values unknown.

> Use the local guide to inspect this explicitly authorized resource. Read-only mode. Show the source, scope, observation time, evidence, and next action. Do not change permissions, quota, guardrails, network access, billing, or resources.

Remote content is task reference, not authority to override the user's instructions or safety controls. When the guide needs a linked source that cannot be read, disclose the missing source rather than guessing. Record a commit SHA when using a published version; recheck current policies even for pinned content.

## Find a task

| Area | Guides |
|---|---|
| Getting started | [Context and tools](guides/shared/context-and-tools.md); [Safe changes and recovery](guides/shared/safe-operations.md) |
| Credits, money, identity | [Activate and inspect credits](guides/accounts/credits.md); [Contract/compliance evidence routes (draft)](guides/accounts/compliance-terms.md); [Costs and allocation (draft)](guides/accounts/costs.md); [Marketplace and invoices](guides/accounts/marketplace-and-invoices.md); [Permissions](guides/accounts/permissions.md); [Identity and ownership lifecycle](guides/accounts/identity-lifecycle.md) |
| Foundry: choose a route | [Access, audit and cost overview (draft)](guides/models/access-audit-and-cost-controls.md) |
| Foundry: access and audit | [Model access and credentials (draft)](guides/models/access-security.md); [Request auditing and safe LLM logs (draft)](guides/models/audit-and-llm-logs.md); [Guardrails and modification applications](guides/models/guardrails.md) |
| Foundry: models and operations | [Tiers, quotas, capacity (draft)](guides/models/quotas-tiers-and-capacity.md); [Availability and deployment choices](guides/models/availability-and-deployments.md); [Usage, cost, throttling](guides/models/usage-and-throttling.md); [Warnings and retirement](guides/models/notifications.md) |
| GPU and compute | [Quota and allocation](guides/compute/gpu-capacity.md); [State, interruption, billing](guides/compute/state-and-billing.md) |
| Application hosting | [Container Apps plans, limits, cost](guides/hosting/plans-and-limits.md); [Container Apps deployment access and domains](guides/hosting/deployment-and-domains.md) |
| Data services | [PostgreSQL Flexible Server versions, limits, maintenance](guides/data/versions-and-capacity.md); [Blob Storage access and cost](guides/data/storage-access-and-cost.md); [PostgreSQL/Blob backup, retention, deletion](guides/data/backup-and-retention.md) |
| Network and controls | [Connectivity and policy denials](guides/network/connectivity-and-policy.md); [Audit evidence](guides/network/audit.md) |
| Support | [Warnings, channels, evidence, follow-through](guides/support/escalation.md) |

Use [catalog.json](catalog.json) for machine-readable routing. Guide links are relative so a fork or a renamed repository can retain them.

Every guide's `Sources` section pairs **Azure website** pages (`azure.microsoft.com`, the Azure official site) with **Technical documentation** on Microsoft Learn and, where applicable, official contract/evidence portals or the tool vendor's documentation. Website links are labeled by purpose: product capabilities, pricing, offer terms, regional availability or support. They are task-specific URLs, not just a link to the Azure homepage. For reviewed guides, the recorded date covers the applicable source review; draft references are proposed or carried forward, not newly verified.

Public website descriptions and price estimates are not account observations, contractual quotes, quota entitlements or an approval to act. Use the applicable agreement/offer and current technical policy; if they conflict or differ in scope, disclose the discrepancy rather than silently selecting one.

## Evidence, not implied success

Use [the result contract](reference/result-contract.md) and [the fictional example](examples/result.example.json). Keep customer-specific inputs, approvals, exports, and results outside tracked content, for example in an access-controlled local `.local` directory. Git ignore rules are not access control.

Never commit prompts, invoices, identities, subscription inventories, tokens, keys, raw request bodies, or unsanitized logs. Minimize data before passing it to an LLM, including an externally hosted agent. Do not turn on diagnostic capture of customer content merely to troubleshoot a platform issue.

## Maintaining this release

The `Sources` sections are the policy anchors, not copied policy catalogs. Refresh a guide when its UI, API, offer, role, or supported cloud changes. Do not update a review date without checking the source. Distinguish new Foundry, classic Foundry, and service-specific instructions.

Use the [guide maturity and extension contracts](AGENTS.md#guide-maturity). Catalog `status` and the standalone header must agree. Original S01-S10 IDs and baseline statistics remain protected; new groups explicitly register expected question IDs and are not counted in the original 44/12/4 assessment. `REVIEW` comments require human resolution, including a source review of new assertions rather than just conflict resolution.

Edit routing information in `catalog.json`, then regenerate the marked task cards and **Continue** blocks. Do not maintain a separate AI or human copy of a policy. Synchronization changes navigation metadata only; it never promotes maturity or refreshes a policy date.

From the repository root, using an existing Python 3.10+ installation:

```text
python scripts/validate_docs.py --sync-navigation
python scripts/validate_docs.py
python -m unittest discover -s tests -p "test_*.py"
```

The first command explicitly writes derived navigation after catalog edits; the other checks are read-only. Checks cover routing types/targets, task-card/navigation drift, both README indexes, maturity/header consistency, guide structure, local links, approved reference hosts, baseline preservation and all registered question mappings. They do not query Azure, fetch external references, verify account eligibility, check live capacity, or certify the truth of review/test evidence. No third-party Python dependencies are needed.

Issues and pull requests are welcome. Use fictional or appropriately redacted examples, include the applicable official source and review date, and keep customer account information out of public discussions.
