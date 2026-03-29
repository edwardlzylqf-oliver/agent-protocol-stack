# Agent Protocol Stack (APS)

> Open protocol for multi-agent AI communication

[中文](./README.md) | English

---

## 🎯 Vision

**Agent Protocol Stack** is an open protocol for multi-agent AI systems, inspired by the Spine-Leaf architecture in networking. It provides a standardized framework for AI assistants to communicate, collaborate, and coordinate.

### The Big Picture

```
When we have one AI assistant → It's a powerful tool
When we have multiple AI assistants → They need coordination
When AI assistants come from different platforms → They need a common language

APS is born for this — An open, universal, extensible protocol for agent communication
```

---

## 🏗️ Architecture

### Spine-Leaf Design

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Spine-Leaf Architecture                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│                          ┌─────────────┐                            │
│                          │    Spine    │                            │
│                          │(Coordinator)│                            │
│                          └──────┬──────┘                            │
│                                 │                                    │
│         ┌───────────────────────┼───────────────────────┐            │
│         │                       │                       │            │
│         ▼                       ▼                       ▼            │
│   ┌─────────┐            ┌─────────┐            ┌─────────┐         │
│   │  Leaf 1 │            │  Leaf 2 │            │  Leaf 3 │         │
│   │(Executor│            │(Executor│            │(Executor│         │
│   └─────────┘            └─────────┘            └─────────┘         │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

| Component | Description |
|-----------|-------------|
| **Spine** | Coordinator: task distribution, decision making |
| **Leaf** | Executor: task execution |
| **Observer** | Supervisor: process monitoring |

---

## 🔧 Protocol Stack

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Agent Protocol Stack                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   L7  Application  │ Spine-Leaf / Task Management / Memory          │
│   ─────────────────────────────────────────────────────────────────  │
│   L6  Transport    │ HTTP / WebSocket / gRPC / MQ                    │
│   ─────────────────────────────────────────────────────────────────  │
│   L5  Protocol     │ AMP (Agent Message Protocol)                   │
│   ─────────────────────────────────────────────────────────────────  │
│   L4  Adapter      │ Platform Adapters (OpenClaw / Claude / ...)    │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📦 Features

- ✅ **Role System** - Spine/Leaf/Observer definitions and response rules
- ✅ **Task Routing** - Keyword routing, composite tasks, load balancing
- ✅ **Layered Memory** - Global/Local/Private three-tier memory
- ✅ **Arbitration** - Version control, conflict detection, auto-arbitration
- ✅ **Security** - Authentication, Authorization, Audit
- 🔄 **Cross-platform Interop** - Adapter pattern (in development)
- 🔲 **Federated Learning** - Cross-organization collaboration (planned)

---

## 🚀 Quick Start

### 1. Create Configuration

```yaml
# UserConfig.yaml
cluster:
  name: "My Agent Team"

agents:
  - id: "spine_001"
    name: "Coordinator"
    role: "spine"
    type: "coordinator"
    capabilities: ["planning", "coordination", "decision"]

  - id: "leaf_001"
    name: "Analyst"
    role: "leaf"
    type: "executor"
    capabilities: ["analysis", "data"]
```

### 2. Validate

```bash
python scripts/validate_config.py --config UserConfig.yaml
```

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [Protocol Spec](./docs/protocol/) | Complete technical specification |
| [Getting Started](./docs/getting-started.md) | 5-minute quick start |
| [Configuration Guide](./docs/configuration.md) | Detailed configuration |
| [API Reference](./docs/api/) | API documentation |

---

## 🛠️ Tech Stack

- **Config**: YAML, JSON
- **Storage**: Obsidian (Markdown), File System
- **Script**: Python 3.10+
- **Testing**: pytest

---

## 🤝 Contributing

Contributions are welcome! Please submit issues and pull requests.

---

## 📄 License

[MIT License](./LICENSE)

---

## 📞 Contact

- GitHub Issues: [Submit bugs or suggestions](https://github.com/your-repo/issues)

---

*Make AI agent collaboration as simple as network communication*