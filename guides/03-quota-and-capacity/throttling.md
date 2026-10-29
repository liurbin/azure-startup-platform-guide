---
title: "429限流：先分管理请求与业务调用"
applies_to:
  - "Azure Global"
  - "管理面与模型请求的限流分类"
last_verified: 2026-10-28
related:
  - guides/03-quota-and-capacity/quotas-and-limits.md
  - guides/03-quota-and-capacity/capacity.md
---

# 429限流：先分管理请求与业务调用

## 结论

429表示请求暂时不能按当前速度被处理，不等于“资源额度全用完”。先分清是在管理资源，还是在调用某个服务，再用错误说明、返回头和对应时间窗口判断，不能只看一分钟平均值。

## 典型问法

- ARM管理请求与模型推理都返回429，原因一样吗？
- 平均请求不高为什么还被限流？
- `max_tokens` 为什么与限流有关？
- 被拒请求、已用token和账单token有什么区别？
- 开启动态配额是否就能保证突发吞吐？

## 关键概念

- **ARM请求**：向Azure Resource Manager提交的资源管理操作，不是模型用户请求。
- **TPM／RPM**：每分钟token／请求限制；适用模型可能按比一分钟更短的窗口评估。
- **限流预估**：请求到达时估计处理量，不是最终账单用量。
- **有效上限**：此刻实际生效的请求限制，不一定与长期配置相同。
- **Dynamic quota／动态配额**：特定模型部署在额外容量允许时机会性获得更多吞吐，不是预订资源。

## 规则与事实

- **[ARM管理请求]** 限制可按订阅、租户、调用身份、区域和操作类型区分，资源提供程序还可有自己的限制；模型TPM不能解释这些管理请求。[来源](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/request-limits-and-throttling)
- **[ARM返回证据]** 管理请求的剩余量和Retry-After等响应信息用于解释限流与等待条件；具体错误要按返回的管理服务范围判断，不自行假设固定重试间隔。[来源](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/request-limits-and-throttling)
- **[Azure OpenAI Standard示例]** 配置的TPM/RPM、短时突发、临时有效上限调整及共享容量压力都可能参与429判断，应对照实际错误与有效限制，而不是统一申请更多quota。[来源](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/quota)
- **[上述模型限流示例]** 估算包含输入与`max_tokens`等请求参数；RPM按短窗口评估，因此分钟均值低于配置仍可能被限流。[来源](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/quota)
- **[上述请求计数边界]** 限流评估可以包含后来被拒或没有计费的请求；这不表示所有错误响应都必然重复计数，也不等于实际计费token。[来源](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/quota)
- **[Classic动态配额示例]** 文档所述Standard部署可在有额外容量时提高吞吐，额外量不可预测且调用仍按正常规则收费；文档属于classic体验，不能据此推断所有新门户/模型都支持。[来源](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/dynamic-quota)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 创建、列举资源或读管理指标时429 | ARM或资源提供程序请求限制 | 核对目标API、调用身份/范围、错误与返回头，不套模型限流指标 |
| 模型分钟均值低但仍429 | 突发、预估处理量或不同实际限制 | 比较请求发生窗口、分配量、错误和有效limit，不只看均值 |
| 配置没变，有效limit变低 | 适用Standard共享池的临时调整 | 对照实际limit头、配置与同期请求，不把单次未知头值当已确认显示缺陷 |
| 返回说明指向系统高需求/容量 | 可能是运行时共享能力紧张 | 保留完整说明、类型、区域和请求ID；持续问题与配置限额分别核实 |
| 响应头为负值、零或缺失 | 仅凭这一字段无法确定原因 | 记录实际API与时间，交叉核对错误、配置与请求结果；本库不宣称它必然是已知bug |
| 收到429但不知道有没有费用 | 限流数据与计费口径不同 | 本篇解释请求限制；实际费用以对应计量记录为准，不能由状态码下总额结论 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 所有429都能用提额解决 | 先分管理请求、分配限制与运行时条件 |
| `max_tokens`只有真的输出后才影响限制 | 在本篇模型示例中它会参与到达时估算 |
| 负值header必定是官方已知显示问题 | 没有适用证据时只保留异常观察，不造诊断 |
| 动态配额就是保证扩容 | 它是机会性能力，不可作为稳定承诺 |

## 需要准备的信息

- API/服务、请求类别、身份与资源范围
- 错误、状态、request ID及实际返回头
- 配置/有效限制、模型或操作类型与同一时间窗请求证据

## 不在本篇范围

- 配额维度、等级与分配：见[配额与限制](quotas-and-limits.md)。
- 创建或扩张分配失败：见[实时容量](capacity.md)。
- 重试、排队、并发器与业务代码实现不在本库范围。

## 来源

- [ARM管理请求限流](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/request-limits-and-throttling)
- [模型限流、估算与响应证据](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/quota)
- [Classic动态配额边界](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/dynamic-quota)
