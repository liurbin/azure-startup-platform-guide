---
title: "谁付款、谁收发票：计费范围"
applies_to:
  - "Azure Global"
  - "按实际协议区分计费对象"
last_verified: 2026-10-28
related:
  - guides/01-credits-and-billing/invoices.md
  - guides/01-credits-and-billing/subscription-and-billing-transfer.md
---

# 谁付款、谁收发票：计费范围

## 结论

能管理云资源，不代表能看发票或改付款方式；这些权限由实际计费协议决定。先识别公司的协议和计费账户，再找订阅对应的账单范围，不要把订阅管理员当成当然的财务管理员。

## 典型问法

- 我是订阅 Owner，为什么看不到发票？
- 计费账户、billing profile、invoice section 分别是什么？
- 每个订阅都会单独开一张发票吗？
- 直接购买与通过 Partner 购买，界面为什么不同？

## 关键概念

- **计费账户（billing account）**：管理账单、付款和成本的商业关系对象。
- **协议类型**：决定计费对象与角色，例如 MCA（Microsoft Customer Agreement）、EA（Enterprise Agreement）或 MOSP（Microsoft Online Services Program）。
- **计费配置文件（billing profile）**：在 MCA 中组织付款与发票的范围。
- **发票分区（invoice section）**：在一个 MCA billing profile 内归类订阅费用的分组，不是独立租户。
- **CSP**：通过 Cloud Solution Provider 合作伙伴购买的渠道，不能当作另一种资源层级。

## 规则与事实

- **[按协议区分]** 门户中的计费账户类型与对象随协议不同；按量付费是一种价格方式，不足以单独确定你看到的是 MOSP 还是 MCA 计费对象。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/view-all-accounts)
- **[仅 MCA]** billing account 下可以有 billing profiles，profile 下的 invoice sections 用于组织账单中的订阅费用；这套对象不应直接套到所有协议。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-work-scopes)
- **[仅 MCA 计费授权]** 发票和付款相关权限由计费账户或 profile 等范围上的计费角色决定，与 Azure 资源管理角色不是同一套授权。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/understand-mca-roles)
- **[MPA 合作伙伴视图]** Microsoft Partner Agreement 的计费账户面向合作伙伴管理客户；不能把 Partner 界面和角色直接当作终端客户自己的账单权限。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/understand/mpa-overview)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 能管资源却看不到发票 | 有资源权限，但未取得对应计费范围的发票权限 | Cost Management + Billing → Billing scopes，核对协议类型与当前计费角色 |
| 找不到 billing profile | 不是 MCA 的对应视图，或该范围不可见 | 先看计费账户 Properties（属性），不要先按教程新建账户 |
| 多个订阅出现在同一发票 | 同属同一可合并开票的计费范围 | 在计费账户的订阅列表核对 profile 与 invoice section 归属 |
| 通过 Partner 购买却找不到直接付款入口 | 购买渠道与直接购买不同 | 根据实际订单和客户/Partner 计费关系确认账单提供方 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| tenant 就是开票主体 | 身份目录与商业计费对象不同 |
| Owner、Global Administrator 都能看所有账单 | 资源、目录与计费授权需要分别核对 |
| EA、MCA、CSP、按量付费是四个同层选项 | 它们混合了协议、渠道与价格方式，不能直接并列替换 |

## 需要准备的信息

- 计费账户类型与购买渠道
- 订阅及其当前计费归属
- 当前计费角色、希望查看或管理的具体对象

## 不在本篇范围

- 发票如何开具、下载和核对金额：见[发票](../01-credits-and-billing/invoices.md)。
- 更换付款责任或目录：见[订阅与计费转移](../01-credits-and-billing/subscription-and-billing-transfer.md)。
- 商业报价、协议谈判和价格承诺不是本篇能替客户决定的事项。

## 来源

- [识别计费账户类型](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/view-all-accounts)
- [计费与成本范围](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-work-scopes)
- [MCA 计费角色](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/understand-mca-roles)
- [MPA 合作伙伴计费视图](https://learn.microsoft.com/en-us/azure/cost-management-billing/understand/mpa-overview)
