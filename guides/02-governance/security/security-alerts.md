---
title: "安全告警和可疑访问：能确认什么"
applies_to:
  - "Azure Global"
  - "安全检测、访问暴露与证据边界"
last_verified: 2026-10-28
related:
  - guides/02-governance/audit/change-history.md
  - guides/02-governance/cost/unexpected-charges.md
---

# 安全告警和可疑访问：能确认什么

## 结论

安全告警表示有需要调查的信号，不等于已经证明入侵；费用上涨也不能单独证明凭据被滥用。先分开“检测到了什么、哪些对象受影响、哪些原因仍未知”，再把技术与费用证据交给对应责任人。

## 典型问法

- 高严重度告警是否就是被攻破了？
- 告警已关闭，是否说明访问已恢复安全？
- 发现Key公开了，能确认哪些影响？
- 删除用户角色后，为什么还要核对其他访问路径？
- 为什么同事能看到的告警我看不到？

## 关键概念

- **安全告警**：安全产品对可疑活动产生的检测信号，不是司法或财务裁定。
- **Severity／严重度**：检测产品给出的风险排序，不等于客户实际损失。
- **暴露／滥用**：凭据可被他人取得，与已经证实有人使用，是不同事实。
- **告警状态**：调查流程中的记录；点选状态不能证明底层访问或问题已经改变。

## 规则与事实

- **[安全产品示例]** Defender for Cloud 的告警提供活动时间、severity、status、描述及受影响对象；调查还要识别是否存在误报。[来源](https://learn.microsoft.com/en-us/azure/defender-for-cloud/manage-respond-alerts)
- **[告警响应证据]** 所引产品流程区分查看告警、调查、响应与更改状态；不能用已dismissed或其他关闭状态替代实际响应结果。[来源](https://learn.microsoft.com/en-us/azure/defender-for-cloud/manage-respond-alerts)
- **[该产品的访问权限]** 查看安全告警需要实际scope中的合适角色，例如Security Reader；别的产品权限或同事能看，不证明当前身份也能看。[来源](https://learn.microsoft.com/en-us/azure/defender-for-cloud/permissions)
- **[资源Key访问示例]** API key 可直接作为资源调用凭据；它与个人目录角色不是同一访问路径，不能只凭撤销某个用户的角色推断所有Key副本失效。[来源](https://learn.microsoft.com/en-us/azure/ai-services/authentication)
- **[支持双Key的资源示例]** 重新生成某个槽位会使该槽位旧值失效，也可能影响合法消费者；不能把移动存放位置或删除一个公开副本视为同样的失效证据。[来源](https://learn.microsoft.com/en-us/azure/ai-services/rotate-keys)

## 如何判断

| 现象 | 可能原因 | 怎么确认 |
|---|---|---|
| 收到高严重度告警 | 检测到高风险信号，影响尚待调查 | 在实际安全产品打开告警，记录范围、时间、实体和检测描述，区分事实与假设 |
| 告警不可见 | scope、筛选、权限或产品不同 | 核对通知来源和目标订阅，再查看该产品角色要求 |
| 已发现凭据公开 | 暴露事实成立，但使用者/费用影响未必已确认 | 交事件责任人决定及时处置；记录暴露窗口、消费者和后续访问证据，不等最终账单才响应 |
| 关闭告警后仍担心异常 | 状态记录与有效访问变化分开 | 对照后续调用/登录证据、实际处理结果与记录时间，不只看关闭按钮 |
| 金额与正常业务量不一致 | 正常消费者、应用放大或可疑访问都需区分 | 财务归因见[异常费用](../cost/unexpected-charges.md)，访问证据按本篇分类 |

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 任何429或5xx都是安全事件 | 状态码不是安全归因证据 |
| 没有告警就能证明没有异常访问 | 检测覆盖与日志可见性都有范围 |
| 用户角色没了，所有旧Key也失效 | 应分别识别实际访问路径 |
| Key换了，所有历史费用都应立即消失 | 访问变化和计费期间是不同问题 |

## 需要准备的信息

- 告警来源、标识、范围、活动时间和状态
- 已观察到的事实、可疑假设与业务影响
- 消费者/访问路径及已采取动作的结果，不只记录动作名称

## 不在本篇范围

- 调用/变更日志可以证明什么：见[变更历史](../audit/change-history.md)。
- 费用增长下钻与计量时间：见[异常费用](../cost/unexpected-charges.md)。
- 取证执行、凭据轮换步骤、隔离、漏洞修复和安全产品配置不在本库范围。

## 来源

- [告警信息、调查与状态](https://learn.microsoft.com/en-us/azure/defender-for-cloud/manage-respond-alerts)
- [告警读取角色](https://learn.microsoft.com/en-us/azure/defender-for-cloud/permissions)
- [资源Key调用身份示例](https://learn.microsoft.com/en-us/azure/ai-services/authentication)
- [Key旧值失效与消费者影响](https://learn.microsoft.com/en-us/azure/ai-services/rotate-keys)
