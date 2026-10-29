---
title: "为什么有权限，仍被治理策略拒绝"
applies_to:
  - "Azure Global"
  - "治理策略的作用范围与评估结果"
last_verified: 2026-10-28
related:
  - guides/02-governance/policy/platform-controls.md
  - guides/02-governance/audit/change-history.md
---

# 为什么有权限，仍被治理策略拒绝

## 结论

有权限做一件事，不代表公司规则允许做成任何样子；Policy 就是约束资源状态或某些动作的治理规则。看到 `RequestDisallowedByPolicy`，先找出命中的规则与适用范围，不要把增加个人权限当作修复。

## 典型问法

- 为什么 Owner 也被 Policy 拦住？
- 哪条上级规则导致本次失败？
- audit、deny、modify、deployIfNotExists 有何不同？
- non-compliant 是否等于部署失败？
- exclusion 和 exemption 是同一种例外吗？

## 关键概念

- **Definition／定义**：规则检查哪些条件；initiative 是多条规则的组合。
- **Assignment／分配**：规则在哪个范围生效，以及采用什么参数。
- **Effect／效果**：只记录、拒绝、修改或检查关联对象等不同评估行为。
- **Exemption／豁免对象**：对某个分配记录特定范围的豁免及原因；与 `notScopes` 排除范围不是同一对象。

## 规则与事实

- **[策略作用范围]** 分配可以作用于管理组、订阅、资源组或资源，并覆盖对应子范围；个人有动作权限不等于不受资源状态规则约束。[来源](https://learn.microsoft.com/en-us/azure/governance/policy/overview)
- **[拒绝定位]** `RequestDisallowedByPolicy` 错误通常提供规则分配与定义标识，可据此核对真正生效的规则，而不是从资源显示名称猜测。[来源](https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/error-policy-requestdisallowedbypolicy)
- **[只记录与拒绝]** `audit` 记录不合规而不阻止该请求；资源管理模式中的 `deny` 可在请求送到资源提供程序前拒绝匹配的创建/更新。[来源](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-audit)；[来源](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deny)
- **[修改与关联对象检查]** `modify` 用于支持的属性修改，`deployIfNotExists` 评估相关资源并按条件部署；它们的身份与修复条件不同，不能把所有不合规视为同一种失败。[来源](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-modify)；[来源](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deploy-if-not-exists)
- **[评估时点]** 合规汇总会按不同触发条件更新；请求被拒与合规页面完成重新评估不是同一时刻。[来源](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data)
- **[例外机制]** exemption 的 `expiresOn` 可选，理由/审批等 metadata 是可记录的信息，不是所有字段都必填；`notScopes` 只是分配的排除范围，不自带同样的到期对象。[来源](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/exemption-structure)；[来源](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/assignment-structure)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| RequestDisallowedByPolicy | 匹配到了治理规则 | 从错误打开 assignment/definition，在 Policy 中核对scope、参数与effect |
| 当前资源组没分配却仍生效 | 上级分配向下适用 | 查看分配的原始scope，而不是只查看资源组本地规则 |
| 页面显示non-compliant但创建成功 | 可能是audit或其他非阻断评估 | 查看effect与本次操作状态，不能用合规摘要替代部署结果 |
| 修复后还显示旧状态 | 评估未更新，或条件仍未满足 | 比较最近评估时间与实际属性，不默认立即变绿 |
| 两个订阅同模板结果不同 | assignment、参数或例外不同 | 分别对照这些条件；不以模板相同推断治理环境相同 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| Owner 可以强行绕过deny | 动作权限不等于可忽略治理规则 |
| exemption和notScopes都有原生自动到期 | 二者机制不同，到期要核对具体对象 |
| non-compliant就是平台故障 | 先分effect、评估时间与实际请求结果 |

## 需要准备的信息

- 规则分配/定义标识、scope、参数与effect
- 原请求错误、关联ID和发生时间
- 已有豁免/排除信息、最近评估时间

## 不在本篇范围

- 服务内的内容控制和准入：见[平台控制](platform-controls.md)。
- 谁改过规则、何时生效的证据：见[变更历史](../audit/change-history.md)。
- 策略编写、修复执行、网络规则和具体产品配置不在本库范围。

## 来源

- [治理与资源授权的分工](https://learn.microsoft.com/en-us/azure/governance/policy/overview)
- [Policy拒绝标识](https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/error-policy-requestdisallowedbypolicy)
- [Audit](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-audit)
- [Deny](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deny)
- [Modify](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-modify)
- [DeployIfNotExists](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deploy-if-not-exists)
- [评估时点](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data)
- [Exemption](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/exemption-structure)
- [Assignment与notScopes](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/assignment-structure)
