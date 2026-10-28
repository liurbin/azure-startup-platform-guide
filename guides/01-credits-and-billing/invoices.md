---
title: "发票金额与用量明细如何对账"
applies_to:
  - "Azure Global"
  - "按协议核对发票与用量数据"
last_verified: 2026-10-28
related:
  - guides/00-foundations/billing-hierarchy.md
  - guides/02-governance/cost/unexpected-charges.md
---

# 发票金额与用量明细如何对账

## 结论

发票回答“这个账期要付多少”，用量明细帮助解释费用来自哪里，两者不是同一张表。先对齐计费范围、账期、币种和费用类型，再核对金额；不要把当天成本图当成最终发票。

## 典型问法

- 发票在哪里下载，为什么同事能看我不能？
- 为什么成本分析比发票金额少？
- 每个订阅、每个 Marketplace 订单都单独开票吗？
- 明细没有 resourceId，是不是数据错了？

## 关键概念

- **Invoice／发票**：按协议和开票范围形成的应付账单，可能包含税与调整。
- **Usage / cost details／明细**：记录消费或购买的费用字段；能提供哪些字段取决于协议与数据集。
- **Meter／计费度量项**：描述收费对象及计量单位，不等于一个完整业务应用。
- **ChargeType**：特定明细架构里的费用分类字段，不能把发票上的所有税费与调整都自行当作它的枚举值。

## 规则与事实

- **[按计费协议]** 下载发票的入口和角色要求不同，应先识别计费账户类型，再使用对应路径。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/understand/download-azure-invoice)
- **[仅 MCA 开票范围]** 发票按 billing profile 生成，profile 下的 invoice sections 用于组织其中费用；不能据此推断每个订阅必有独立发票。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/understand/review-customer-agreement-bill)
- **[当前未结算成本]** 成本数据在发票生成前可能仍是估算，且成本视图不把 credits 当作同一套费用抵扣结果展示。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-cost-mgt-data)
- **[Usage details 数据集]** `ChargeType` 以及税前成本等字段有各自定义；某些费用不能归属单一资源，应按实际字段解释而不是强行补造 `ResourceId`。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields)
- **[Marketplace 开票]** 是否合并到 Azure 发票，以及月结或特定购买的次日开票，取决于协议、地区和产品计费方式；不能按“都在Azure购买”推断同一张票。[来源](https://learn.microsoft.com/en-us/marketplace/billing-invoicing)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| Invoices 页面不可见 | 协议或发票读取范围不对 | 先核对 billing account type，再在该范围的计费角色中确认访问 |
| 发票与成本分析不一致 | 范围、时间、税、Credits、购买或结算状态不同 | 对照同一账期的发票分项与明细字段，先标出各视图包含/排除的部分 |
| 明细没有 resourceId | 可能是购买、未使用权益或非资源级费用 | 查看产品、卖方、meter、ChargeType 和原数据架构，不按空字段判定免费 |
| 同一次采购出现不同时间的发票 | 不同计费部分采用不同开票周期 | 按订单与发票行项目核对，不仅比较总额与出具日期 |
| 想改开票资料或 PO 编号 | 需要协议和账单责任范围内的变更 | 在对应发票/计费属性中核对支持方式；历史票据能否更正交计费责任人处理 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 当前成本图应与最终发票即时相等 | 要先比较范围、时点和包含项目 |
| ChargeType 可以填入我认为合理的税费类型 | 应使用该数据集实际定义，发票分项另行核对 |
| 删除资源会抹掉其过去费用 | 发票核对用的是实际计费期间，不是资源当前是否存在 |

## 需要准备的信息

- 发票标识、账期、币种及计费范围
- 实际明细架构、相关产品/meter/ChargeType
- 成本视图的时间、过滤和结算状态；付款问题另附实际状态

## 不在本篇范围

- 计费对象和角色的概念：见[计费层级](../00-foundations/billing-hierarchy.md)。
- 定位哪种资源/用量造成上涨：见[异常费用](../02-governance/cost/unexpected-charges.md)。
- 本文不决定税务处理、历史发票更正资格或退款结果。

## 来源

- [发票下载与角色](https://learn.microsoft.com/en-us/azure/cost-management-billing/understand/download-azure-invoice)
- [MCA 发票](https://learn.microsoft.com/en-us/azure/cost-management-billing/understand/review-customer-agreement-bill)
- [成本数据与结算](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-cost-mgt-data)
- [Usage details 字段定义](https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields)
- [Marketplace 发票周期](https://learn.microsoft.com/en-us/marketplace/billing-invoicing)
