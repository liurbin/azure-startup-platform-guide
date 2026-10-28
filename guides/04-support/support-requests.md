---
title: "找谁支持、如何描述问题与跟进"
applies_to:
  - "Azure Global"
  - "按问题类别、计划与实际影响选择支持"
last_verified: 2026-10-28
related:
  - guides/04-support/service-health.md
  - guides/00-foundations/billing-hierarchy.md
---

# 找谁支持、如何描述问题与跟进

## 结论

支持请求要先说明“哪个范围、什么时候、发生什么、影响多大”，再选择匹配的问题类别和支持资格。提交成功不等于解决或获批；响应目标、可选严重度和后续配合条件要看实际计划，不从Credits或云消费推断。

## 典型问法

- 计费、订阅、配额和技术故障分别找哪里？
- 没有付费技术支持计划还能提交什么问题？
- Severity怎么选，能不能后续调整？
- 如何找到申请状态、补充证据或跟进？
- 买哪种支持计划，需要先比较什么？

## 关键概念

- **Issue type／问题类别**：计费、订阅管理、具体技术问题等，不等于严重度。
- **Severity／严重度**：按实际业务影响选择的响应优先级，不能代替技术错误码。
- **Support plan／支持计划**：规定技术支持覆盖和响应条件的商业权益。
- **工单ID／请求ID**：前者定位支持记录，后者帮助定位具体服务调用或管理操作，二者不同。

## 规则与事实

- **[Azure订阅管理支持]** 官方将计费、配额调整、账户转移列入订阅管理支持；技术问题需要相应支持计划，不能把“可提交账单问题”读成“所有技术问题免费”。[来源](https://learn.microsoft.com/en-us/azure/azure-portal/supportability/how-to-create-azure-support-request)
- **[创建请求的资源权限]** 对指定订阅创建支持请求需要Owner、Contributor、Support Request Contributor或相应自定义权限；涉及实际账单信息与账户变化还可能要求计费管理员。[来源](https://learn.microsoft.com/en-us/azure/azure-portal/supportability/how-to-create-azure-support-request)
- **[实际响应条件]** 可选严重度、响应时间与工作时段受支持计划、实际业务影响及适用地区影响；高严重度还可能要求持续配合，不能承诺一个跨客户固定时限。[来源](https://learn.microsoft.com/en-us/azure/azure-portal/supportability/how-to-create-azure-support-request)
- **[现有请求跟进]** Help + support的All support requests可查看记录和消息；严重度调整的处理方式取决于计划及是否已分配工程师，不保证每个请求都能自行任意提高。[来源](https://learn.microsoft.com/en-us/azure/azure-portal/supportability/how-to-manage-azure-support-request)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 不知道选技术还是计费 | 把症状、商业权益和资源错误混在一起 | 写明希望解决的具体问题；付款/权益归实际计费关系，服务失败按对应产品技术类别 |
| 无法提交technical request | 计划、角色或目标范围不满足 | 在正式支持入口核对选用订阅、计划和角色，不直接增加全部管理员权限 |
| 提交后无邮件 | 通知、筛选或记录状态未确认 | 按工单ID查看All support requests、时间过滤、消息与联系人 |
| 需要提高严重度 | 实际生产影响扩大或没有可用替代 | 在现有记录更新影响及开始时间，按官方管理流程确认能否调整 |
| 问“支持值不值得买” | 响应需要与现有覆盖尚未比较 | 列服务时段、停机影响、内部能力和实际报价，再看当前计划条款；本文不报统一价格 |
| 客户通过Partner购买 | 合同与联系责任可能不同 | 依据实际采购关系确认第一联系人；不假定Azure门户就是所有项目/渠道支持入口 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| Credits多就一定有更高级技术支持 | 费用权益与支持计划分别核对 |
| Severity是想快一点就能随便选 | 它应匹配实际影响与配合能力 |
| 只给一张报错截图就足够定位 | 还需要具体范围、时间、错误和请求标识 |
| 工单已关闭代表原问题一定修好 | 要对照实际结果与未完成事项，不只看流程状态 |

## 需要准备的信息

- 问题类别、目标订阅/资源、服务或具体申请
- 发生时间与时区、错误、请求/关联ID、已有工单ID
- 业务影响、可用替代、联系人和支持计划/购买渠道

## 不在本篇范围

- 当前平台与资源健康证据：见[服务健康](service-health.md)。
- 计费账户与角色概念：见[计费层级](../00-foundations/billing-hierarchy.md)。
- 技术实施、合同谈判、Partner交付RACI、补贴审批、退款或SLA赔偿裁决不在本篇范围。

## 来源

- [支持类别、角色与响应条件](https://learn.microsoft.com/en-us/azure/azure-portal/supportability/how-to-create-azure-support-request)
- [查看请求、补充消息与严重度调整](https://learn.microsoft.com/en-us/azure/azure-portal/supportability/how-to-manage-azure-support-request)
