---
title: "人员离职、应用身份与所有权交接"
applies_to:
  - "Azure Global"
  - "人员与工作负载身份治理"
last_verified: 2026-10-28
related:
  - guides/02-governance/identity/access-types.md
  - guides/01-credits-and-billing/subscription-and-billing-transfer.md
---

# 人员离职、应用身份与所有权交接

## 结论

交接不只是禁用一个人的登录，还要知道谁继续负责关键账号、应用和商业关系。人员账号、应用身份与凭据各有生命周期；先分类型，才能判断离职、删除资源或凭据到期会影响什么。

## 典型问法

- Founder 或管理员离开，公司怎样接管？
- 外包到期，怎样确认访问不再需要？
- 删除应用 owner 会不会立刻让应用不能登录？
- 两类托管身份的生命周期一样吗？
- 外部流水线怎样不用长期应用秘密来证明身份？

## 关键概念

- **Owner／责任人**：可能指应用维护者、资源角色或计费责任人，不是处处相同的“所有者”。
- **Service principal／服务主体**：应用在某个目录中的运行身份，与创建它的人分开。
- **托管身份（managed identity）**：Azure 管理其凭据的工作负载身份，包括 system-assigned 和 user-assigned 两类。
- **联合身份（federation）**：信任外部身份提供者签发的token；OIDC是这类信任中使用的标准之一。
- **紧急访问账号**：正常管理员登录链路失效时恢复目录控制的身份，不能当普通共享账号。

## 规则与事实

- **[托管身份生命周期]** system-assigned 与所属资源绑定；user-assigned 是独立资源，可关联多个消费者，删除某个消费者不等于删除该身份。[来源](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
- **[支持的外部工作负载]** 联合身份可用外部token交换获得对 Entra 保护资源的访问token；信任成立后仍需对目标资源授予访问，不是自动获得资源管理员权限。[来源](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation)
- **[应用的联合凭据]** `issuer`（签发者）、`subject`（外部主体）和 `audience`（接收目标）等值需要与外部token匹配；具体平台必须满足相应支持条件。[来源](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust)
- **[人员访问撤销]** 禁用用户与撤销目录会话不能直接终止所有应用自己签发的会话，实际失效取决于token、应用和已有会话处理。[来源](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access)
- **[访问治理]** Access reviews 可复核组、企业应用和角色访问；PIM（特权身份管理）可提供按需、限时的角色激活，具体功能需匹配许可与角色范围。[来源](https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-overview)；[来源](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure)
- **[目录应急访问]** Microsoft 建议保留独立于日常联合身份链路的 cloud-only 紧急访问账号，并监控和验证其可用性；具体数量、认证和维护要求按当前官方指南核实。[来源](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 管理员即将离职 | 资源授权、应用维护与账单联系依赖个人 | 按资源 IAM、应用 Owners、计费与支持联系人分别列出责任；不是一键转“所有Owner” |
| 应用认证失败 | 凭据过期、主体禁用或信任不匹配等 | 对照应用/服务主体状态、凭据元数据和sign-in记录；不要仅凭owner被删除推导故障 |
| 删除一个资源后访问仍存在 | 使用了独立user-assigned身份或其他主体 | 对照真实身份类型和消费者，不只看原资源是否存在 |
| 想让流水线无长期秘密访问 | 联合信任与目标授权需要分别核实 | 对照实际平台支持条件、issuer/subject/audience及目标角色范围 |
| 找不到谁能应急接管 | 日常登录或责任人形成单点 | 核对紧急身份的独立性、使用记录、验证时间和负责保管的角色 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 删除应用owner等于立即删除应用身份 | 维护责任与运行身份是不同对象，应分别判断 |
| 所有托管身份随应用一起删除 | 两类托管身份的生命周期不同 |
| 外部token能交换成功就表示有资源权限 | 认证信任与目标授权分开 |
| 没有手工秘密就不用身份治理 | 仍需核查消费者、授权、责任与删除影响 |

## 需要准备的信息

- 人员/应用/托管身份的类型与对象标识
- 消费者、关键角色、商业与应用责任人
- 凭据到期/信任元数据、会话与访问评审记录

## 不在本篇范围

- 角色三要素、ID与拒绝分类：见[访问类型](access-types.md)。
- 跨目录与计费转移：见[订阅与计费转移](../../01-credits-and-billing/subscription-and-billing-transfer.md)。
- 联合凭据、MFA、PIM策略、Key或证书轮换的配置步骤不在本库范围。

## 来源

- [两类托管身份](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
- [工作负载联合身份](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation)
- [联合凭据信任字段](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust)
- [撤销用户与应用会话的边界](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access)
- [访问评审](https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-overview)
- [PIM](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure)
- [紧急访问治理](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access)
