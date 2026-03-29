# Agent Protocol Stack - 完整技术规范

> 版本：1.0.0 | 状态：Draft

---

## 一、协议概述

### 1.1 目标与范围

Agent Protocol Stack (APS) 是一个面向多智能体系统的通信协议标准，旨在：

1. **标准化通信**：为不同平台的AI智能体提供统一的通信格式
2. **简化协作**：降低多智能体系统的开发复杂度
3. **促进互操作**：支持跨平台、跨组织的智能体协作

### 1.2 设计原则

| 原则 | 说明 |
|------|------|
| **简洁性** | 最少的信息冗余，清晰的协议结构 |
| **可扩展** | 支持自定义扩展，不破坏兼容性 |
| **互操作** | 跨平台兼容，适配器模式 |
| **安全性** | 内置认证、授权、审计机制 |

---

## 二、核心概念

### 2.1 Agent (智能体)

智能体是协议的基本执行单元，每个智能体具有：

- **唯一标识** (Agent ID)
- **角色类型** (Spine/Leaf/Observer)
- **能力集合** (Capabilities)
- **独立工作空间** (Workspace)

### 2.2 Cluster (集群)

集群是一组协同工作的智能体：

```
Cluster
├── Spine (1个)
├── Leafs (多个)
├── Observer (可选)
└── Shared Resources
```

### 2.3 Task (任务)

任务是智能体协作的基本单元：

```yaml
task:
  task_id: "唯一标识"
  type: "single|composite"
  priority: "low|normal|high|urgent"
  status: "pending|assigned|executing|completed|failed"
```

---

## 三、角色体系

### 3.1 Spine (协调者)

Spine是集群的核心，负责：
- 接收用户请求
- 解析任务意图
- 路由任务到合适的Leaf
- 汇总结果并反馈

### 3.2 Leaf (执行者)

Leaf是任务的实际执行者：
- 只在被指定时执行任务
- 执行完成后返回结果
- 可以具有不同的专长（分析、设计、开发等）

### 3.3 Observer (监督者)

Observer负责监督流程：
- 监听所有通信
- 发现问题并提出质疑
- 不直接参与执行

---

## 四、响应规则

### 4.1 消息接收权限

| 角色 | 接收所有消息 | 只接收指定消息 |
|------|--------------|----------------|
| **Spine** | ✅ | - |
| **Observer** | ✅ | - |
| **Leaf** | ❌ | ✅ |

### 4.2 禁止规则

| 编号 | 禁止行为 | 处罚 |
|------|----------|------|
| F1 | 未经Spine确认就回答 | 首次提醒→多次记录 |
| F2 | 未经@直接响应 | 同上 |
| F3 | 被@后不回复"收到" | 首次提醒 |
| F4 | 转告而非直接@ | 提醒 |

---

## 五、任务路由

### 5.1 路由流程

```
用户任务 → Spine解析 → 关键词匹配 → @目标Leaf → 执行 → 结果汇总
```

### 5.2 路由表格式

```json
{
  "rules": [
    {
      "keywords": ["分析", "数据", "报表"],
      "targets": ["leaf_analyst"],
      "description": "数据分析任务"
    },
    {
      "keywords": ["PPT", "设计", "演示"],
      "targets": ["leaf_designer"],
      "description": "设计制作任务"
    }
  ]
}
```

### 5.3 复合任务

当任务涉及多个技能领域时，自动识别为复合任务：

```yaml
composite_task:
  task_type: "专业报告"
  required_skills:
    - skill: "分析"
      agent: "leaf_analyst"
    - skill: "PPT"
      agent: "leaf_designer"
  execution_mode: "sequential"  # 或 "parallel"
```

---

## 六、分层记忆

### 6.1 记忆层级

| 层级 | 名称 | 可见性 | 同步方式 |
|------|------|--------|----------|
| L0 | 全局记忆 | 所有Agent | 即时推送 |
| L1 | 局部记忆 | 组内成员 | 定时同步 |
| L2 | 私有记忆 | 仅自己 | 手动同步 |

### 6.2 同步规则

```yaml
sync_rules:
  private_to_local:
    trigger: "daily"
    filter:
      - important: true
      - shared: true
      
  local_to_global:
    trigger: "weekly"
    filter:
      - type: "knowledge"
      - type: "rule"
```

---

## 七、协议栈

### 7.1 四层架构

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Agent Protocol Stack                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   L7  应用层    │ Spine-Leaf协议 / 任务管理 / 记忆系统               │
│   ─────────────────────────────────────────────────────────────────  │
│   L6  传输层    │ HTTP / WebSocket / gRPC / Message Queue           │
│   ─────────────────────────────────────────────────────────────────  │
│   L5  协议层    │ AMP (Agent Message Protocol)                       │
│   ─────────────────────────────────────────────────────────────────  │
│   L4  适配层    │ 平台适配器                                         │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### 7.2 AMP消息格式

```json
{
  "amp_version": "1.0",
  "message_id": "唯一标识",
  "message_type": "task_request|response|error|...",
  
  "header": {
    "sender": {
      "platform": "openclaw",
      "agent_id": "spine_001",
      "address": "agent://openclaw/spine_001@main/default"
    },
    "receiver": {...},
    "timestamp": "ISO8601"
  },
  
  "body": {
    "type": "task",
    "content": {...}
  },
  
  "metadata": {
    "encoding": "utf-8",
    "auth": {...}
  }
}
```

---

## 八、安全机制

### 8.1 身份认证

| 方式 | 适用场景 | 安全级别 |
|------|----------|----------|
| API Key | Agent间通信 | 中 |
| Token | 用户会话 | 高 |
| MFA | 敏感操作 | 极高 |

### 8.2 权限控制

基于RBAC的权限模型：

| 角色 | 全局记忆 | 局部记忆 | 私有记忆 | 任务管理 |
|------|----------|----------|----------|----------|
| Spine | 读/写 | 读/写 | 读 | 全部 |
| Leaf | 读 | 读/写(组内) | 读/写 | 执行 |
| Observer | 读 | 读 | - | 监督 |

---

## 九、版本管理

### 9.1 语义化版本

```
主版本.次版本.修订号
1.0.0

- 主版本: 不兼容的API变更
- 次版本: 向后兼容的功能新增
- 修订号: 向后兼容的问题修复
```

### 9.2 兼容性

| 版本关系 | 说明 |
|----------|------|
| 1.0 → 1.1 | 向后兼容 |
| 1.0 → 2.0 | 可能破坏兼容 |

---

## 十、扩展机制

### 10.1 适配器模式

```
不同平台通过适配器接入APS:

OpenClaw → OpenClawAdapter → AMP → Spine
Claude   → ClaudeAdapter   → AMP → Spine
Cursor   → CursorAdapter   → AMP → Spine
```

### 10.2 自定义扩展

```yaml
extensions:
  - name: "custom_capability"
    type: "skill"
    handlers:
      - event: "task_request"
        handler: "custom_handler.py"
```

---

## 附录A: 术语表

| 术语 | 说明 |
|------|------|
| Agent | 智能体，AI执行单元 |
| Spine | 协调者，核心节点 |
| Leaf | 执行者，叶子节点 |
| Observer | 监督者，监控角色 |
| Cluster | 集群，智能体组织 |
| AMP | Agent Message Protocol |
| APS | Agent Protocol Stack |

## 附录B: 错误码

| 范围 | 类别 |
|------|------|
| 1000-1999 | 连接错误 |
| 2000-2999 | 任务错误 |
| 3000-3999 | 协议错误 |
| 4000-4999 | 权限错误 |

---

*本文档持续更新中 | 版本 1.0.0*