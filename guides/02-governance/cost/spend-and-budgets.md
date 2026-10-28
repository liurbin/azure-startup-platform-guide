---
title: "日常支出、预算与共享费用分摊"
applies_to:
  - "Azure Global"
  - "按协议支持范围进行成本分析"
last_verified: 2026-10-28
related:
  - guides/01-credits-and-billing/invoices.md
  - guides/02-governance/cost/unexpected-charges.md
---

# 日常支出、预算与共享费用分摊

## 结论

日常控费先要看清“谁在什么时间花了多少”，再设置有责任人接收的预算通知。预算不是自动停费开关；团队分摊也不等于改变供应商发票或能精确算出每个客户的账单。

## 典型问法

- 本月主要花在哪里，哪些费用属于哪个团队？
- actual cost 和 amortized cost 应该看哪个？
- 预算超了为什么还在运行？
- 没打标签，共享费用还能怎么分？

## 关键概念

- **Scope／分析范围**：选择哪部分计费或资源范围；能否支持该范围还取决于协议。
- **Actual cost／实际记账成本**：按费用记账方式展示，包括购买发生时的金额。
- **Amortized cost／摊销成本**：把适用预留或节省计划成本分配到受益期间与资源。
- **Budget／预算**：成本条件与通知的组合，不是默认资源关停机制。
- **分摊**：把共享费用归给内部团队的方法，必须保留依据和未能分配的部分。

## 规则与事实

- **[成本视图]** 结果随范围、时间、粒度、指标和过滤改变；比较两次成本前需要先对齐这些条件。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis)
- **[协议与范围]** 管理组等分析范围不是所有协议都支持，例如当前文档列明 MCA 订阅的管理组成本支持限制；不能因能看到资源层级就推断同样能查成本。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-work-scopes)
- **[预留/节省计划分析]** actual 与 amortized 表示方式不同，摊销可展示受益资源与未使用部分；支持范围按实际协议和购买类型核实。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/view-amortized-costs)
- **[预算能力]** 阈值可触发通知；资源不会仅因预算超限自动停止。action group（通知/动作组）只在文档支持的范围可关联，不能把配置存在当作通知已送达。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)
- **[支持的标签继承]** 成本标签继承作用于使用记录而不是修改资源本身；可更新当前月相应记录，但不等于追溯改写全部历史成本。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/enable-tag-inheritance)
- **[支持的 EA/MCA 成本分摊]** 分摊规则改变内部成本展示，不改变发票付款责任；购买项等存在不支持的类别，不能把所有费用都机械分配到应用。[来源](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/allocate-costs)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 团队报表总额不一致 | 范围、时间、指标或过滤不同 | 在 Cost analysis 对照同一组视图设置，先保留差异而不是修改数字 |
| 购买月成本突增 | 按actual显示了承诺购买 | 同时检查actual与amortized，分别解释现金/账单与受益期间 |
| 预算超限仍运行 | 预算通知与停用控制不同 | 查看预算条件、接收人及实际通知记录；是否另有动作机制单独确认 |
| 标签分摊缺少费用 | 未打标、继承范围不支持或没有对应资源级记录 | 检查实际使用记录，区分直接归属、规则分摊、估算与未分配残差 |
| 需要按客户核算 | 平台账单未提供完整客户维度 | 先明确可观察的归因信息；不能从共享资源或共享Key推造逐客户账单 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| Budget 就是金额硬上限 | 它的基本作用是监控与通知 |
| 打标签后所有过去费用会自动正确分摊 | 标签、继承和历史支持范围不同 |
| 分摊后付款责任也转给了另一个团队订阅 | 这是内部分析归属，不是改商业发票 |
| 预测金额就是最终账单 | 预测是计划参考，发票结算另有口径 |

## 需要准备的信息

- 协议、分析范围、期间、币种和观察时间
- actual/amortized、过滤及分摊方法
- 阈值、接收人、通知证据、响应责任人
- 未分配部分及估算标签，不把未知填成零

## 不在本篇范围

- 发票、用量明细和结算差异：见[发票](../../01-credits-and-billing/invoices.md)。
- 已出现不正常增长的调查：见[异常费用](unexpected-charges.md)。
- 自动停损、应用级计量、财务chargeback实施和承诺购买决策不在本篇范围。

## 来源

- [成本视图](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis)
- [范围的协议限制](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-work-scopes)
- [实际与摊销](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/view-amortized-costs)
- [预算与动作组范围](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)
- [标签继承](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/enable-tag-inheritance)
- [内部成本分摊](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/allocate-costs)
