---
title: "能登录却不能操作：区分访问权限"
applies_to:
  - "Azure Global"
  - "身份认证、资源授权与拒绝分类"
last_verified: 2026-10-28
related:
  - guides/02-governance/policy/policy-denials.md
  - guides/00-foundations/billing-hierarchy.md
---

# 能登录却不能操作：区分访问权限

## 结论

登录只证明“你是谁”，不证明“你能对哪个对象做什么”。看资源、读取数据、查看账单和分配权限要分别判断；遇到拒绝先读具体动作与范围，不要先把所有人都加成管理员。

## 典型问法

- 能登录，为什么看不到资源？
- 为什么 Owner 能管资源，却读不了数据或发票？
- 同样是 403，怎么知道是哪类拒绝？
- 应用的 client ID、object ID、principal ID 应该看哪个？
- 权限已经给了，为什么暂时仍失败？

## 关键概念

- **认证（authentication）**：确认调用者身份；令牌是用于该过程的凭据形式之一。
- **授权（authorization）**：决定该身份在具体范围能执行的动作。
- **Azure RBAC**：把“身份、角色、范围”组合起来的资源授权机制。
- **管理面／数据面**：管理资源配置，与读取服务里的实际数据，不是相同动作。
- **Client ID／对象 ID**：前者识别应用，后者定位目录中的具体对象；应用对象与其在租户中的服务主体不是同一个对象。

## 规则与事实

- **[资源授权]** 一个角色分配由 security principal（调用主体）、role definition（允许动作）和 scope（授权范围）组成；上级范围的角色可向下继承。[来源](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)
- **[角色动作]** `Actions` 描述管理面动作，`DataActions` 描述集成此机制的数据面动作；管理权限不能笼统等同于读写所有服务数据。[来源](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions)
- **[应用身份]** 应用注册对象与各租户中的 service principal（服务主体）有不同对象 ID；托管身份也通过服务主体获得授权，排查要记录真正调用主体。[来源](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals)
- **[角色分配权限]** 是否能给别人分配角色取决于 `Microsoft.Authorization/roleAssignments/write` 等实际授权，不能从“可以创建资源”推断。[来源](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting)
- **[近期角色变化]** 授予/撤销可能存在传播与令牌缓存影响；托管身份等场景还有不同缓存条件，不能统一承诺刷新后立即生效。[来源](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 登录后资源为空 | 目录/订阅筛选不同或缺读取范围 | 门户目录与订阅筛选，加目标范围 IAM → Check access |
| 错误含 AuthorizationFailed | 调用主体、被拒动作或授权范围不匹配 | 读取错误里的主体标识、action、scope，再对照有效角色 |
| 同事授错一个应用 ID | 把应用对象、client ID 与实际服务主体混用 | 在 Entra 的 App registrations 与 Enterprise applications 对照身份类型和对象 ID |
| 近期加角色仍失败 | 缓存、未激活权限或作用域错误 | 同时核对授予时间、激活状态和实际token主体，不用等待替代权限核对 |
| 错误明确指向策略或网络 | 不是普通资源角色缺失这一类问题 | 保留错误分类；Policy 见下文专篇，网络路径由网络责任人处理 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 403 就是需要订阅 Owner | 错误码不足以唯一确定拒绝来源 |
| Contributor 一定可以给别人授权 | 创建资源与修改角色分配是不同动作 |
| 应用注册的 object ID 就是运行身份 ID | 应先识别应用对象与实际调用服务主体 |
| Owner 看不到发票说明平台异常 | 发票属于独立计费授权，见计费层级 |

## 需要准备的信息

- 想做的动作、目标范围和完整错误
- 当前目录、调用主体类型及实际对象 ID
- 有效角色、继承来源、激活状态和变更时间

## 不在本篇范围

- Policy 拒绝与例外：见[策略拒绝](../policy/policy-denials.md)。
- 计费账户与发票角色：见[计费层级](../../00-foundations/billing-hierarchy.md)。
- 条件访问、MFA、安全组及服务内权限的具体配置不在本篇范围；本篇只帮助识别拒绝类型。

## 来源

- [资源授权的三要素](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)
- [管理与数据动作](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions)
- [应用对象与服务主体](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals)
- [权限、激活与传播排查](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting)
