---
title: "购买资格、订单与合同证据"
applies_to:
  - "Azure Global"
  - "商业采购与服务条款的适用范围"
last_verified: 2026-10-28
related:
  - guides/01-credits-and-billing/credits.md
  - guides/01-credits-and-billing/invoices.md
---

# 购买资格、订单与合同证据

## 结论

看得到产品或部署按钮，不代表公司已经具备购买资格，也不代表所有条款都已接受。先分清卖方、具体方案、付款范围与接受者；客户要的合同证据，还必须与这笔购买的实际协议和服务范围匹配。

## 典型问法

- 谁能接受私有报价，谁能真正购买？
- 为什么已经接受报价，仍用不了或看不到约定价格？
- Marketplace 产品适用微软条款还是卖方条款？
- 客户要 DPA、BAA 或审计报告，应该给哪类证据？

## 关键概念

- **Offer／plan**：具体销售产品及其价格、期限和交付方案。
- **Private offer／私有报价**：给指定客户的协商条件，不等于应用权限或资源配额。
- **DPA／数据保护附录**：描述供应商处理数据相关条款的合同文件，不等于创业公司对其客户的所有义务。
- **BAA／业务伙伴协议**：在美国 HIPAA 医疗法规适用关系下的合同安排，并非所有业务通用的认证。

## 规则与事实

- **[私有报价交易]** 账号准备、接受报价、购买/订阅是不同环节；接受报价本身不等于购买已完成。[来源](https://learn.microsoft.com/en-us/marketplace/private-offers-overview)
- **[按采购协议与范围]** 启用购买、接受私有报价和执行购买的角色要求分别核实；还可能受到 Marketplace 购买策略或私有市场限制。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/enable-marketplace-purchases)
- **[文档所述 MCA/EA 私有报价]** MCA 接受报价使用计费账户 Owner/Contributor，EA 使用具备写权限的 Enterprise Administrator；执行相应订阅中的购买还需订阅 Owner/Contributor等适用授权。接受者、购买者与启用采购策略的人不必是同一角色。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/enable-marketplace-purchases)
- **[Marketplace 订单]** 自动续订与取消后的服务行为要按实际订单及其方案判断；公开方案与私有报价的默认续订安排不应混用。[来源](https://learn.microsoft.com/en-us/marketplace/billing-invoicing)
- **[受 HIPAA 约束且使用范围内 Azure 服务的客户]** 官方说明 Microsoft 的 HIPAA BAA 通过 Product Terms 与所引用的 DPA 提供；这不能推出任意服务、任意合同或创业公司的整个产品已合规。[来源](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 能查看价格但无法购买 | 角色、付款范围、市场或采购策略不满足 | 在实际 offer/plan 的资格提示及计费角色中核对，不默认增加订阅 Owner 就能解决 |
| 接受后价格仍不对 | 账号、有效期或后续购买环节不匹配 | Private offer management 中核对目标计费账号、状态、有效期与对应订单 |
| 客户要“你们的 DPA” | 可能在问创业公司自身文件，不只是云厂商附件 | 先确认请求对象，再由合同责任人核对实际协议、版本和数据处理关系 |
| 需要 BAA 或框架适用证明 | 法规主体、服务范围与合同尚未匹配 | 对照官方 HIPAA 说明及所链接的范围清单，记录尚未成立的适用条件，不用资源区域代替合同判断 |
| 需要把厂商报告放进资料室 | 报告使用与转发条件尚未核实 | 对照该报告的实际获取/共享条款；未检查条款时，不把“找到了报告”当成“可自由转发” |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 接受私有报价就能调用对应服务 | 商业购买、技术授权和可分配能力仍是不同环节 |
| 微软的 DPA 能替代我们的全部客户合同 | 请求对象与各方责任需要分别确认 |
| 云厂商报告证明我的产品已获得相同认证 | 供应商证据不能替代客户自身的范围和控制验证 |
| 报告里没有列出某服务，内部签字就能解决 | 这是尚未解决的适用性问题，不是本文能作出的法律许可 |

## 需要准备的信息

- 产品、plan、卖方、订单或私有报价标识
- 协议、计费范围、接受者角色与交易状态
- 客户要什么证据、实际使用的服务范围与合同责任人

## 不在本篇范围

- Credits 是否能抵扣：唯一详细说明见[Credits](credits.md)。
- 发票、开票周期和支付金额核对：见[发票](invoices.md)。
- 本篇只提供合同证据判断边界，不提供法律意见、卖方上架、服务配置或报价谈判。

## 来源

- [私有报价的阶段](https://learn.microsoft.com/en-us/marketplace/private-offers-overview)
- [购买与接受报价的权限](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/enable-marketplace-purchases)
- [订单、续订与取消语境](https://learn.microsoft.com/en-us/marketplace/billing-invoicing)
- [HIPAA BAA 的合同与服务范围](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us)
