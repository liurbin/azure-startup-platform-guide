---
title: "租户、订阅与资源：分别管什么"
applies_to:
  - "Azure Global"
  - "资源组织与管理范围"
last_verified: 2026-10-29
related:
  - guides/00-foundations/billing-hierarchy.md
  - guides/02-governance/identity/access-types.md
---

# 租户、订阅与资源：分别管什么

## 结论

租户是公司的身份目录，订阅是组织云资源的重要管理范围，资源组把需要一起管理的资源放在一起；它们不是三个不同名字的“账号”。先确认资源属于哪里，再判断谁能访问、什么规则生效；谁付钱则看另一套计费关系。

## 典型问法

- tenant、subscription、resource group 到底有什么区别？
- 我们需要几个订阅，什么时候再加管理组？
- 为什么换一个目录就找不到资源了？
- 完整资源 ID 怎么读，为什么不能只给名称？

## 关键概念

- **租户（tenant）**：保存用户、组和应用身份的 Microsoft Entra 目录，不是付款账户。
- **管理组（management group）**：把多个订阅放在一起应用共同治理规则的容器。
- **订阅（subscription）**：组织资源、分配管理权限和应用部分服务限额的范围。
- **资源组（resource group）**：订阅内相关资源的管理容器，通常按共同生命周期组织。
- **资源 ID**：资源的完整管理路径；显示名称相同不代表同一个对象。

## 规则与事实

- **[资源管理机制]** 管理组、订阅、资源组和资源构成常用管理层级；在较大范围设置的管理规则可以向子范围生效。[来源](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview)
- **[管理组治理]** 管理组用于把多个订阅组织到共同治理范围；层级应围绕实际治理需求，而不是机械复制公司组织图。[来源](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/resource-org-management-groups)
- **[资源组级资源]** 一个这类资源只能属于一个资源组，通常把一起部署、更新和删除的资源归为一组；同组资源可以位于不同区域，资源组自身的位置用于存放组的管理元数据。[来源](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview)
- **[订阅规划]** 订阅是治理、成本、安全和规模等管理边界，应按实际需求决定是否拆分，而不是套固定数量；一个订阅可以包含不同区域的资源，不必仅因区域不同就增加订阅。[来源](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/resource-org-subscriptions)
- **[范围标识]** 资源组级 ID 通常包含订阅、资源组、提供程序、类型和名称；订阅或管理组自身也有 ID，不应要求所有 ID 都包含资源组这一段。[来源](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)

## 如何判断

下面是条件化示例，不是按公司人数或产品数量规定组织结构；先写出需要独立的管理边界，再决定用哪一层承载。

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 登录成功但资源列表为空 | 当前目录或订阅筛选不同，也可能没有读取权限 | 门户“目录 + 订阅”先核对范围，再看目标资源的 IAM（访问控制）页面 |
| 同名资源有多份 | 位于不同订阅、资源组或资源类型下 | 打开资源的 JSON 视图，比较完整 ID，不只比较名称 |
| 小团队只有几项资源，不知道从几层开始 | 可能只是需要把相关资源分组，还没有明确的独立订阅边界 | 一起部署、更新、删除的资源先按共同生命周期考虑资源组；逐项核对权限、治理、成本或服务限制是否要求独立订阅，不因人数少就省略这些判断 |
| 开发与生产由不同人员管理，规则也不同 | 需要分别控制访问或治理，但未必每个差异都要求新订阅 | 先列清两边允许的动作与规则；资源组范围能够满足的可在该范围区分，确需独立订阅边界的再评估拆分，不能只改名称当作隔离 |
| 同一团队在多个区域使用资源 | 把区域误当成必须独立的订阅边界 | 不必仅因区域不同就拆订阅；若另有区域治理或规模需求，列明该需求后再判断 |
| 多个订阅反复需要同一套治理规则 | 出现跨订阅统一治理需求 | 把需要共同继承规则的订阅列为管理组的候选集合；不按部门名称机械复制组织图 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 一家公司必须只有一个订阅 | 数量取决于实际管理边界，本文不规定统一数量 |
| 资源组在哪里，组内所有数据就在哪里 | 管理容器位置不能证明每个服务的数据存放或处理范围 |
| AWS 或 GCP 的组织对象可逐个改名照搬 | 应比较各对象实际职责，而不是按名称寻找一一对应 |

## 需要准备的信息

- 已知租户、订阅和资源 ID；尚未确定的项注明未知
- 需要分开的环境、团队、权限或成本责任
- 当前目录、订阅筛选和访问身份

## 不在本篇范围

- 谁付款、发票归哪里：见[计费层级](billing-hierarchy.md)。
- 登录后能做什么、权限如何判断：见[访问类型](../02-governance/identity/access-types.md)。
- 组织级自动发订阅、网络和应用架构的具体实施不在本库范围。

## 来源

- [资源管理范围与资源组](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview)
- [管理组设计考虑](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/resource-org-management-groups)
- [订阅边界与多区域考虑](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/resource-org-subscriptions)
- [资源 ID 与授权范围格式](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)
