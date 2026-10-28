# 问题覆盖矩阵（仅维护回归）

本文件不是读者入口。**已覆盖**表示正文直接解释相应机制、条件或判断路径，不代表取得客户实时数据或执行成功；**部分**表示只提供部分答案或当前范围限制；**超出范围**表示不计划在本库补实施。主guide是主要答案归属，辅助链接仅补另一个边界，不要求遍历所有related。

| ID | 状态 | 主guide | 覆盖依据或限制 |
|---|---|---|---|
| Q001 | 已覆盖 | [资源层级](../guides/00-foundations/resource-hierarchy.md) | 租户、订阅、资源组概念与实际定位 |
| Q002 | 已覆盖 | [资源层级](../guides/00-foundations/resource-hierarchy.md) | 管理容器职责；未按固定规模给出订阅数量 |
| Q003 | 已覆盖 | [资源层级](../guides/00-foundations/resource-hierarchy.md) | 同名不等于同ID、目录和订阅筛选 |
| Q004 | 已覆盖 | [资源层级](../guides/00-foundations/resource-hierarchy.md) | 管理范围继承概念；具体Policy效果另由策略篇负责 |
| Q005 | 部分 | [资源层级](../guides/00-foundations/resource-hierarchy.md) | 有ID各层和例外说明，不是全部嵌套/扩展资源ID解析器 |
| Q006 | 已覆盖 | [计费层级](../guides/00-foundations/billing-hierarchy.md) | 资源授权与实际协议计费角色分离 |
| Q007 | 已覆盖 | [计费层级](../guides/00-foundations/billing-hierarchy.md) | MCA的account/profile/section与订阅关系，不套用全部协议 |
| Q008 | 已覆盖 | [提供程序](../guides/00-foundations/resource-providers.md) | 订阅注册、register/action与内置角色 |
| Q009 | 部分 | [Credits](../guides/01-credits-and-billing/credits.md) | MCA余额路径与字段明确；其他创业方案要匹配实际权益入口，不提供客户当前数值 |
| Q010 | 已覆盖 | [Credits](../guides/01-credits-and-billing/credits.md) | 余额、绑定、适用费用与方案差异 |
| Q011 | 部分 | [Credits](../guides/01-credits-and-billing/credits.md) | 解释spending limit分支，不穷举所有项目/offer的继续付费安排 |
| Q012 | 已覆盖 | [Credits](../guides/01-credits-and-billing/credits.md) | 抵扣资格唯一在Credits展开，采购篇只链接 |
| Q013 | 已覆盖 | [购买与条款](../guides/01-credits-and-billing/purchases-and-terms.md) | 区分MCA/EA接受者、订阅购买角色及采购策略 |
| Q014 | 已覆盖 | [发票](../guides/01-credits-and-billing/invoices.md) | 按协议找下载入口和角色，未知协议先识别 |
| Q015 | 已覆盖 | [发票](../guides/01-credits-and-billing/invoices.md) | 范围、时间、税、Credits和结算口径 |
| Q016 | 已覆盖 | [发票](../guides/01-credits-and-billing/invoices.md) | 费用字段与非资源级明细例外 |
| Q017 | 已覆盖 | [转移](../guides/01-credits-and-billing/subscription-and-billing-transfer.md) | 付款人、目录与资源移动是不同关系 |
| Q018 | 部分 | [转移](../guides/01-credits-and-billing/subscription-and-billing-transfer.md) | 目录角色与购买项边界明确；所有Credits/协议转换仍需实际方案结论 |
| Q019 | 已覆盖 | [访问类型](../guides/02-governance/identity/access-types.md) | 登录与资源授权、scope检查 |
| Q020 | 已覆盖 | [访问类型](../guides/02-governance/identity/access-types.md) | 管理面与数据面授权分开 |
| Q021 | 已覆盖 | [访问类型](../guides/02-governance/identity/access-types.md) | 按实际动作/错误分流，不凭403盲目增权 |
| Q022 | 部分 | [访问类型](../guides/02-governance/identity/access-types.md) | 区分app/client与服务主体ID；不穷举各产品身份字段UI |
| Q023 | 已覆盖 | [访问类型](../guides/02-governance/identity/access-types.md) | 传播、令牌、激活和作用域一起判断 |
| Q024 | 已覆盖 | [身份生命周期](../guides/02-governance/identity/identity-lifecycle.md) | 人员、应用和商业责任分类型交接 |
| Q025 | 部分 | [身份生命周期](../guides/02-governance/identity/identity-lifecycle.md) | 解释评审对象与证据，不提供完整跨应用访问评审实施 |
| Q026 | 已覆盖 | [身份生命周期](../guides/02-governance/identity/identity-lifecycle.md) | 维护owner、实际运行主体、秘密到期不能互相代替 |
| Q027 | 已覆盖 | [身份生命周期](../guides/02-governance/identity/identity-lifecycle.md) | 紧急身份独立性、监控与验证责任，不写固定动态数量或配置步骤 |
| Q028 | 已覆盖 | [支出与预算](../guides/02-governance/cost/spend-and-budgets.md) | 可比视图、范围、指标与归因 |
| Q029 | 已覆盖 | [支出与预算](../guides/02-governance/cost/spend-and-budgets.md) | 预算通知不等于自动停费 |
| Q030 | 已覆盖 | [支出与预算](../guides/02-governance/cost/spend-and-budgets.md) | 标签、支持协议下的分摊、估算与未分配残差 |
| Q031 | 已覆盖 | [支出与预算](../guides/02-governance/cost/spend-and-budgets.md) | actual/amortized及未使用部分，支持范围需匹配 |
| Q032 | 已覆盖 | [异常费用](../guides/02-governance/cost/unexpected-charges.md) | 用量时间与显示时点分开，不在多篇重复展开延迟规则 |
| Q033 | 已覆盖 | [异常费用](../guides/02-governance/cost/unexpected-charges.md) | VM仅作为Stopped/Deallocated收费含义示例，无配置步骤 |
| Q034 | 部分 | [异常费用](../guides/02-governance/cost/unexpected-charges.md) | PTU预配费有明确例子，其他具体hosting plan计费需其产品依据 |
| Q035 | 已覆盖 | [异常费用](../guides/02-governance/cost/unexpected-charges.md) | 找真实收费对象与计量期间，不假定删应用等于终止所有购买 |
| Q036 | 已覆盖 | [限流](../guides/03-quota-and-capacity/throttling.md) | 限流估算可包含未计费/被拒请求，不能推导全部错误响应的收费 |
| Q037 | 已覆盖 | [Policy拒绝](../guides/02-governance/policy/policy-denials.md) | 错误中assignment与definition定位 |
| Q038 | 已覆盖 | [Policy拒绝](../guides/02-governance/policy/policy-denials.md) | 动作授权与资源规则是两个条件 |
| Q039 | 已覆盖 | [Policy拒绝](../guides/02-governance/policy/policy-denials.md) | audit/deny/modify/deployIfNotExists、豁免与排除的机制区别 |
| Q040 | 已覆盖 | [平台控制](../guides/02-governance/policy/platform-controls.md) | 资源治理与服务内容控制的边界，具体Policy由专篇展开 |
| Q041 | 已覆盖 | [平台控制](../guides/02-governance/policy/platform-controls.md) | Limited Access的具体功能与普通使用区别，不泛化所有模型 |
| Q042 | 已覆盖 | [平台控制](../guides/02-governance/policy/platform-controls.md) | 修改内容控制与修改abuse monitoring分别核实 |
| Q043 | 已覆盖 | [安全告警](../guides/02-governance/security/security-alerts.md) | 例子中scope、实体、活动窗口和检测含义 |
| Q044 | 已覆盖 | [安全告警](../guides/02-governance/security/security-alerts.md) | 严重度与已证实入侵/损失不同 |
| Q045 | 已覆盖 | [审计证据](../guides/02-governance/audit/change-history.md) | 管理操作、caller/claims与证据范围 |
| Q046 | 已覆盖 | [审计证据](../guides/02-governance/audit/change-history.md) | 管理、服务数据面和采集/保留缺口 |
| Q047 | 已覆盖 | [审计证据](../guides/02-governance/audit/change-history.md) | 受支持Resource Graph属性变更的含义与边界，无查询实现 |
| Q048 | 部分 | [可用性](../guides/03-quota-and-capacity/availability.md) | 给当前能力表入口与查询维度，不冻结实时地区/模型清单 |
| Q049 | 已覆盖 | [可用性](../guides/03-quota-and-capacity/availability.md) | 公开能力表与订阅资格/实际组合分开 |
| Q050 | 已覆盖 | [可用性](../guides/03-quota-and-capacity/availability.md) | 明确模型例子中Global/Data Zone/Regional处理范围，不作为法律结论 |
| Q051 | 已覆盖 | [配额](../guides/03-quota-and-capacity/quotas-and-limits.md) | Azure OpenAI订阅范围与其他服务/ARM机制分开 |
| Q052 | 已覆盖 | [配额](../guides/03-quota-and-capacity/quotas-and-limits.md) | 等级条件、自动升级策略与提额增量不同 |
| Q053 | 已覆盖 | [配额](../guides/03-quota-and-capacity/quotas-and-limits.md) | 按已接入模型与Scope列区分共享池，不靠固定历史日期推断 |
| Q054 | 已覆盖 | [配额](../guides/03-quota-and-capacity/quotas-and-limits.md) | 最小usage角色与单位区别，删除未核实的标签页断言 |
| Q055 | 已覆盖 | [容量](../guides/03-quota-and-capacity/capacity.md) | 额度与当前可分配能力、例子与购买项分开 |
| Q056 | 已覆盖 | [容量](../guides/03-quota-and-capacity/capacity.md) | 按错误和约束分类，不把SkuNotAvailable唯一归为显式restriction |
| Q057 | 已覆盖 | [限流](../guides/03-quota-and-capacity/throttling.md) | 管理API/提供程序限流与模型运行时分开 |
| Q058 | 已覆盖 | [限流](../guides/03-quota-and-capacity/throttling.md) | 短窗口与均值不同，不冻结固定秒数 |
| Q059 | 已覆盖 | [限流](../guides/03-quota-and-capacity/throttling.md) | 移除未核实header已知bug，保留异常观察与受条件限制的dynamic示例 |
| Q060 | 已覆盖 | [服务健康](../guides/04-support/service-health.md) | 公开、个性化和单资源健康的分工 |
| Q061 | 部分 | [服务健康](../guides/04-support/service-health.md) | 可分类平台证据与未知，但应用配置/运行根因调查不在范围 |
| Q062 | 已覆盖 | [通知](../guides/04-support/notices-and-retirements.md) | 事件、截止要求、影响对象和接收责任；具体升级不覆盖 |
| Q063 | 已覆盖 | [支持](../guides/04-support/support-requests.md) | 问题类别、计划、严重度、实际影响与跟进证据 |
| Q064 | 超出范围 | — | 网络配置有意排除，不指向一篇也不回答网络配置的guide |
| Q065 | 超出范围 | — | 备份、域名证书、应用架构有意排除，不重新增篇 |

最后更新：2026-10-28。各题的“已覆盖”只在本文定义的知识参考层成立；没有执行客户查询、独立LLM盲测或生产环境验证。
