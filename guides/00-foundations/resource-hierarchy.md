---
title: "租户、订阅与资源：分别管什么"
applies_to:
  - "Azure Global"
  - "资源组织与管理范围"
last_verified: 2026-10-28
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
- **[资源组级资源]** 一个这类资源只能属于一个资源组；同组资源可以位于不同区域，资源组自身的位置用于存放组的管理元数据。[来源](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview)
- **[范围标识]** 资源组级 ID 通常包含订阅、资源组、提供程序、类型和名称；订阅或管理组自身也有 ID，不应要求所有 ID 都包含资源组这一段。[来源](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 登录成功但资源列表为空 | 当前目录或订阅筛选不同，也可能没有读取权限 | 门户“目录 + 订阅”先核对范围，再看目标资源的 IAM（访问控制）页面 |
| 同名资源有多份 | 位于不同订阅、资源组或资源类型下 | 打开资源的 JSON 视图，比较完整 ID，不只比较名称 |
| 想按环境或产品拆订阅 | 权限、治理、成本或服务限制的隔离需求不同 | 列明哪些边界必须独立，再按上面的层级确定管理范围；不是固定数量题 |
| 不确定要不要管理组 | 可能尚未形成跨订阅共同治理需求 | 对照实际订阅数量、共同规则及管理责任，而不是默认一开始就建立复杂层级 |

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
- [资源 ID 与授权范围格式](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)
