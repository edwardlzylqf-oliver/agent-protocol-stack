# Agent Protocol Stack (APS)

> 一个面向多智能体系统的开放通信协议

**简体中文** | [English](./README_en.md)

---

## 🎯 愿景

```
当有一个AI助手时，它是一个强大的工具
当有多个AI助手时，它们需要协调
当AI助手来自不同平台时，它们需要共同语言

APS —— 为多智能体协作而生的开放协议
```

---

## 🏗️ 核心架构

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         Spine-Leaf 多智能体架构                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│                          ┌─────────────────┐                            │
│                          │      Spine       │                            │
│                          │    (协调者)      │                            │
│                          │  • 任务路由       │                            │
│                          │  • 决策汇总       │                            │
│                          │  • 记忆同步       │                            │
│                          └────────┬────────┘                            │
│                                   │                                       │
│         ┌────────────────────────┼────────────────────────┐            │
│         │                        │                        │            │
│         ▼                        ▼                        ▼            │
│  ┌─────────────┐          ┌─────────────┐          ┌─────────────┐     │
│  │   Leaf 1    │          │   Leaf 2    │          │   Leaf 3    │     │
│  │  (执行者)   │          │  (执行者)   │          │  (执行者)   │     │
│  │  • 分析    │          │  • 设计    │          │  • 开发    │     │
│  │  • 研究    │          │  • 可视化   │          │  • 实现    │     │
│  └─────────────┘          └─────────────┘          └─────────────┘     │
│                                                                          │
│  可选: ┌─────────────┐                                                   │
│        │  Observer   │                                                   │
│        │  (监督者)   │ ← 监听所有通信，发现问题                          │
│        └─────────────┘                                                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 📦 协议栈

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          Agent Protocol Stack                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  L7 应用层                                                              │
│  ├─ Spine-Leaf 协作协议                                                │
│  ├─ 任务管理                                                           │
│  ├─ 分层记忆                                                           │
│  └─ 仲裁机制                                                           │
│                                                                          │
│  L6 传输层                                                              │
│  ├─ HTTP / WebSocket                                                   │
│  ├─ gRPC                                                              │
│  └─ Message Queue                                                      │
│                                                                          │
│  L5 协议层 (AMP - Agent Message Protocol)                               │
│  ├─ 消息格式                                                           │
│  ├─ 寻址机制                                                           │
│  └─ 会话管理                                                           │
│                                                                          │
│  L4 适配层                                                              │
│  ├─ OpenClaw Adapter                                                   │
│  ├─ Claude Adapter                                                    │
│  └─ Generic Adapter                                                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## ✨ 主要特性

| 特性 | 说明 |
|------|------|
| 🔄 **智能路由** | 关键词路由 + 复合任务识别 + 负载均衡 |
| 🎭 **角色体系** | Spine/Leaf/Observer 明确分工 |
| 🧠 **分层记忆** | 全局/局部/私有 三级记忆系统 |
| ⚖️ **仲裁机制** | 版本控制 + 冲突检测 + 自动解决 |
| 🔒 **企业级安全** | 认证授权 + 加密 + 审计日志 |
| 🌐 **跨平台互操作** | 适配器模式支持多平台 |

---

## 🚀 快速开始

### 1. 创建配置

```yaml
# config/UserConfig.yaml
cluster:
  name: "My Agent Team"

agents:
  - id: "spine_001"
    name: "Coordinator"
    role: "spine"
    type: "coordinator"
    capabilities:
      - "规划"
      - "协调"
      - "决策"

  - id: "leaf_analyst"
    name: "Analyst"
    role: "leaf"
    type: "executor"
    capabilities:
      - "分析"
      - "数据"

  - id: "leaf_designer"
    name: "Designer"
    role: "leaf"
    type: "designer"
    capabilities:
      - "设计"
      - "PPT"

routing:
  rules:
    - keywords: ["分析", "数据"]
      targets: ["leaf_analyst"]
    - keywords: ["设计", "PPT"]
      targets: ["leaf_designer"]
```

### 2. 运行验证

```bash
# 克隆仓库
git clone https://github.com/your-repo/agent-protocol-stack.git
cd agent-protocol-stack

# 验证配置
python3 src/validate_config.py --config examples/UserConfig.example.yaml

# 输出示例
# ✅ 配置加载成功
# ✅ Spine验证通过: spine_001
# ✅ 路由目标验证通过
# ✅ 注册表已生成: registry/AgentRegistry.json
```

---

## 📚 文档

### 核心协议文档

| 文档 | 说明 |
|------|------|
| [协议规范](./docs/protocol/spec.md) | 完整技术规范 |
| [角色体系](./docs/protocol/roles.md) | Spine/Leaf/Observer定义 |
| [任务路由](./docs/protocol/routing.md) | 路由机制详解 |
| [分层记忆](./docs/protocol/memory.md) | 记忆系统设计 |

### 指南

| 指南 | 说明 |
|------|------|
| [快速开始](./docs/guides/getting-started.md) | 5分钟上手 |
| [配置指南](./docs/guides/configuration.md) | 完整配置说明 |
| [部署指南](./docs/guides/deployment.md) | 生产环境部署 |

### API 参考

| 参考 | 说明 |
|------|------|
| [AMP 协议](./docs/api/amp.md) | Agent Message Protocol |
| [适配器接口](./docs/api/adapter.md) | 适配器开发指南 |

---

## 📝 系列文章

| 序号 | 标题 | 核心内容 |
|------|------|----------|
| [01](./docs/articles/article01-architecture.md) | 起源与架构设计 | Spine-Leaf灵感、整体架构 |
| [02](./docs/articles/article02-roles.md) | 角色体系与响应规则 | 角色定义、禁止规则 |
| [03](./docs/articles/article03-routing.md) | 任务路由机制 | 关键词路由、复合任务 |
| [04](./docs/articles/article04-memory.md) | 分层记忆系统 | L0/L1/L2设计、同步策略 |
| [05](./docs/articles/article05-arbitration.md) | 仲裁与冲突处理 | 版本控制、仲裁机制 |
| [06](./docs/articles/article06-security.md) | 安全与企业级特性 | 认证、授权、审计 |
| [07](./docs/articles/article07-interop.md) | 协议栈与跨平台互操作 | AMP协议、适配器模式 |

---

## 🛠️ 技术栈

| 组件 | 技术 | 说明 |
|------|------|------|
| 配置格式 | YAML, JSON | 人类可读的配置文件 |
| 存储 | Obsidian / 文件系统 | 灵活的记忆存储 |
| 脚本 | Python 3.10+ | 跨平台脚本支持 |
| 测试 | pytest | 单元测试和集成测试 |

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 开发流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

---

## 📄 许可证

本项目采用 [MIT License](./LICENSE) 开源。

---

## 📞 联系

- **GitHub Issues**: [提交 Bug 或建议](https://github.com/your-repo/agent-protocol-stack/issues)
- **讨论群**: [加入讨论](https://github.com/your-repo/agent-protocol-stack/discussions)

---

## 🙏 致谢

- 灵感来源：[Spine-Leaf Network Architecture](https://en.wikipedia.org/wiki/Leaf-spine)
- 网络协议设计：[TCP/IP](https://en.wikipedia.org/wiki/TCP/IP)
- 多智能体系统研究：[Multi-Agent Systems](https://en.wikipedia.org/wiki/Multi-agent_system)

---

```
让AI智能体协作像网络通信一样简单
Make AI agent collaboration as simple as network communication
```