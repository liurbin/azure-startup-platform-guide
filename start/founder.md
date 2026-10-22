# Founder quick cards

[中文](founder.zh-CN.md) | [Full index](../README.md)

Reading and handoff only, not an authorization to inspect or change an account. A linked draft remains reference/review only. No customer tenant was accessed to create these cards.

## First use

Choose the row that describes you. You do not need every Azure identifier before asking a reference question.

| Your state | Next reading | What to establish |
|---|---|---|
| Startup-program access, but no Azure subscription yet | [Credits and activation](../guides/accounts/credits.md) | Actual program/offer, current official activation route and intended account. The customer handles sign-in, commercial acceptance and payment information; do not create an arbitrary paid subscription to complete this checklist |
| A subscription exists, but credits are unclear | [Context](../guides/shared/context-and-tools.md), then [credits](../guides/accounts/credits.md) | Intended cloud/account and actual benefit binding, remaining balance and expiry; inaccessible values stay unknown |
| The model already works | [Foundry control overview](../guides/models/access-audit-and-cost-controls.md) | Choose the current access, audit/logging or cost task; do not repeat every onboarding step |

Minimal vocabulary: **cloud** is the Azure environment and endpoints; **tenant** is the identity directory; **subscription** is a resource/access and billing-management scope; **deployment** is the selected model-service deployment. Location or language alone does not choose the cloud.

If a page becomes too technical, ask an AI to read `AGENTS.md`, `catalog.json` and the relevant guide, explain the next step in plain language, and leave live values unknown. Missing tools are not a reason to install a CLI or share credentials.

Done with this card means you know your current state, the selected task and its responsible owner. It does not mean activation, eligibility or deployment has succeeded.

## Unexpected model charges

| What you know | Immediate handoff |
|---|---|
| Only spending increased; no exposure evidence | Use [usage reconciliation](../guides/models/usage-and-throttling.md) and [cost guidance](../guides/accounts/costs.md) to align scope, usage period, currency and data freshness. Do not label the cause key theft |
| A key was publicly exposed or credible unexplained access is ongoing | Contact the authorized account/incident owner promptly. Use an independently reviewed and approved response process; billing investigation can run in parallel. Do not wait for a final invoice or invent authority from a draft |
| You cannot inspect the account | Record the access gap and ask the authorized owner or [appropriate support route](../guides/support/escalation.md); a blank view is not zero spending |

Do not send keys, tokens, authorization headers, complete prompts/responses or invoices to public issues or unapproved agents. Do not regenerate both keys, delete a resource group or change production networking as a generic stop-loss shortcut. A budget alert is not an automatic consumption stop.

## Safe handoff

Copy this blank record to an approved private location, not into tracked files:

```text
Question and desired outcome:
Discovered at, including time zone:
Cloud/service and resource alias, if known:
Observed facts and their source/time:
Unconfirmed hypotheses:
Business impact and whether traffic is ongoing or unknown:
Actions already taken, actor role and time:
Responsible account/incident owner and next contact:
Missing access or evidence:
```

For a team without Cloud Ops, the founder/account owner identifies an authorized engineer or the appropriate official support channel. Benefit/billing and technical/security questions can require different owners and support eligibility. Do not assume every startup has a dedicated administrator or unrestricted technical support.

## Next owner

| Concern | Responsible role |
|---|---|
| Credits, binding or disputed charges | Benefit/billing owner; program or billing support where applicable |
| Credentials, access or ongoing suspicious use | Authorized identity/platform or incident owner |
| LLM content, log readers or exports | Data/security owner |

[Return to the full index](../README.md). For the source-review gate, see the [draft review packet](../reference/source-review.md).
