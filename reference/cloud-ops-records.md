# Cloud Ops inspection and handoff records

These are blank reference templates, not an executable runbook, approved baseline or tenant evidence. Read the selected task's scope and maturity first. A draft remains reference/review only; filling a form never grants permission.

Copy a template into a separately authorized private location outside tracked content. Do not fill customer identities, resource inventories, approval correspondence or runtime exports into this repository. Use aliases in shareable summaries; never collect key values, tokens, prompts, completions or invoices here.

## Inspection record

Use one record per control and target. `unknown` is the initial state, not an error to hide.

```text
Record ID / selected guide / guide status:
Cloud / service generation / endpoint or deployment type:
Target alias and authorized scope:
Question / control:
Approved expected state and its policy or decision reference:
Observed current state: unknown
Evidence source, exact query scope, observation time and data freshness:
Private evidence reference; collection or sampling gaps:
Conclusion: unknown | conforms | does_not_conform | not_applicable
Reason; applicability evidence if not_applicable:
Responsible role / next action / next review time:
```

An expected state comes from the applicable reviewed policy and authorized owner, not a universal assumption that every customer must use the same network, identity or logging configuration. `conforms` describes this control and evidence only, not general production readiness or legal compliance.

| Control | Evidence to record if authorized | Do not infer |
|---|---|---|
| Model access | Intended principals, effective operation/scope, remaining key paths, approved consumers and connectivity evidence | A role assignment means every intended operation works |
| Credentials | Credential type/slot metadata, consumer coverage, approved change time and rejected/working paths after a permitted check | A visible key copy was deleted, therefore every copied value is revoked |
| Request audit | Existing schema/categories, correlation fields, capture start, sampling and missing caller metadata | An aggregate metric or shared key proves individual user identity |
| LLM content and log access | Where content is captured, purpose/approval, readers, exporters, retention and configuration privileges | A single SDK flag controls every exporter or makes all data safe |
| Costs and credits | Usage window, billing scope/basis/currency/period/freshness, actual benefit source and expiry, attribution method and residual | Token volume is a complete real-time bill or missing data is zero |
| Alerts | Scope, metric or actual/forecast condition, window, threshold, recipients, responder, observed delivery and separate action evidence | A saved budget means notification arrived or spending stopped |

Use [access security](../guides/models/access-security.md), [LLM logs](../guides/models/audit-and-llm-logs.md), [costs](../guides/accounts/costs.md), [usage](../guides/models/usage-and-throttling.md) and [credits](../guides/accounts/credits.md) only within their own gates.

## Change and acceptance record

Inspection authorization is not change authorization. A draft does not become executable because an approval field is populated.

```text
Change ID / selected reviewed task / responsible operator:
Exact target and allowed delta:
Before-state evidence:
Proposed after-state and reason:
Affected consumers / downtime tolerance / cost exposure:
Data collection, destination and retention implications:
Private approval reference, approved scope and validity:
Execution time / operation reference / partial failures:
Recovery constraints and approved rollback:
Verification method and separately approved test budget, if any:
Observed after-state / evidence time / actual delivery or access result:
Result: unknown | verified_for_this_scope | action_required | blocked
Unresolved risks / next owner / follow-up:
```

Do not restore an exposed credential as a rollback shortcut. Any new test event, billable inference, role/key/network change or content capture needs exact approval; prefer existing permitted evidence where it can answer the question.

## Acceptance examples

These are criteria, not successful results or performed tests.

| Task | Evidence required before closing |
|---|---|
| Access change | Intended clients retain approved access, revoked paths are rejected using a supported check, and applicable propagation/unknowns are recorded |
| Metadata-only logging | Approved event fields are actually collected and correlated; prohibited content is excluded without exporting customer messages; actual readers/destinations/retention match the decision |
| Cost alert | Intended owner receives the applicable notification or an explicitly permitted test notification; record evaluation/delivery limitations and do not infer a hard stop |
| Cost containment | Separately observe ongoing request paths and continuing billed meters after the approved action; distinguish posting delay and fixed charges |

Do not invent a generic CLI/KQL command across resource generations. A service-specific procedure must state endpoint/API or schema version, target scope, required permission, redaction and success evidence. Missing permission or unsupported fields stay blocked/unknown, not an invitation to elevate or enable content capture.

## Shift handoff

```text
Incident or control and business impact:
Confirmed facts / hypotheses / unknowns:
Authorized scope and actions already performed:
Private evidence and approval references:
Current traffic / billing freshness / ongoing cost exposure:
Next action, responsible role and deadline:
Customer/platform/security/data/billing handoffs still pending:
```

The next operator should be able to repeat the authorized observation and understand the limits without contacting the document author. Use the [result contract](result-contract.md) for outward reporting and the [source-review packet](source-review.md) for publication gates.
