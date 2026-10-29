# Changelog

本项目记录结构和事实变化。日期采用 `YYYY-MM-DD`。

## 2026-10-29 — 新增例行基线审计

- 新增`guides/05-routine-baseline-audit/`，与基础、计费、治理、配额容量和支持同级，不新增独立routines或prompts入口。
- 提供独立中文与英文指令，按安全、费用、错误与警告、输出要求和边界组织，不套知识guide九段模板。
- 双语README在原目录中各增加一个对应语言的审计条目，不拆分为两套阅读体系，也不放指令全文。
- 审计保持高层只读建议，不附加数据连接、任务调度、配置实施或自动整改；不能把无法验证当通过。
- 同步AGENTS/CLAUDE维护规范；原有22篇知识正文、路径及65题覆盖保持不变，不因审计提示涉及某领域而宣称知识已覆盖。

## 2026-10-29 — 阅读闭环与多语言回答

- 资源层级篇补小团队、开发/生产、跨区域与多订阅共同治理的条件化判断，不规定统一订阅数量。
- 购买与条款篇补DPA、BAA、Product Terms及服务信任门户的官方入口，说明版本、服务范围、报告期间和访问/共享条件。
- 复核当前来源后区分私有报价分步流程与符合条件的单击购买；提交、各产品购买结果与实际可用状态不混为一谈。
- 双语README明确Agent按提问或指定语言回答，保留条件、未知与来源；中文正文仍为唯一答案集，不宣称提供英文正文版本。
- 保持22篇、九段模板及单一目录，不加入跨云对照索引、配置步骤或客户资格承诺。

## 2026-10-29 — 正式入口发布

- 双语README的22篇完整URL同步指向main，移除草稿分支预览说明。
- 本次只调整发布入口和README更新日期；guide的来源复核日期与事实正文保持不变。
- 发布到main不代表客户状态已核实、合同资格已获批准或已完成租户执行测试。

## 2026-10-28 — 治理层级重构

### 本轮实质修订：三点可读性与事实边界

- 22篇逐篇改写白话结论与首次术语释义，保持文件路径和九段模板，不新增guide或读者索引。
- 所有规则先列适用条件，区分平台机制、具体协议、classic/preview与产品示例，不把服务专属结论泛化。
- 每类主要答案只在一篇展开：计费对象→billing-hierarchy；权益资格→credits；发票口径→invoices；日常预算/分摊→spend-and-budgets；费用变化→unexpected-charges。
- 身份ID与授权→access-types；身份生命周期/联合信任→identity-lifecycle；治理Policy→policy-denials；服务控制→platform-controls；安全信号→security-alerts；日志与可追溯性→change-history。
- 可用组合→availability；允许量/等级→quotas-and-limits；创建时分配→capacity；管理API/模型429→throttling；预告行动→notices；当前健康→service-health；支持资格/跟进→support-requests。
- 修正Credits资源Amount与余额混淆、两类托管身份生命周期、caller字段解释、Policy例外属性、SKU错误分类及classic来源适用性。
- 删除没有所引官方依据的header负值“已知显示问题”、固定标签页、统一数据保留/响应/默认配额等断言，不用猜测替代。
- 原两篇确认基准保留表达风格，不再豁免事实纠正；默认等级清单、上线日期和固定秒数改为机制及查询维度。
- 在现有篇内精简保留OIDC信任与授权分离、合同证据边界、角色撤销不等于Key失效、LLM元数据/正文区别、内部成本分摊与未分配残差。
- 中英文README同步22篇目录；标明完整URL是尚待发布的目标main路径，未宣称已经线上可用。
- 65个回归题号保留；Q053/Q054/Q057～Q059去除冻结日期、未核实UI和显示缺陷前提；coverage按主要答案归属重映射并保留部分/范围外。
- AGENTS/CLAUDE只写维护规范；旧版兼容跳转不另增guide，破坏性迁移保留原包与审核材料作为历史。

### 定位

- 改为 Azure Global startup 平台问题参考知识库，不再作为 agent 执行规程。
- 只覆盖账号、计费、身份、费用、策略、配额、容量和支持。
- 明确移出应用架构、服务配置/运维、网络配置、备份、域名和证书。
- README 改为唯一入口，并同步英文与中文版本。

### 新目录

- 新建 `guides/00-foundations/`、`guides/01-credits-and-billing/`、`guides/02-governance/`、`guides/03-quota-and-capacity/`、`guides/04-support/`。
- 新写 `subscription-and-billing-transfer.md` 与 `security-alerts.md`。
- 新建 `scenarios/questions.md` 与 `scenarios/coverage.md`，仅供维护和回归测试。

### 迁移与合并

- `shared/context-and-tools.md` → `00-foundations/resource-hierarchy.md`、`billing-hierarchy.md`、`resource-providers.md`。
- 删除 `shared/safe-operations.md`；不再保留 agent 变更规程。
- `accounts/credits.md` → `credits.md`。
- `accounts/marketplace-and-invoices.md` → `purchases-and-terms.md` + `invoices.md`。
- `accounts/compliance-terms.md` 的请求对象、供应商合同/客户义务与适用范围区分 → `purchases-and-terms.md`；不提供法律意见或受限报告访问/分享实施。
- `accounts/permissions.md` → `identity/access-types.md`。
- `accounts/identity-lifecycle.md` → `identity/identity-lifecycle.md`。
- `accounts/costs.md` → `cost/spend-and-budgets.md`。
- `compute/state-and-billing.md` 的计费部分 → `cost/unexpected-charges.md`；中断部分 → `service-health.md`。
- `hosting/plans-and-limits.md` 的空闲费用 → `unexpected-charges.md`；限额 → `quotas-and-limits.md`。
- `data/storage-access-and-cost.md` 的通用权限/费用判断 → `access-types.md` / `unexpected-charges.md`；具体存储限流、数据访问与网络配置移出，不声称模型例子覆盖存储专项。
- `data/versions-and-capacity.md` 的通用维护通知概念 → `notices-and-retirements.md`；数据库版本、连接与维护实施移出，不声称模型额度覆盖数据库专项限制。
- `network/connectivity-and-policy.md` 的策略 → `policy-denials.md`；网络内容移出，仅在 `access-types.md` 保留“网络拒绝不是权限问题”的判断。
- `network/audit.md` → `audit/change-history.md`。
- `models/availability-and-deployments.md` → `availability.md`。
- `models/quotas-tiers-and-capacity.md` → `quotas-and-limits.md`。
- `models/usage-and-throttling.md` → `throttling.md`；费用对账 → `unexpected-charges.md`。
- `compute/gpu-capacity.md` → `capacity.md`。
- `models/guardrails.md` → `policy/platform-controls.md`。
- `models/notifications.md` → `notices-and-retirements.md`。
- `support/` → `support-requests.md`，并拆出 `service-health.md`。
- `data/backup-and-retention.md` 与 `hosting/deployment-and-domains.md` 移出范围。

### 内容规范

- 22 篇 guide 统一使用 front matter 和九段中文模板。
- 删除 Mode、密钥声明、变更/审批章节与场景编号。
- 每条规则与事实附 Microsoft 官方来源；动态数值改为指向实时查询位置。
- 直接采用已确认的 `quotas-and-limits.md` 与 `throttling.md` 样板要点。
