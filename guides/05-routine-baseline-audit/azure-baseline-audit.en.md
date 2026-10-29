---
title: "Routine Baseline Audit"
applies_to:
  - "Azure Global"
  - "Read-only recurring audit of a user-specified scope"
last_verified: 2026-10-29
related:
  - guides/02-governance/security/security-alerts.md
  - guides/02-governance/cost/spend-and-budgets.md
  - guides/04-support/service-health.md
---

# Routine Baseline Audit

[Chinese version](azure-baseline-audit.md)

Give the instruction below to your agent to check security, spending, and errors and warnings on an agreed schedule. Actual auditing requires appropriate data-reading capabilities; this page provides no data connectors, schedulers or execution tools.

The audit's areas of attention do not extend the coverage of the library's knowledge articles. For areas such as networking, hosts or backups, use the official requirements applicable to the services in use. This page provides no configuration procedures and does not establish coverage of every security control or compliance certification.

## Copyable audit instruction

```markdown
# Azure Routine Baseline Audit

On the agreed schedule, perform a read-only audit of the specified Azure Global environment. Use the actual information you can read and focus on these three areas.

## 1. Security
Refer to the official security baselines applicable to the services in use, checking their version and applicability. Review:
- Identities and permissions, network security and data protection.
- Audit logging, and host and backup security where applicable.
- Access control and data protection for AI services.

Identify important security gaps and risks that are new or have worsened since the previous audit.

## 2. Spending
Review:
- Spending trends, unusual increases and unexplained ongoing charges.
- Budgets, credit balances and expiry.
- Spending risks that need advance attention based on the current trend.

Explain the main sources of change and what needs confirmation or action.

## 3. Errors and warnings
Review:
- Important alerts and recurring errors from the platform and AI services.
- Quota, throttling and service-health issues.
- Platform notices requiring action and important unresolved issues.

Distinguish actual business impact from informational messages; do not dump every alert.

## Output requirements
- Start with a brief conclusion, then rank important findings by impact.
- For each finding, explain what was found, what it affects and what to prioritize, with the evidence source and observation time.
- Compare with the previous record when available. Explicitly identify missing data or unverifiable areas; do not treat them as an audit pass.

## Boundaries
Only inspect and recommend. Do not automatically change the environment or permissions, or make purchases.
Do not expand into enterprise asset governance, DevOps processes, application code, AI application design or configuration implementation.
```

## References

- [Microsoft cloud security benchmark introduction](https://learn.microsoft.com/en-us/security/benchmark/azure/introduction)
- [Security baselines for Azure overview](https://learn.microsoft.com/en-us/security/benchmark/azure/security-baselines-overview)
