---
name: novel-arch
description: |
  AI 网文创作项目架构搭建技能。
  用户触发后，AI 读取内置的 AI 操作手册（ai-operations-manual.md），按手册指令执行。
  覆盖：新建项目、写入章节、更新设定、运行审计、关卷存档五个操作。
  WorkBuddy 及其他 AI 平台通用。
agent_created: true
---

# Novel Arch — 网文创作项目架构搭建技能

## 这是什么

这是一个**项目架构搭建技能**，而不是一个写作技能。它的作用是：

| 你告诉 AI | AI 执行的操作 |
|:---|:---|
| "开一本新书，以下是大纲..." | 解析大纲 → 搭目录 → 填充设定/人物/大纲文件 → 自检 → 报告 |
| "写第 X 章" | 读设定速查 → 按流程写作 → 质检 → 更新日志/伏笔/索引 |
| "加个角色" / "改个设定" | 定位文件 → 修改 → 同步速查锚点 → 记变更日志 |
| "审计一下最近 10 章" | 逐项检查设定/角色/伏笔/红线 → 输出审计报告 |
| "本卷结束了" | 生成快照 → 刷新锚点 → 完善卷概述 → 更新总索引 |

## 工作方式

AI 不依赖任何脚本或插件。它读取本技能附带的 `references/ai-operations-manual.md`（AI 操作手册），手册中定义了完整的执行步骤、字段规范、自检规则。AI 按手册执行。

## 使用方式

在任意 AI 对话中说以下指令即可触发：

```
"新建一个小说项目"
"开新书"
"按照架构方案创建项目"
"初始化新书"
"帮我把这本小说建好项目"
```

如果你有大纲/设定文档，一并提供，AI 会自动拆解填充到对应文件中。

### 适用示例

```
"新建一个玄幻小说项目，书名为《我为百代共主》，共 9 卷 200 万字，以下是大纲..."
```

```
"继续写第 5 章，上一章写到主角被追杀至悬崖边"
```

```
"对最近 10 章做一次审计"
```

## 前提条件

- AI 需要**文件读写能力**（在 WorkBuddy 中自动具备；其他平台需确认是否支持创建和编辑文件）
- 不需要安装任何软件、不需要配置环境变量

## 文件说明

| 文件 | 用途 |
|:---|:---|
| `SKILL.md` | 本文件，技能定义（用户视角） |
| `references/ai-operations-manual.md` | AI 操作手册，AI 执行时读取的完整指令集 |
| `references/ai-novel-architecture.md` | 架构方案全文（参考文档） |
| `scripts/setup_project.py` | 辅助脚本，部分平台可用 |

## 相关技能

- [novel-audit-skill](https://github.com/ahao0625/novel-audit-skill) — 网文审计
- [novel-polish-skill](https://github.com/ahao0625/novel-polish-skill) — 网文润色
- [general-writing-skill](https://github.com/ahao0625/general-writing-skill) — 通用写作
