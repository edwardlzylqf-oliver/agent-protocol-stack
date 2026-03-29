# 分层记忆架构

> 版本：1.0 | 状态：生效
> 基于：文档存储分级方案
> 更新日期：2026-03-29

---

## 一、记忆层级定义

| 层级 | 名称 | 位置 | 可见性 | 同步方式 |
|------|------|------|--------|----------|
| **L0** | 全局记忆 | `Memory/Global/` | 所有Agent | 即时推送 |
| **L1** | 局部记忆 | `Memory/Local/` | 项目组/业务组 | 定时同步 |
| **L2** | 私有记忆 | `{workspace}/memory/` | 仅自己 | 手动同步 |

---

## 二、各层级内容

### L0 全局记忆（Global）

**位置**: `Obsidian/⚙️Clusters/Memory/Global/`

**内容**:
- 📜 法律法规（政策、法规、合规要求）
- 📋 公司规则（制度、规范、流程）
- 🌍 全局知识库（通用知识、标准）
- 🔔 重要通知（全员公告、变更）

**可见范围**: 所有Agent可读

**同步规则**:
- 变更时即时推送
- 每日检查更新

### L1 局部记忆（Local）

**位置**: `Obsidian/⚙️Clusters/Memory/Local/`

**结构**:
```
Local/
├── 项目组-AIM/          ← 项目组
│   ├── 任务.md
│   ├── 进度.md
│   └── 文档/
│
├── 金蝶业务组/         ← 业务组
│   ├── 业务规则.md
│   ├── 案例.md
│   └── 经验.md
│
└── 投资研究组/         ← 业务组
    ├── 市场分析.md
    └── 标的跟踪.md
```

**可见范围**: 组内成员

**同步规则**:
- 私有→局部: 每日筛选
- 局部→全局: 每周归纳

### L2 私有记忆（Private）

**位置**: `{agent_workspace}/memory/`

**结构**:
```
memory/
├── daily/              ← 每日记录
│   └── YYYY-MM-DD.md
│
├── projects/           ← 项目待办
│   └── 项目名.md
│
└── notes/             ← 临时笔记
    └── *.md
```

**可见范围**: 仅Agent自己

---

## 三、同步规则

```yaml
sync_policy:
  # L2 → L1: 私有到局部
  private_to_local:
    trigger: "daily"          # 每日触发
    time: "23:00"             # 每天23:00
    filter:                   # 筛选条件
      - "important: true"
      - "shared: true"
    review: "required"         # 需要审核
    
  # L1 → L0: 局部到全局
  local_to_global:
    trigger: "weekly"         # 每周触发
    day: "Sunday"             # 周日
    time: "22:00"
    filter:
      - "type: knowledge"     # 知识类
      - "type: rule"         # 规则类
    review: "required"
    
  # L0 → L1/L2: 全局推送
  global_push:
    trigger: "immediate"      # 即时推送
    content_types:
      - "law_update"         # 法律更新
      - "rule_change"        # 规则变更
      - "announcement"       # 重要通知
```

---

## 四、访问控制

| 记忆层 | 读 | 写 | 删除 |
|--------|----|----|------|
| L0 Global | 所有Agent | Spine | Spine |
| L1 Local | 组内成员 | 组内成员 | Spine |
| L2 Private | 仅自己 | 仅自己 | 仅自己 |

---

## 五、仲裁机制

当多个Agent同时修改L1局部记忆时：

1. **版本检测**: 比较修改时间戳
2. **冲突标记**: 如有冲突，标记需审核
3. **默认策略**: 时间戳最新的覆盖
4. **人工介入**: 复杂冲突由Spine处理

---

## 关联文档

- `../Protocol/Core/AgentProtocol.md` - 核心协议
- `../Registry/MemoryPolicy.yaml` - 记忆策略配置
- `../Arbitration/` - 仲裁机制

---

*基于文档存储分级方案整合 | 2026-03-29*