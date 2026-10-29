---
title: "Credits 余额、抵扣范围与到期"
applies_to:
  - "Azure Global"
  - "区分创业项目赞助额度与协议内抵扣权益"
last_verified: 2026-10-28
related:
  - guides/00-foundations/billing-hierarchy.md
  - guides/02-governance/cost/unexpected-charges.md
---

# Credits 余额、抵扣范围与到期

## 结论

Credits 是有适用范围和期限的费用抵扣权益，不是能支付所有产品的现金。先确认是哪种权益、绑定到哪里，再读余额与到期信息；“授予金额”“本月用量”和“当前剩余”不能互相代替。

## 典型问法

- 创业项目额度在哪里看，还剩多少？
- 有余额为什么仍要付款？
- 能否把权益用于另一个订阅或第三方模型？
- 用完或到期会自动扣卡，还是停服？

## 关键概念

- **Offer／权益方案**：规定资格、适用费用、期限及后续安排的条款。
- **Sponsorship／赞助额度**：指定项目下的抵扣权益，不应与所有 MCA 余额页或其他项目混用。
- **MCA credits**：Microsoft Customer Agreement 下分配到计费范围的权益；不同于资源所属订阅本身。
- **余额与授予金额**：余额是按相应页面定义可用的部分；授予金额是最初额度，不证明剩余多少。

## 规则与事实

- **[Microsoft for Startups 赞助方案]** 合格 Azure 消耗通过对应赞助订阅使用额度；非 Azure 产品、支持计划和 Marketplace 购买不能一概视为同样适用。[来源](https://learn.microsoft.com/en-us/startups/build/getting-started/use-startup-credits)
- **[创业项目的模型消费示例]** 模型是否覆盖要按销售与计费路线判断：当前项目文档区分 Azure 直接销售/计费的模型与 Partner、社区或 Marketplace 模型，不按模型厂商名字简单归类。[来源](https://learn.microsoft.com/en-us/startups/build/getting-started/foundry-model-sponsorship-coverage)
- **[仅 MCA 余额视图]** credits 分配到 billing profile（计费配置文件）；余额页展示的 Available balance 有自己的结算时点，不能把它直接称为所有创业项目的实时余额。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/benefits/credits/mca-check-azure-credits-balance)
- **[仅符合条件的 credit resource]** 资源详情的 `Amount` 是创建时授予总额，不是剩余余额；资源落在某个订阅内也不单独决定权益可抵扣的商业范围。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/benefits/credits/manage-azure-credits)
- **[带 spending limit 的订阅类型]** 额度耗尽可能触发停用；按量付费等类型不提供同样的 spending limit。到期、升级或付费继续使用要按实际 offer 判断，不能仅凭已经绑卡推断。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 不知道从哪个余额页开始 | 创业项目赞助、MCA 或其他权益被混为一类 | 先读实际 offer/项目激活信息；MCA 用 Billing scopes → 对应范围 → Payment methods → Azure credits，其他项目用该方案正式提供的权益入口 |
| 资源页 Amount 很大，但不知道剩余多少 | 看的是授予金额而非余额 | 区分字段名与页面范围，回到方案对应的余额/交易视图，不自行相减重建余额 |
| 能部署模型却出现额外付款 | 购买路线可能不符合该权益 | 核对具体产品、销售方、计费订阅与权益方案；模型示例按上面的赞助覆盖规则判断 |
| 希望分配给更多订阅或升级旧层级 | 使用了不同项目、加入批次或协议假设 | 确认当前权益方案和实际绑定，不默认存在统一层级或通用跨订阅转移能力 |
| 即将到期，担心业务中断 | 权益到期与订阅后续付费安排尚未核实 | 一起记录权益结束日、订阅状态、offer 和显示的继续使用路径，交权益/计费责任人确认 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 一个叫 Credits 的页面适用于所有项目 | 先分方案，再选入口，特别不能把 credit resource 当通用余额表 |
| 月用量低于初始额度，所以余额等于两者之差 | 时间、范围和累计口径可能不同，余额必须读实际来源 |
| 只要在同一模型目录中，抵扣资格就一样 | 技术可见性与商业计费路线不同 |
| 项目赠送额度用完必定自动扣卡 | 后续行为依实际 offer 与订阅状态确定，本文不作通用承诺 |

## 需要准备的信息

- 方案名称、实际加入/激活信息与绑定账号
- 计费范围、订阅、余额字段及观察时间
- 权益到期信息；有争议时提供产品和费用归属

## 不在本篇范围

- 计费账户与订阅的关系：见[计费层级](../00-foundations/billing-hierarchy.md)。
- 已出现费用增长的调查路径：见[异常费用](../02-governance/cost/unexpected-charges.md)，其中抵扣资格以本篇为准。
- 商业续期、补贴、项目升级和退款资格需要实际项目责任人确认，不能由本库批准。

## 来源

- [创业项目额度的使用范围](https://learn.microsoft.com/en-us/startups/build/getting-started/use-startup-credits)
- [创业项目模型赞助覆盖](https://learn.microsoft.com/en-us/startups/build/getting-started/foundry-model-sponsorship-coverage)
- [MCA 余额及其显示口径](https://learn.microsoft.com/en-us/azure/cost-management-billing/benefits/credits/mca-check-azure-credits-balance)
- [Credit resource 字段与适用范围](https://learn.microsoft.com/en-us/azure/cost-management-billing/benefits/credits/manage-azure-credits)
- [Spending limit 的适用订阅](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit)
