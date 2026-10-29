---
title: "平台还是我的问题：区分健康状态"
applies_to:
  - "Azure Global"
  - "公开、订阅与单资源的健康证据"
last_verified: 2026-10-28
related:
  - guides/04-support/notices-and-retirements.md
  - guides/04-support/support-requests.md
---

# 平台还是我的问题：区分健康状态

## 结论

公开状态页正常，不能排除你的订阅或单个资源有问题；单个资源显示健康，也不证明整个产品能用。应分别看公开事件、订阅相关事件、资源健康和实际业务表现，结论只到证据支持的那一层。

## 典型问法

- Azure状态页全绿，我的业务为什么仍不可用？
- Azure Status、Service Health、Resource Health分别看什么？
- 如何区分平台原因、用户操作和未知？
- 平台显示恢复，为什么产品还没有恢复？

## 关键概念

- **Azure Status／公开状态**：面向公开、广泛影响事件的页面。
- **Service Health／服务健康**：与所用服务/区域相关的个性化健康事件视图。
- **Resource Health／资源健康**：具体资源当前与历史健康状态，不是端到端业务探测。
- **RCA/PIR／事后分析**：官方事件复盘材料；提供范围随事件与流程不同，不能预先保证每个症状都有。

## 规则与事实

- **[公开事件]** Azure Status用于公开广泛影响等特定场景；更多受影响客户的定向通信通过Service Health提供，公开绿灯不能证明所有客户都正常。[来源](https://learn.microsoft.com/en-us/azure/service-health/azure-status-overview)
- **[订阅/服务相关视图]** Service Health提供所用服务和区域的个性化问题、维护和健康建议；它与公开状态及单资源健康互补。[来源](https://learn.microsoft.com/en-us/azure/service-health/overview)
- **[具体资源]** Resource Health区分Available、Unavailable、Unknown和Degraded等状态，并可提供平台或非平台事件解释；状态只在该资源及支持信号范围内有意义。[来源](https://learn.microsoft.com/en-us/azure/service-health/resource-health-overview)
- **[业务影响]** 完整业务健康仍要用实际工作负载遥测和用户路径证明，不能由单个依赖的健康状态替代。[来源](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/observability)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 公开状态正常但单个资源异常 | 局部影响、用户操作或其他尚未知条件 | 对照相关Service Health与Resource Health的实际对象/时段 |
| 资源标为Unavailable/Degraded | 平台或非平台条件影响了该资源 | 读取资源健康的事件原因、支持信号与历史时间，不仅看颜色 |
| 资源标为Unknown | 当前证据不足以判断 | 保留未知并比较实际请求表现，不把Unknown当健康或必然平台故障 |
| 平台事件与业务错误同期 | 可能相关，但不自动等同 | 对照region、resource、发生/恢复时间及业务错误窗口 |
| 平台恢复后业务仍失败 | 应用、数据或依赖恢复可能滞后 | 分开记录平台恢复与用户路径恢复，交实际责任方继续调查 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 公开页绿就证明不是Azure | 公开页并不覆盖所有局部症状 |
| 单资源Available等于端到端服务正常 | 它不验证整个应用依赖链 |
| 平台有事件就必有赔偿或单独RCA | 事实、合同适用与支持结论要分别确认 |

## 需要准备的信息

- 订阅/资源、服务规格与区域
- 健康事件标识、状态、原因与时间线
- 实际业务影响、请求结果及其开始/恢复时间

## 不在本篇范围

- 尚未发生的维护、变更与退役提醒：见[通知与退役](notices-and-retirements.md)。
- 工单材料、资格和响应跟进：见[支持请求](support-requests.md)。
- 故障切换、网络修复、应用架构与业务恢复实施不在本库范围。

## 来源

- [公开状态的发布范围](https://learn.microsoft.com/en-us/azure/service-health/azure-status-overview)
- [健康视图的分工](https://learn.microsoft.com/en-us/azure/service-health/overview)
- [具体资源状态](https://learn.microsoft.com/en-us/azure/service-health/resource-health-overview)
- [业务健康与观测证据](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/observability)
