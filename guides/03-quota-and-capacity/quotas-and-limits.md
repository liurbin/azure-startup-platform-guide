---
title: "配额、服务限制与用量层级"
applies_to:
  - "Azure Global"
  - "额度机制；正文中模型配额为限定示例"
last_verified: 2026-10-28
related:
  - guides/03-quota-and-capacity/capacity.md
  - guides/03-quota-and-capacity/throttling.md
---

# 配额、服务限制与用量层级

## 结论

配额说明“允许申请或分配多少”，服务限制说明“这个能力有什么边界”，不等于已经用掉多少或现在能拿到多少容量。要先读清额度的对象、范围和单位；不能把某个模型的订阅池规则泛化到整个Azure。

## 典型问法

- 额度属于租户、订阅、区域还是某个部署？
- 为什么提额获批，Tier却没变？
- Global和Data Zone模型到底共享哪一池额度？
- 谁能看配额，TPM、RPM和PTU分别是什么？
- 提额申请没邮件，在哪里继续核对？

## 关键概念

- **Quota／配额**：对指定对象和范围分配的上限，部分可以申请调整。
- **Service limit／服务限制**：能力边界，是否可调整要按该服务维度核实。
- **Tier／等级**：模型示例中的额度分层，不是商业合同或购买容量的同义词。
- **TPM／RPM**：每分钟token与请求限制；不能直接相加，也不能不看模型就互换。
- **PTU**：模型预配处理能力的单位，不是token数量或请求次数。

例如“订阅总量、分配到部署的量、实际流量”是三种观察；读取时保留单位和时间。具体默认值、可申请量与等级清单不在本文冻结。

## 规则与事实

- **[通用额度框架]** Azure有多类可调整及不可调整额度，实际要按订阅、提供程序、位置与具体限制维度查看；默认值和可申请上限以当前页面为准。[来源](https://learn.microsoft.com/en-us/azure/quotas/quotas-overview)
- **[Azure OpenAI示例]** 该产品配额的最高范围为订阅而非租户；结论只限本例，不是所有Azure服务和接口的通则。[来源](https://learn.microsoft.com/en-us/azure/foundry/openai/quotas-limits)
- **[已接入订阅级管理的模型]** 同model/version的Global Standard跨区域共享订阅池，Data Zone Standard按数据zone共享；未接入模型可能仍按区域管理，应读Quota页的Scope列，而不按名称推断。[来源](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/quotas-limits)
- **[模型等级与提额]** 等级评估受使用、付款历史、offer等条件影响，且有自动升级策略；批准额外quota不等于等级升级，不能承诺增加消费就必然升级。[来源](https://learn.microsoft.com/en-us/azure/foundry/openai/quotas-limits)
- **[Azure OpenAI配额读取]** 订阅级Cognitive Services Usages Reader提供最小usage读取权限；资源组或单资源上的同名角色不足以读取订阅级Usages接口。[来源](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/quota)
- **[模型等级接口]** 官方提供订阅级`quotaTiers`只读查询，返回`currentTierName`、`assignmentDate`、`tierUpgradePolicy`等字段；当前接口带preview版本，具体版本和支持范围应按文档核实。[来源](https://learn.microsoft.com/en-us/azure/foundry/openai/quotas-limits)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 配额页为空或403 | 订阅不对或缺该usage读取范围 | 核对订阅IAM与实际Usages角色scope，不从空页推断额度为零 |
| 提额获批但Tier不变 | 批准的是附加额度 | 对照申请对象、单位、已批准总量与等级字段，分别记录 |
| 一区域分配后另一区域余额下降 | 可能使用同一订阅级池 | 比较Quota页Scope、model/version和type；Scope是具体区域时不直接套共享池 |
| 有订阅额度却运行中429 | 可分配额度与部署有效请求限制不同 | 先确认分配到哪个部署，再看[限流](throttling.md)，不把未分配额度当运行余量 |
| TPM、RPM、PTU混在一起 | 比较了不同维度 | 按具体模型/类型的单位记录，不依赖可能变化的门户标签位置 |
| 申请已提交却没收到邮件 | 请求入口、通知或处理状态未核实 | 按申请编号查看对应配额请求/支持记录及通知对象；提交不等于批准，也不承诺处理期限 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 所有Azure限额都按同一订阅池 | 先识别服务和维度，不能把模型例子扩展成平台通则 |
| 普通提额表就是Tier升级表 | 附加额度与等级状态分开 |
| 多订阅或多区域必然合规解决额度 | 真实池范围与使用条件需核实，不把拆分作为绕过限制的建议 |
| 限流图里的token就是财务账单token | 请求限制与计费含义不同，见限流篇 |

## 需要准备的信息

- 订阅、产品/模型版本/类型、区域或数据zone
- Scope、额度维度、单位、已分配与剩余、观察时间
- 等级/升级策略字段、申请编号和批准说明

## 不在本篇范围

- 额度足够但分配不到资源：见[实时容量](capacity.md)。
- 管理API或模型请求被429：见[限流](throttling.md)。
- 本篇不提供额度规避、容量承诺采购或服务配额修改的执行流程。

## 来源

- [通用额度机制](https://learn.microsoft.com/en-us/azure/quotas/quotas-overview)
- [模型等级、追加额度与preview查询](https://learn.microsoft.com/en-us/azure/foundry/openai/quotas-limits)
- [订阅级管理与Scope列](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/quotas-limits)
- [Quota读取权限与分配](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/quota)
