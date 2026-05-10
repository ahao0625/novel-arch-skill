# Novel Arch Skill — AI 网文创作项目架构搭建

> **即装即用，一键创建结构化小说项目** — 基于通用架构方案，让 AI 创作不跑偏、设定不丢失

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/ahao0625/novel-arch-skill?style=social)](https://github.com/ahao0625/novel-arch-skill/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ahao0625/novel-arch-skill?style=social)](https://github.com/ahao0625/novel-arch-skill/network/members)
[![GitHub issues](https://img.shields.io/github/issues/ahao0625/novel-arch-skill)](https://github.com/ahao0625/novel-arch-skill/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/ahao0625/novel-arch-skill)](https://github.com/ahao0625/novel-arch-skill)
[![Project Maintained](https://img.shields.io/badge/Maintained-YES!-green.svg)](https://github.com/ahao0625/novel-arch-skill/pulse)

---

## 功能特性

### 核心能力

- **目录结构搭建**：10+3 个模块化目录，覆盖设定、人物、大纲、正文、日志、审计全链路
- **核心文件初始化**：自动生成设定骨架、角色档案模板、大纲模板、创作工作流
- **守御体系配置**：设定速查锚点、变更日志、红线清单、章节元数据头部
- **AI 上下文优化**：优先级分层读取、章节摘要缓存、排除指令机制
- **自动核验脚本**：时间线冲突检测、角色年龄校验、伏笔超期告警

### 适用题材

| 题材 | 目录适配 | 额外审计维度 |
|:---|:---|---:|
| 玄幻/仙侠 | 01_世界设定 | 境界体系一致性、法宝等级校验 |
| 都市/现代 | 01_时代背景 | 社会规则合理性、经济逻辑自洽 |
| 科幻 | 01_科技与世界观 | 科技树一致性、硬科幻规则校验 |
| 历史/架空 | 01_时代与制度 | 历史事件时间线、制度风俗考据 |
| 悬疑/推理 | 01_故事背景 | 线索合理性、信息公平性 |
| 言情 | 01_世界设定 | 情感发展曲线、关系推进节奏 |

---

## 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/ahao0625/novel-arch-skill.git

# 运行安装脚本
cd novel-arch-skill && bash install.sh
```

或直接下载 [Releases](https://github.com/ahao0625/novel-arch-skill/releases) 中的 zip 包解压到 WorkBuddy skills 目录。

### 使用方法

在 WorkBuddy 中触发以下任一指令：

```
"新建一个小说项目"
"按照架构方案创建项目"
"初始化新书"
"搭建网文项目目录"
"帮我开一本新书，按照架构方案"
```

WorkBuddy 会自动加载本技能并执行完整的 5 步流程：

1. **收集信息** — 书名、类型、目标字数、卷数
2. **创建目录** — 运行 `scripts/setup_project.py` 自动搭建
3. **初始化文件** — 填充设定骨架、角色模板、大纲模板
4. **检查清单** — 输出确认清单和下一步建议
5. **启动写作** — 按章节元数据模板写出第一章

### 快速命令

```bash
# 3 卷玄幻项目
python3 scripts/setup_project.py /path/to/项目名 --type 玄幻 --volumes 3

# 9 卷项目 + 可选目录
python3 scripts/setup_project.py /path/to/项目名 --type 玄幻 --volumes 9 --with-optional
```

---

## 架构概览

```
项目名称/
├── 01_世界设定/        ← 总纲、地理、规则 + 守御文件（速查锚点/变更日志/红线）
├── 02_人物档案/        ← 角色档案全集
├── 03_故事大纲/        ← 全书大纲 + 每卷章节纲要
├── 04_时间线/          ← 时间轴 + 卷级时间线
├── 05_伏笔与悬念/      ← 伏笔登记与回收追踪
├── 06_正文内容/        ← 正文 + 卷概述
├── 07_章节索引/        ← 卷级索引 + 总索引
├── 08_创作日志/        ← 卷级日志 + 章节摘要缓存
├── 09_审计报告/        ← 卷级审计报告
├── 10_创作模板/        ← 章节模板/审计模板/纲要模板
├── 11_素材库/          ← (可选)参考资料、概念图
├── 12_废弃稿/          ← (可选)删除章节归档
├── 13_数据统计/        ← (可选)字数曲线、进度统计
├── 创作工作流.md       ← 核心 SOP
└── 项目配置.md         ← AI 行为指令配置
```

---

## 文件结构

```
novel-arch-skill/
├── SKILL.md                    ← 技能定义（WorkBuddy 加载入口）
├── README.md                   ← 本文件
├── CHANGELOG.md                ← 更新日志
├── LICENSE                     ← MIT 许可证
├── install.sh                  ← 安装脚本
├── .editorconfig               ← 编辑器配置
├── .markdownlint.json          ← 标记语言检查配置
├── .github/workflows/
│   ├── ci.yml                  ← CI 工作流
│   └── release.yml             ← 发布工作流
├── references/
│   └── ai-novel-architecture.md ← 架构方案全文（技能参考）
├── scripts/
│   └── setup_project.py        ← 项目搭建脚本
├── assets/                     ← 资源文件（预留）
└── examples/                   ← 用例（预留）
```

---

## 反跑偏守御体系

本技能内置 7 个机制确保 AI 创作不跑偏、设定不丢失：

| 机制 | 作用 | 使用时机 |
|:---|---:|:---:|
| 章节元数据头部 | AI 打开文件即定位时间/地点/状态 | 每章开头 |
| 设定速查锚点 | 1 页极简快照替代全量设定读取 | 每次创作前 |
| 排除指令 | 明确告知 AI 不需要关注的范围 | 每次创作前 |
| 设定变更日志 | 版本追踪防新旧混用 | 设定变更时 |
| 设定快照存档 | 每卷凝固当前设定状态 | 卷结束时 |
| 红线清单 | 刚性底线不可触碰 | 每次创作前确认 |
| 自动核验脚本 | 时间线/年龄/等级/伏笔一致性检测 | 阶段性运行 |

---

## 相关项目

- [general-writing-skill](https://github.com/ahao0625/general-writing-skill) — 通用写作技能
- [novel-audit-skill](https://github.com/ahao0625/novel-audit-skill) — 网文审计技能
- [novel-polish-skill](https://github.com/ahao0625/novel-polish-skill) — 网文润色技能

---

## ⭐ 如果对你有帮助，请支持一下！

如果这个项目对你有帮助，可以：

### 🌟 点个 Star
这是对我最大的鼓励和支持！

[![GitHub stars](https://img.shields.io/github/stars/ahao0625/novel-arch-skill?style=social)](https://github.com/ahao0625/novel-arch-skill/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ahao0625/novel-arch-skill?style=social)](https://github.com/ahao0625/novel-arch-skill/network/members)

### ☕ 赞助一杯咖啡
如果这个技能帮你搭建了顺手的创作项目，可以考虑赞助我一杯咖啡，让我更有动力继续优化！

**赞助方式**：
- GitHub Sponsors（推荐）：点击右侧的 [Sponsor] 按钮
- 微信/支付宝：扫码见下方

**扫码打赏**：

<table>
  <tr>
    <td align="center">
      <img src="assets/wechat-qr.png" width="200" alt="微信收款码"/><br/>
      <strong>微信扫一扫</strong>
    </td>
    <td align="center">
      <img src="assets/alipay-qr.png" width="200" alt="支付宝收款码"/><br/>
      <strong>支付宝扫一扫</strong>
    </td>
  </tr>
</table>

**你的支持将用于**：
- 持续优化架构方案和技能
- 添加更多创作场景适配
- 维护参考文档和示例
- 回复用户反馈和问题

---

## 贡献

欢迎提交 Issue 和 Pull Request！详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

[MIT](LICENSE) © ahao0625
