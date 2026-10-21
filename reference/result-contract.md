# Customer result contract

Use this shape for human reports or JSON; do not invent live values in reference mode.

Guide maturity and result `status` are separate. A selected `draft` guide can only yield `mode: reference` and `status: reference_only`, without customer-query findings. A reviewed or tested guide still needs the customer's scoped authorization; its maturity alone is not an execution result.

| Field | Required meaning |
|---|---|
| `mode` | `reference` or `authorized_read_only`; an approved change needs a separate operation record |
| `status` | `reference_only`, `verified`, `action_required`, `blocked`, or `unsupported` |
| `scope` | Cloud, tenant, subscription, target resource, service/deployment type; unknown fields are null |
| `observed_at_utc` | Observation timestamp, or null when no customer query was performed |
| `policy_sources` | Official URLs, checked dates, applicable offer/cloud/API/service generation |
| `findings` | Statement, supporting observation, scope, source, interpretation, uncertainty |
| `unknowns` | Missing facts, why unavailable, and the minimum authorized way to obtain them |
| `next_actions` | Exact target, proposed action, responsible role, approval required, success evidence |

`verified` means the requested fact was checked in the approved scope. It does not mean the account is generally production-ready. An empty response, a 403, and an unsupported API are different states. Never translate them into zero usage, no quota, or no restrictions.

For changes, record approved deltas, execution timestamps, operation IDs, before/after state, and any partial failure. A submitted request remains pending until approval and applicable platform state have been checked.

Keep all customer reports private by default. Use resource aliases in shareable summaries. Do not include prompt text, invoices, payment data, tokens, keys, SAS URLs, or complete request bodies. Obtain consent before providing even sanitized customer information to an external agent service.
