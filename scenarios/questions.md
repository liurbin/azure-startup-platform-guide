# 常见平台问题清单（维护与回归测试）

> 本文件不是读者入口。这是按新定位组织的65道维护回归问题，不是旧版68题的一对一迁移记录。本轮保留所有题号，只将Q053、Q054、Q057～Q059中冻结日期、门户位置或未经核实的诊断表述改为对应机制问题；不新增读者索引。

| ID | 类别 | 问题 |
| --- | --- | --- |
| Q001 | 基础 | 我的资源属于哪个 tenant、subscription 和 resource group？ |
| Q002 | 基础 | management group、subscription、resource group 分别控制什么？ |
| Q003 | 基础 | 为什么同名资源在门户里找不到？ |
| Q004 | 基础 | Azure RBAC 或 Policy 会从哪里继承？ |
| Q005 | 基础 | resource ID 中每一段代表什么？ |
| Q006 | 计费 | 为什么我是 subscription Owner 仍看不到发票？ |
| Q007 | 计费 | billing account、profile、invoice section 和 subscription 如何对应？ |
| Q008 | 基础 | MissingSubscriptionRegistration 是什么，谁能注册 provider？ |
| Q009 | Credits | startup credits 还剩多少、何时到期？ |
| Q010 | Credits | 为什么有 credits 仍然出现信用卡扣款？ |
| Q011 | Credits | credits 到期或用尽后订阅和资源会怎样？ |
| Q012 | 购买 | Marketplace 或第三方费用能否使用 credits？ |
| Q013 | 购买 | 谁可以接受 private offer 或购买 Marketplace plan？ |
| Q014 | 发票 | 在哪里下载发票和用量明细？ |
| Q015 | 发票 | 为什么 Cost Analysis 和发票金额不一致？ |
| Q016 | 发票 | 如何把发票行项目追到 subscription、resource 和 meter？ |
| Q017 | 转移 | 计费所有权转移、换 tenant 和资源移动有什么区别？ |
| Q018 | 转移 | subscription 转移后 RBAC、credits 和 Marketplace 订单会怎样？ |
| Q019 | 身份 | 能登录 Azure 为什么看不到资源？ |
| Q020 | 身份 | 为什么 Owner 能管理资源却不能读数据？ |
| Q021 | 身份 | 403 是 RBAC、data plane、Policy、billing 还是网络拒绝？ |
| Q022 | 身份 | service principal 和 managed identity 应该查看哪个 object ID？ |
| Q023 | 身份 | 权限刚授予为什么仍然 AuthorizationFailed？ |
| Q024 | 身份 | 创始人或关键管理员离职前要交接哪些 Azure 所有权？ |
| Q025 | 身份 | 如何定期发现 guest、顾问或员工的多余权限？ |
| Q026 | 身份 | 应用 owner 离职或 secret 到期会造成什么影响？ |
| Q027 | 身份 | 为什么需要紧急访问账号以及如何确认它可用？ |
| Q028 | 成本 | 本月 Azure 花了多少，主要花在哪里？ |
| Q029 | 成本 | budget 达到阈值会自动停止资源吗？ |
| Q030 | 成本 | 如何按 team、environment、subscription 或 tag 分摊费用？ |
| Q031 | 成本 | actual cost 与 amortized cost 应该看哪个？ |
| Q032 | 成本 | 为什么今天的成本还没出现在 Cost Analysis？ |
| Q033 | 异常费用 | VM 已关机为什么还在收费？ |
| Q034 | 异常费用 | 没有请求为什么预配服务或 hosting plan 仍有费用？ |
| Q035 | 异常费用 | 删除主资源后为什么磁盘、IP、日志或 Marketplace 仍收费？ |
| Q036 | 异常费用 | 429 或失败请求是否可能继续计入用量或限流窗口？ |
| Q037 | Policy | RequestDisallowedByPolicy 是哪条 assignment 导致的？ |
| Q038 | Policy | 为什么 Owner 也不能绕过 deny policy？ |
| Q039 | Policy | non-compliant、deny、audit、modify 和 exemption 分别意味着什么？ |
| Q040 | 平台控制 | 内容过滤拦截与 Azure Policy deny 有什么区别？ |
| Q041 | 平台控制 | 为什么某模型或功能需要 limited access / registration？ |
| Q042 | 平台控制 | 修改 content filter 是否等于关闭平台安全控制？ |
| Q043 | 安全 | Defender for Cloud 的安全告警影响哪些资源？ |
| Q044 | 安全 | 高严重度安全告警是否等于确认入侵？ |
| Q045 | 审计 | 是谁在什么时候修改或删除了 Azure 资源？ |
| Q046 | 审计 | 为什么 Activity Log 找不到数据读取或对象删除？ |
| Q047 | 审计 | 如何比较 Azure 资源修改前后的属性？ |
| Q048 | 可用性 | 某服务、SKU、模型或版本在哪些 Azure Global 区域可用？ |
| Q049 | 可用性 | 为什么官方说区域可用但我的 subscription 看不到？ |
| Q050 | 可用性 | Global、Data Zone 和 Regional deployment 的可用范围怎么判断？ |
| Q051 | 配额 | Azure quota 属于 tenant、subscription、region 还是 deployment？ |
| Q052 | 配额 | Azure OpenAI Quota Tier 如何升级，申请获批为什么 Tier 不变？ |
| Q053 | 配额 | Global Standard 和 Data Zone 是否已接入订阅级共享池，Scope 怎么看？ |
| Q054 | 配额 | 谁能查看 quota，TPM、RPM 和 PTU 单位怎么区分？ |
| Q055 | 容量 | quota 足够为什么仍出现 AllocationFailed 或 insufficient capacity？ |
| Q056 | 容量 | SkuNotAvailable、QuotaExceeded 和 AllocationFailed 如何区分？ |
| Q057 | 限流 | 管理API和模型请求的429应如何分层判断，而不是统一提额？ |
| Q058 | 限流 | 为什么每分钟平均请求不高，仍可能因更短窗口的突发被限流？ |
| Q059 | 限流 | max_tokens、被拒请求、异常响应头与dynamic quota各能证明什么？ |
| Q060 | 支持 | Azure Status、Service Health 和 Resource Health 有什么区别？ |
| Q061 | 支持 | 如何确认一次中断是平台、资源还是客户配置导致？ |
| Q062 | 通知 | 在哪里查看 service retirement、maintenance 和 impacted resources？ |
| Q063 | 支持 | 创建 Azure support request 要准备哪些证据和 severity 信息？ |
| Q064 | 范围回归 | 如何配置 DNS、VNet、firewall 或 private endpoint？ |
| Q065 | 范围回归 | 如何设计备份恢复、域名证书或应用架构？ |

最后更新：2026-10-28
