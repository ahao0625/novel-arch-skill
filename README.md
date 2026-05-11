# Novel Arch — 网文创作项目架构技能

> **任何 AI 平台通用。** 不用装插件、不用配环境、不依赖任何特定工具。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/ahao0625/novel-arch-skill?style=social)](https://github.com/ahao0625/novel-arch-skill/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ahao0625/novel-arch-skill?style=social)](https://github.com/ahao0625/novel-arch-skill/network/members)
[![Project Maintained](https://img.shields.io/badge/Maintained-YES!-green.svg)](https://github.com/ahao0625/novel-arch-skill/pulse)

---

## 这是什么

这是一个**项目架构搭建技能**，定义了 5 个核心操作。你一句话触发，AI 按内置操作手册执行：

| 操作 | 你告诉 AI | AI 做什么 |
|:---|:---|---:|
| 新建项目 | "开一本新书，大纲如下..." | 解析大纲 → 创建目录 → 填充设定/人物/大纲 → 自检 |
| 写入章节 | "写第 5 章" | 读设定速查 → 按流程写作 → 质检 → 更新日志 |
| 更新设定 | "加一个角色" | 定位文件 → 修改 → 同步速查 → 记变更日志 |
| 运行审计 | "检查最近 10 章" | 逐项检查设定/角色/伏笔/红线 → 输出报告 |
| 关卷存档 | "本卷写完" | 生成快照 → 刷新锚点 → 更新总索引 |

## 使用方式

在任意 AI 对话中说以下指令即可：

```
"新建一个玄幻小说项目，书名为《我为百代共主》，共 9 卷 200 万字，以下是大纲..."
"继续写第 5 章，上一章写到..."
"对最近 10 章做一次审计"
```

AI 会读取本技能附带的 `references/ai-operations-manual.md`（AI 操作手册），按手册中定义的步骤执行，每步自检。

## 前提条件

- AI 需要具有**文件读写能力**（WorkBuddy、Claude Projects、ChatGPT Code Interpreter 等均支持）
- 无需安装任何软件

## 文件说明

```
novel-arch-skill/
├── SKILL.md                              ← 技能定义（用户视角：这是什么、怎么用）
├── references/
│   ├── ai-operations-manual.md           ← AI 操作手册（AI 执行时读取）
│   └── ai-novel-architecture.md          ← 架构方案全文（参考）
└── scripts/
    └── setup_project.py                  ← 辅助脚本（可选）
```

## 功能特性

- **10+3 模块化目录**：世界设定、人物档案、故事大纲、时间线、伏笔悬念、正文、索引、日志、审计、模板
- **5 个核心操作**：新建项目、写入章节、更新设定、运行审计、关卷存档
- **字段级规范**：每个字段标注必填/推荐/可选，AI 不会模糊执行
- **自检嵌在每一步**：每做完一步自己检查，不一致即时发现
- **内容标注规则**：【待补充】/【待设定】/【AI 推断】/【AI 建议】，AI 不自作主张编造

## 相关项目

- [general-writing-skill](https://github.com/ahao0625/general-writing-skill) — 通用写作技能
- [novel-audit-skill](https://github.com/ahao0625/novel-audit-skill) — 网文审计技能
- [novel-polish-skill](https://github.com/ahao0625/novel-polish-skill) — 网文润色技能

---

## ⭐ 如果对你有帮助，请支持一下！

[![GitHub stars](https://img.shields.io/github/stars/ahao0625/novel-arch-skill?style=social)](https://github.com/ahao0625/novel-arch-skill/stargazers)

### ☕ 赞助一杯咖啡

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

[MIT](LICENSE) © ahao0625
