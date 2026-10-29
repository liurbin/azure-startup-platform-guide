---
title: "购买资格、订单与合同证据"
applies_to:
  - "Azure Global"
  - "商业采购与服务条款的适用范围"
last_verified: 2026-10-29
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
- 客户要 DPA、BAA 或审计报告，去哪里找、怎样确认适用？

## 关键概念

- **Offer／plan**：具体销售产品及其价格、期限和交付方案。
- **Private offer／私有报价**：给指定客户的协商条件，不等于应用权限或资源配额。
- **DPA／数据保护附录**：描述供应商处理数据相关条款的合同文件，不等于创业公司对其客户的所有义务。
- **BAA／业务伙伴协议**：在美国 HIPAA 医疗法规适用关系下的合同安排，并非所有业务通用的认证。
- **Service Trust Portal／服务信任门户**：Microsoft 提供云服务审计报告和合规资料的入口；资料的服务范围、期间与访问条件需分别核对。

## 规则与事实

- **[私有报价交易]** 分开接受与购买的流程中，单独接受报价不等于完成购买；符合条件的报价也可能通过 single-click purchase（单击购买）一起提交接受与购买，不能把分步流程套到所有报价。[来源](https://learn.microsoft.com/en-us/marketplace/private-offers-overview)
- **[按采购协议与范围]** 启用购买、接受私有报价和执行购买的角色要求分别核实；还可能受到 Marketplace 购买策略或私有市场限制。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/enable-marketplace-purchases)
- **[分步流程中的 MCA/EA 私有报价]** MCA 接受报价使用计费账户 Owner/Contributor，EA 使用具备写权限的 Enterprise Administrator；订阅中的购买通常还需订阅 Owner/Contributor，VM 软件预留购买则核对 Owner 或 Reservation Purchaser（预留购买者）等适用授权。接受者、购买者与启用采购策略的人不必是同一角色。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/enable-marketplace-purchases)；[来源](https://learn.microsoft.com/en-us/marketplace/private-offers-overview)
- **[单击购买支持的报价]** 提交确认不等于所有产品均已购买成功；需分别看产品状态、开始日期与供应商后续接入要求，不能把购买成功当成软件已可使用。[来源](https://learn.microsoft.com/en-us/marketplace/private-offers-single-click-purchase)
- **[Marketplace 订单]** 自动续订与取消后的服务行为要按实际订单及其方案判断；公开方案与私有报价的默认续订安排不应混用。[来源](https://learn.microsoft.com/en-us/marketplace/billing-invoicing)
- **[Marketplace 产品条款]** 发布者可采用标准合同、带修订的标准合同或自定义合同；具体条款可从产品页的 Legal Agreement（法律协议）入口核对，不能仅凭 Microsoft 代收费用就推断所有产品适用同一合同。[来源](https://learn.microsoft.com/en-us/marketplace/legal-contracts)
- **[受 HIPAA 约束且使用范围内 Azure 服务的客户]** 官方说明 Microsoft 的 HIPAA BAA 通过 Product Terms 与所引用的 DPA 提供；这不能推出任意服务、任意合同或创业公司的整个产品已合规。[来源](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us)
- **[Microsoft 云服务报告]** 服务信任门户提供审计报告等资料，可按云服务与日期筛选；部分资料需要组织账号登录并接受保密或许可条款，受限资料还取决于权限。不同审计覆盖的服务可能不同，获取报告不等于已经证明所用服务在范围内。[来源](https://learn.microsoft.com/en-us/compliance/assurance/stp-get-started)；[来源](https://learn.microsoft.com/en-us/azure/compliance/offerings/cloud-services-in-audit-scope)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 能查看价格但无法购买 | 角色、付款范围、市场或采购策略不满足 | 在实际 offer/plan 的资格提示及计费角色中核对，不默认增加订阅 Owner 就能解决 |
| 接受后价格或可用状态仍不对 | 账号、有效期、购买结果或开始日期不匹配 | Private offer management 中核对目标计费账号、流程类型、有效期与各产品订单状态；若购买已成功，再核对开始日期与供应商接入要求，不重复购买已成功的产品 |
| 不知道 Marketplace 采用谁的条款 | 把采购/计费关系与产品合同混为一类 | 对照产品页 Legal Agreement 中的合同、修订及报价附件，核对实际卖方与方案，不把标准合同、卖方合同和 Microsoft DPA 当成同一文件 |
| 客户要“你们的 DPA” | 可能在问创业公司自身文件，不只是云厂商附件 | 先确认请求对象；若要 Microsoft 文件，从[官方 DPA 入口](https://aka.ms/dpa)核对版本与语言，再与实际协议匹配；若要创业公司自己的文件，交自身合同责任人处理 |
| 需要 Microsoft BAA 或服务适用证明 | 法规主体、服务范围与合同尚未匹配 | 从[官方 HIPAA 说明](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us)核对合同承载方式，查看[BAA 入口](https://aka.ms/baa)、[Product Terms](https://www.microsoft.com/licensing/docs/view/Product-Terms)及[服务范围入口](https://learn.microsoft.com/en-us/azure/compliance/offerings/cloud-services-in-audit-scope)；不把一份 BAA 当作全部业务合规的证明 |
| 需要云厂商审计报告或认证证书 | 尚未找到对应服务与期间的证据 | 从[服务信任门户](https://aka.ms/STP)按云服务和日期筛选，核对报告/证书版本、覆盖服务与期间；部分内容需要登录或接受相关条款，不能保证匿名下载 |
| 需要把厂商报告放进资料室 | 获取与转发是不同条件 | 对照该资料实际保密、许可及共享条款；未检查条款时，不把“找到了报告”当成“可自由转发” |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 接受或提交购买就能调用对应服务 | 先确认具体流程和各产品购买结果；商业购买、技术授权和可分配能力仍是不同环节 |
| 官方文件入口里的最新版本必定适用于旧订单 | 应核对实际合同及适用版本，不以下载日期代替适用性判断 |
| 微软的 DPA 能替代我们的全部客户合同 | 请求对象与各方责任需要分别确认 |
| 云厂商报告证明我的产品已获得相同认证 | 供应商证据不能替代客户自身的范围和控制验证 |
| 报告里没有列出某服务，内部签字就能解决 | 这是尚未解决的适用性问题，不是本文能作出的法律许可 |

## 需要准备的信息

- 产品、plan、卖方、订单或私有报价标识
- 协议、计费范围、接受者角色与交易状态
- 客户要谁的什么证据、实际使用的服务范围与合同责任人
- 文件/报告的标题、版本、覆盖期间、获取与共享条件；适用性未确认的部分保留为未知

## 不在本篇范围

- Credits 是否能抵扣：唯一详细说明见[Credits](credits.md)。
- 发票、开票周期和支付金额核对：见[发票](invoices.md)。
- 本篇只提供合同证据判断边界，不提供法律意见、卖方上架、服务配置或报价谈判。

## 来源

- [私有报价的阶段](https://learn.microsoft.com/en-us/marketplace/private-offers-overview)
- [符合条件的单击购买、结果与激活边界](https://learn.microsoft.com/en-us/marketplace/private-offers-single-click-purchase)
- [购买与接受报价的权限](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/enable-marketplace-purchases)
- [订单、续订与取消语境](https://learn.microsoft.com/en-us/marketplace/billing-invoicing)
- [Marketplace 法律合同与产品页入口](https://learn.microsoft.com/en-us/marketplace/legal-contracts)
- [HIPAA BAA 的合同与服务范围](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us)
- [服务信任门户的资料、筛选与访问条件](https://learn.microsoft.com/en-us/compliance/assurance/stp-get-started)
- [云服务审计与 BAA 范围入口](https://learn.microsoft.com/en-us/azure/compliance/offerings/cloud-services-in-audit-scope)
- [Microsoft DPA 官方文件入口](https://aka.ms/dpa)
- [Microsoft HIPAA BAA 入口](https://aka.ms/baa)
- [Microsoft Product Terms](https://www.microsoft.com/licensing/docs/view/Product-Terms)
- [Microsoft 服务信任门户](https://aka.ms/STP)
