# Azure Startup 云平台使用指南

[English index](README.md)

面向 startup 创始人、财务、平台工程师及其 AI Agent。范围是**云平台的政策、当前状态、开通配置、权限费用、限制告警与支持申请**，不包括应用架构、业务代码、提示词或模型训练方法。

## 这版已经包含什么

22 篇任务指南，覆盖七类平台主题，并新增“使用前准备”和“平台变更执行与恢复”两个共享主题。英文正文便于国内外团队共用；每篇都能单独交给 LLM 阅读，不必先加载整仓库。

官方来源复核日期为 **2026-09-17**。这是文档初稿，**没有访问客户订阅，没有执行云部署或变更**。60 道虚构场景题与正文建立对应关系，不等于经过 60 次真实客户环境验证。

仓库原创内容采用 [MIT 许可证](LICENSE)，欢迎复用、反馈和提交 PR。这里是社区整理的参考材料，不是 Microsoft 官方发布；所链接的官网和技术文档仍适用各自的条款。

## 按问题选入口

| 想解决的问题 | 阅读 |
|---|---|
| 只给 LLM 链接怎么用；缺工具怎么办；登录了哪朵云、哪个租户和订阅；资源提供程序未注册 | [使用前准备](guides/shared/context-and-tools.md) |
| Agent 如何检查已有资源、预览变更、等待确认；执行一半失败如何恢复和清理 | [平台变更规范](guides/shared/safe-operations.md) |
| Credits 激活、绑定、余额、有效期和到期安排 | [Credits](guides/accounts/credits.md) |
| 消费、分摊、标签、预算告警与支出限制 | [费用管理](guides/accounts/costs.md) |
| Marketplace 购买和条款；账单与发票 | [商业开通与票据](guides/accounts/marketplace-and-invoices.md) |
| 看账单、创建资源、调用模型分别需要什么权限 | [权限查询](guides/accounts/permissions.md) |
| GitHub 短期身份、凭据轮换、人员离开、所有权交接 | [身份生命周期](guides/accounts/identity-lifecycle.md) |
| 当前 Tier、升级策略、配额分配、余量和容量 | [模型配额](guides/models/quotas-tiers-and-capacity.md) |
| 当前可用模型、版本、区域、部署方式和数据处理位置 | [模型与部署选项](guides/models/availability-and-deployments.md) |
| 当前模型费用、用量不一致、429、临时限流 | [用量与限流](guides/models/usage-and-throttling.md) |
| 当前护栏、实际关联、护栏修改与滥用监控修改申请 | [护栏](guides/models/guardrails.md) |
| 模型警告、退役、升级通知 | [模型通知](guides/models/notifications.md) |
| GPU 规格、配额获批但机器分配失败 | [GPU 容量](guides/compute/gpu-capacity.md) |
| VM 停止、解除分配、删除、维护、中断与残留费用 | [算力状态与计费](guides/compute/state-and-billing.md) |
| 托管计划、实例上限、最低资源费用 | [托管限制](guides/hosting/plans-and-limits.md) |
| 容器镜像拉取失败、域名与证书绑定 | [部署与访问](guides/hosting/deployment-and-domains.md) |
| 数据库版本、规格、连接数、容量、维护 | [数据服务状态](guides/data/versions-and-capacity.md) |
| 存储访问、请求限制和传输费用 | [存储管理](guides/data/storage-access-and-cost.md) |
| 实际备份、恢复点、保留时间和删除后的保留项 | [备份与保留](guides/data/backup-and-retention.md) |
| 私有端点、DNS、网络规则、组织策略拒绝 | [连接与策略](guides/network/connectivity-and-policy.md) |
| 谁改了护栏、权限或公开访问；审计记录及保留 | [平台审计](guides/network/audit.md) |
| 告警分流、支持资格、工单材料、申请后生效检查 | [支持交接](guides/support/escalation.md) |

## 使用方式与范围

只参考：复制单篇正文或提供工具可读取的链接；没有环境访问权限时，当前状态必须写“未知”，不能引用文档默认值冒充客户实际值。

本地使用：显式加载 `AGENTS.md`，确认身份、云环境、租户、订阅和授权范围，再按具体模块只读检查。修改计费、权限、护栏、网络或资源前，必须取得本次操作的明确批准。

```text
git clone https://github.com/liurbin/azure-startup-platform-guide.git
cd azure-startup-platform-guide
```

不拉取仓库时，可以直接把单篇 Raw 地址交给支持联网读取的 Agent，例如：

```text
https://raw.githubusercontent.com/liurbin/azure-startup-platform-guide/main/guides/models/quotas-tiers-and-capacity.md
```

首版详细操作面向全球 Azure。世纪互联环境目前只覆盖环境识别和路由，不推断其服务、权益或模型与全球版相同。托管、数据库和存储的具体例子分别是 Container Apps、PostgreSQL Flexible Server 和 Blob Storage，不冒充覆盖所有产品。

每篇遵循：适用范围 → 官方政策与客户状态 → 只读检查 → 解读与分支 → 修改及审批 → 验证和交接。可机器读取的目录见 [catalog.json](catalog.json)，60 道题见 [tests/scenarios.json](tests/scenarios.json)。

每篇末尾的 `Sources` 都分为 **Azure website（Azure 官网）** 和 **Technical documentation（操作文档）**。官网使用实际的 `azure.microsoft.com` 对应页面，分别标注产品、定价、Offer 条款、区域可用性或支持入口的用途；操作文档保留 Microsoft Learn 等官方来源，并沿用该篇的核实日期。

官网公开价格不等于客户账单，产品介绍不等于当前订阅的资格或配额。出现官网、技术文档与客户实际协议适用范围不一致时，必须明确说明并核实，不能自行选择有利的解释。
