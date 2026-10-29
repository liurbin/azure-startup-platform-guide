---
title: "换付款人、换租户与移动资源有什么不同"
applies_to:
  - "Azure Global"
  - "按源目标协议与身份依赖区分转移类型"
last_verified: 2026-10-28
related:
  - guides/00-foundations/billing-hierarchy.md
  - guides/02-governance/identity/identity-lifecycle.md
---

# 换付款人、换租户与移动资源有什么不同

## 结论

换谁付款、换资源信任的身份目录、把资源移到另一个容器，是三种不同的事。先说清要改变哪一项，再查实际协议支持的路径；不能保证权益、身份与订单都自动跟着订阅走。

## 典型问法

- 从 CSP 换到直接购买，是不是要重建资源？
- 只换账单所有者，会影响团队访问吗？
- 换租户后 RBAC 和托管身份会怎样？
- Credits、预留、节省计划与 Marketplace 订单能一起转吗？

## 关键概念

- **计费所有权转移**：改变订阅或购买项由哪个计费范围承担费用。
- **目录转移**：改变订阅信任的 tenant（身份目录），不只是改付款资料。
- **资源移动**：在支持的资源组/订阅之间改变管理归属，不等于迁应用数据。
- **源/目标协议**：转移前后真实协议与渠道；“转到正式账号”不足以唯一确定流程。

## 规则与事实

- **[产品计费转移]** 支持路径按源/目标协议及产品类型区分；有的可转移计费，有的需要资源移动，不能把 MOSP 专属流程当作所有协议的操作方式。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/subscription-transfer)
- **[订阅目录转移]** 原目录中的 Azure 角色分配会被永久删除；自定义角色和托管身份等依赖需按类型重新处理，不能只在新目录“刷新登录”恢复。[来源](https://learn.microsoft.com/en-us/azure/role-based-access-control/transfer-subscription)
- **[支持移动的资源]** 跨订阅移动要求源/目标满足同一目录、活动状态、支持的资源类型与依赖等条件；目录转移和资源移动不是同一个动作。[来源](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription)
- **[购买项与合同]** 支持计划不能随产品转移；预留与节省计划存在路径例外，Marketplace SaaS 也可能需单独处理。应按转移矩阵逐项确认，不能把“订阅能转”读成“所有购买都能转”。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/subscription-transfer)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 只想换公司付款范围 | 可能只需要计费路径变化 | 记录当前/目标协议、渠道和计费对象，按官方转移矩阵确认具体支持路径 |
| 转移后团队失去资源访问 | 同时发生了目录变化 | 对照转移记录和新目录身份，区分旧角色删除与普通权限传播 |
| 按钮不可用或客户说“只能迁资源” | 实际协议/状态可能不支持所选计费转移 | 核对精确的源→目标类型，不仅比较“都是Azure订阅” |
| 担心 Credits 或订单丢失 | 权益与产品的转移规则不同 | 单列实际权益、购买项、支持与承诺，分别核对；没有明文支持的项保持待确认 |
| 资源类型不支持移动 | 存在依赖或平台限制 | 按官方支持列表与源/目标条件判断，不用改账单来假装完成资源迁移 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 转移账单一定换 tenant | 先区分真正选择的转移类型，部分流程也可组合两项 |
| 换目录后原身份授权都在 | 主体和授权依赖需要按官方影响表处理 |
| 订阅能转就表示所有权益跟随 | 需要逐项确认，没有统一保留承诺 |

## 需要准备的信息

- 当前和目标协议、渠道、计费范围与目录
- 订阅状态、实际想改变的关系
- 资源依赖、身份/自动化、权益和订单清单

## 不在本篇范围

- 协议计费对象如何识别：见[计费层级](../00-foundations/billing-hierarchy.md)。
- 员工或应用身份的长期交接：见[身份生命周期](../02-governance/identity/identity-lifecycle.md)。
- 具体服务迁移、数据搬迁、重建与切换实施不在本库范围。

## 来源

- [跨协议、产品和支持计划转移](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/subscription-transfer)
- [目录转移的角色与身份影响](https://learn.microsoft.com/en-us/azure/role-based-access-control/transfer-subscription)
- [资源移动条件](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription)
