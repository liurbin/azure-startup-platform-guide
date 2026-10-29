# Azure Startup Platform Guide

[默认入口 / English](README.md)

面向使用 **Azure Global** 的startup创始人、技术负责人、财务、Cloud Ops团队及其LLM Agent的平台知识参考库。原有22篇知识指南仍共用一套中文正文，不读中文的读者可使用支持翻译的Agent辅助阅读；「例行基线审计」作为同级分类，另有独立的中文与英文指令。

> **一句用法：把README网址和问题交给Agent，让它读取1～3篇相关guide，按提问语言或你指定的语言回答，保留适用条件、未确认事项和来源链接。**

翻译或按读者背景解释时，保留角色名、错误码和字段名的原文，必要术语首次出现就解释；不能把某个服务的例子变成整个Azure的通则。正文未回答的部分应明确说明缺口，不能用没有依据的断言补齐。

## 定位与边界

知识指南覆盖账号与计费、身份、费用、治理策略、平台安全与审计、配额、容量和支持，解释机制与判断条件，不是Agent执行规程。「例行基线审计」提供给用户自己智能体的高层只读指令，不提供数据连接、任务调度或自动整改工具。

每篇知识指南第一屏先用白话回答；事实前明确标记“通用机制”“某种协议”或“具体示例”。相关篇只补另一部分答案，不反复复制同一条政策。

知识指南不覆盖应用架构、具体服务的配置/部署/运维、网络配置、备份、域名与证书。审计指令可以提示关注网络、主机与备份等适用风险，但不提供专项实施步骤，也不代表知识正文已覆盖这些领域；其他Azure云环境不在范围内。

稳定机制可以直接从正文解释。余额、当时容量、客户协议资格和未明事故仍需实际账号或合同证据，不能虚构；来源用于追溯依据和查询动态信息，不要求每次概念问答都重读全部外部文档。

## 目录

| 分类 | Guide | 回答什么 | 完整URL |
|---|---|---|---|
| 基础 | [资源层级](guides/00-foundations/resource-hierarchy.md) | 各容器分别管什么，哪些管理边界支持分组或拆分。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/00-foundations/resource-hierarchy.md |
| 基础 | [计费层级](guides/00-foundations/billing-hierarchy.md) | 实际协议下由谁付款、哪些计费对象和角色决定访问。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/00-foundations/billing-hierarchy.md |
| 基础 | [资源提供程序注册](guides/00-foundations/resource-providers.md) | 注册报错究竟是登记、权限还是区域/接口不支持。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/00-foundations/resource-providers.md |
| Credits与计费 | [Credits](guides/01-credits-and-billing/credits.md) | 哪种权益、什么余额字段、哪些费用与到期条件适用。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/01-credits-and-billing/credits.md |
| Credits与计费 | [购买与条款](guides/01-credits-and-billing/purchases-and-terms.md) | 谁接受/购买报价，合同文件和报告去哪里找、怎样核对适用。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/01-credits-and-billing/purchases-and-terms.md |
| Credits与计费 | [发票](guides/01-credits-and-billing/invoices.md) | 开票范围、周期与用量明细如何解释应付金额。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/01-credits-and-billing/invoices.md |
| Credits与计费 | [订阅与计费转移](guides/01-credits-and-billing/subscription-and-billing-transfer.md) | 换付款人、换身份目录与移动资源有哪些不同。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/01-credits-and-billing/subscription-and-billing-transfer.md |
| 治理：身份 | [访问类型](guides/02-governance/identity/access-types.md) | 哪个调用身份、动作与授权范围解释本次访问拒绝。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/identity/access-types.md |
| 治理：身份 | [身份生命周期](guides/02-governance/identity/identity-lifecycle.md) | 人员、应用、托管身份与联合信任如何分类型交接。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/identity/identity-lifecycle.md |
| 治理：成本 | [支出与预算](guides/02-governance/cost/spend-and-budgets.md) | 日常成本怎么比较，预算通知和共享分摊能做什么。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/cost/spend-and-budgets.md |
| 治理：成本 | [异常费用](guides/02-governance/cost/unexpected-charges.md) | 从哪里定位上涨，怎样区分当前状态与计量时点。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/cost/unexpected-charges.md |
| 治理：策略 | [Policy拒绝](guides/02-governance/policy/policy-denials.md) | 哪条治理规则生效，评估效果与例外是什么意思。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/policy/policy-denials.md |
| 治理：策略 | [平台控制](guides/02-governance/policy/platform-controls.md) | 服务内容控制、滥用监控和功能准入为何不同于Policy。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/policy/platform-controls.md |
| 治理：安全 | [安全告警](guides/02-governance/security/security-alerts.md) | 告警或凭据暴露能证明什么，哪些影响仍未确认。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/security/security-alerts.md |
| 治理：审计 | [变更与审计证据](guides/02-governance/audit/change-history.md) | 管理变更、数据调用、LLM遥测和日志查询分别能追踪什么。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/02-governance/audit/change-history.md |
| 配额与容量 | [可用性](guides/03-quota-and-capacity/availability.md) | 实际上下文是否支持目标产品、版本和类型组合。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/03-quota-and-capacity/availability.md |
| 配额与容量 | [配额与限制](guides/03-quota-and-capacity/quotas-and-limits.md) | 允许量、单位、模型共享池和等级怎么区分。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/03-quota-and-capacity/quotas-and-limits.md |
| 配额与容量 | [实时容量](guides/03-quota-and-capacity/capacity.md) | 为什么允许量足够，创建或扩张时仍分配失败。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/03-quota-and-capacity/capacity.md |
| 配额与容量 | [429限流](guides/03-quota-and-capacity/throttling.md) | 管理API和模型请求为什么需要不同的限流判断证据。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/03-quota-and-capacity/throttling.md |
| 支持 | [通知与退役](guides/04-support/notices-and-retirements.md) | 未来哪些变更影响谁，谁应在何时行动。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/04-support/notices-and-retirements.md |
| 支持 | [服务健康](guides/04-support/service-health.md) | 公开、个性化和单资源健康各能说明什么。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/04-support/service-health.md |
| 支持 | [支持请求](guides/04-support/support-requests.md) | 实际问题应选什么支持路径、证据、严重度及跟进方式。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/04-support/support-requests.md |
| 例行基线审计 | [例行基线审计](guides/05-routine-baseline-audit/azure-baseline-audit.md) | 定期应检查哪些安全、费用、错误与警告事项，以及相应的证据要求和只读边界。 | https://github.com/liurbin/azure-startup-platform-guide/blob/main/guides/05-routine-baseline-audit/azure-baseline-audit.md |

维护规范见[AGENTS.md](AGENTS.md)与[CLAUDE.md](CLAUDE.md)。[问题集](scenarios/questions.md)和[覆盖表](scenarios/coverage.md)只供维护回归，不是第二套读者索引，也不证明真实租户验证。

**最后更新：2026-10-29**
