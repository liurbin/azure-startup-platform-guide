---
title: "通知、计划维护与退役：谁需要行动"
applies_to:
  - "Azure Global"
  - "预告类事件、受影响对象与联系人"
last_verified: 2026-10-28
related:
  - guides/04-support/service-health.md
  - guides/04-support/support-requests.md
---

# 通知、计划维护与退役：谁需要行动

## 结论

没有收到邮件，不代表没有需要处理的变更；收到通知，也不代表每个资源都受影响。把官方事件、实际使用版本和责任人对起来，才能知道谁要在什么时候做什么，而不是只转发一封邮件。

## 典型问法

- 同事收到退役邮件，我为什么没有？
- 哪里能确认具体截止时间和影响对象？
- Impacted Resources为空，是否可以不管？
- 计划维护与已经发生的故障如何分开看？

## 关键概念

- **Health advisory／健康建议**：可能包含需要客户行动的变更、退役或提醒。
- **Planned maintenance／计划维护**：预告的维护事件，不等于已经证实客户业务中断。
- **Retirement／退役**：某服务、版本或能力不再按原方式提供；具体行动依正式通知。
- **Impacted resources／受影响资源**：事件识别出的支持范围内对象清单，不是全平台绝对完整清单。

## 规则与事实

- **[服务通知类别]** Service Health通知可按服务问题、计划维护、健康建议和安全建议等类别区分，分类决定关注的是预告行动还是当前影响。[来源](https://learn.microsoft.com/en-us/azure/service-health/alerts-activity-log-service-notifications-portal)
- **[Health Advisory受影响清单]** Impacted Resources只覆盖受支持服务/功能的子集，空列表不能单独证明没有受影响对象。[来源](https://learn.microsoft.com/en-us/azure/service-health/impacted-resources-retirements)
- **[通知规则]** 健康通知的范围可按订阅或目录、服务、区域与类别选择；收到通知取决于规则和接收设置，不只看某个人是不是资源Owner。[来源](https://learn.microsoft.com/en-us/azure/service-health/alerts-activity-log-service-notifications-portal)
- **[通知接收能力]** Action group用于定义通知目标或动作，具备测试能力；保存配置与实际送达不是同一证据。[来源](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 收到退役或变更提醒 | 当前使用的产品/版本可能匹配事件 | 在官方Health advisory或服务通知核对对象、截止时间、要求与tracking ID |
| 影响列表为空 | 未覆盖该能力，或暂无识别对象 | 按实际资源/版本清单匹配事件条件，明确未知而非自动结案 |
| 没收到同事收到的通知 | 规则scope、筛选或接收目标不同 | 在Health alerts及实际action group核对当前状态和送达记录 |
| 邮件链接与门户信息不同 | 邮件时点、事件更新或通知来源需核实 | 以正式事件及其后续更新核对，不依赖邮件中的单个日期 |
| 维护时段恰好有业务故障 | 时间重合不证明因果 | 当前影响按[服务健康](service-health.md)对照，不把全部应用错误归因到维护 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 没邮件就没风险 | 主动核对正式通知与实际使用范围 |
| 影响清单空就无需行动 | 清单覆盖有限，要匹配事件条件 |
| 截止日期大概率会延期 | 以当前正式要求安排责任与时间，不预设延期 |
| 转发邮件就完成交接 | 还要明确受影响对象、行动责任和完成证据 |

## 需要准备的信息

- 正式事件/通知标识、最新更新时间与要求
- 产品/规格/API或模型版本、实际资源范围
- 责任人、接收设置、行动期限和尚未确认对象

## 不在本篇范围

- 正在发生的可用性影响：见[服务健康](service-health.md)。
- 通知不明确或需要支持跟进：见[支持请求](support-requests.md)。
- 具体版本升级、迁移、备份与回滚实施不在本库范围。

## 来源

- [通知类别和规则范围](https://learn.microsoft.com/en-us/azure/service-health/alerts-activity-log-service-notifications-portal)
- [受影响资源的覆盖限制](https://learn.microsoft.com/en-us/azure/service-health/impacted-resources-retirements)
- [通知目标与测试](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)
