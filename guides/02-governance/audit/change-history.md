---
title: "谁改了什么：审计记录与日志能证明什么"
applies_to:
  - "Azure Global"
  - "管理变更、数据访问与日志证据分类"
last_verified: 2026-10-28
related:
  - guides/02-governance/identity/access-types.md
  - guides/02-governance/security/security-alerts.md
---

# 谁改了什么：审计记录与日志能证明什么

## 结论

资源被修改时先查管理操作记录；数据被读取、模型被调用或谁查过日志，需要另外的相应记录。查不到不等于没发生，要一起说明采集范围、开始时间、保留期限和身份字段的限制。

## 典型问法

- 是谁修改或删除了资源，能看前后值吗？
- 为什么 Activity Log 找不到数据读取或模型调用？
- 日志能保存多久，历史还能补回来吗？
- 调用元数据、LLM正文与日志查询审计有什么区别？
- caller 是什么，能直接认定真实用户吗？

## 关键概念

- **Activity Log／活动日志**：Azure 管理面操作记录，不是全部数据调用流水。
- **Resource logs／资源日志**：具体服务运行或数据面记录，是否已采集与支持哪些字段需分别确认。
- **调用元数据／正文**：时间、状态、请求标识等，与prompt、模型回答、工具参数等内容不是同一种证据。
- **Correlation／request ID**：关联操作或请求的标识，不等于个人身份。
- **日志查询审计**：谁查了日志、查了什么范围的记录，不等于原业务请求日志。

## 规则与事实

- **[管理操作]** Activity Log 自动记录管理面事件，内置保留有限；延长可查询历史依赖相应导出与存储，当前期限看官方保留说明。[来源](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/activity-log)
- **[数据访问与服务运行]** 资源日志内容随服务和资源类型变化，通常需要相应诊断采集；不能用管理日志缺失排除所有数据面操作。[来源](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/data-sources)
- **[身份字段]** Activity Log 的 `caller` 可呈现邮箱、UPN或SPN等值，身份对象标识可能在claims中；不能把所有caller都按一个object ID解析。[来源](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/activity-log-schema)
- **[支持的资源变更]** Resource Graph 的变更记录可提供受支持管理资源的属性差异与变更信息；这不是恢复所有数据内容或所有历史版本的能力。[来源](https://learn.microsoft.com/en-us/azure/governance/resource-graph/changes/get-resource-changes)
- **[日志读取权限]** Log Analytics 的访问受工作区、资源上下文和表等实际配置影响；能读一个资源，不应推断可读同工作区所有团队的记录。[来源](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/manage-access)
- **[已启用的查询审计]** 日志查询审计可记录查询者、时间、查询文本和范围；该记录与业务请求记录分开，也不能证明后续所有导出行为。[来源](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/query-audit)
- **[LLM遥测的SDK示例，所引API视图含预发布说明]** `Microsoft.Extensions.AI` 的聊天遥测区分元数据与敏感输入/输出采集；这是特定SDK的行为，不能当作所有模型、网关与Agent默认不记录正文的保证。[来源](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.ai.opentelemetrychatclient.enablesensitivedata)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 资源配置或角色被改 | 管理面写入/删除 | 按资源与时间过滤Activity Log，核对操作、状态、caller与claims |
| 需要前后属性差异 | 现状不足以解释变化 | 对照支持的Resource Graph变更记录及其可查询期间，缺失部分标为未知 |
| 管理日志为空但数据发生变化 | 数据面事件、范围或保留问题 | 查看已有服务日志的类别、实际采集开始/保留与时间窗，不假定能补录过去 |
| 不知道LLM是否记了正文 | 诊断、SDK、网关或Agent各自采集行为不同 | 列明已有采集器、字段、目的、接收位置与读者；不把一个开关代表整条链路 |
| 想查谁看过日志 | 查询审计与业务审计不同 | 核对工作区是否已有查询审计、哪些字段和期间可见；不能从当前角色反推所有历史读取 |
| trace不完整或身份只显示共享主体 | 采样、链路或身份粒度有限 | 记录实际覆盖和可关联标识，不把样本当完整访问台账或强行认定个人 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| Activity Log 已开，所有调用都有记录 | 管理、数据面和应用遥测要分别核对 |
| 今天补开日志就能看昨天全部请求 | 缺少当时采集不能被当前配置替代 |
| 看到Success就能证明业务结果正确 | 它只在对应操作与日志范围内有意义 |
| 审计越完整就越需要记录全部prompt | 正文不是默认必需的责任追踪字段，目的、范围和读取风险需单独判断 |

## 需要准备的信息

- 事件对象、UTC时间窗、操作/请求标识
- 采集类别、开始时间、采样、保留、位置与读取范围
- 实际身份字段、已关联事实与不能证明的部分

## 不在本篇范围

- 身份对象和授权范围概念：见[访问类型](../identity/access-types.md)。
- 告警与可疑访问的调查边界：见[安全告警](../security/security-alerts.md)。
- 日志采集器、LLM正文开关、导出、留存配置和应用审计代码不在本库范围。

## 来源

- [Activity Log 范围与保留](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/activity-log)
- [管理与服务日志的区别](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/data-sources)
- [Caller与claims字段](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/activity-log-schema)
- [资源变更](https://learn.microsoft.com/en-us/azure/governance/resource-graph/changes/get-resource-changes)
- [日志访问范围](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/manage-access)
- [查询审计](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/query-audit)
- [特定SDK的元数据与正文区别](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.ai.opentelemetrychatclient.enablesensitivedata)
