# Novel Arch — 网文创作项目架构技能

> **任何 AI 平台通用。** 粘贴指令给 AI，AI 即可按手册执行。
> 不用装插件、不用配环境、不依赖任何特定工具。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/ahao0625/novel-arch-skill?style=social)](https://github.com/ahao0625/novel-arch-skill/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ahao0625/novel-arch-skill?style=social)](https://github.com/ahao0625/novel-arch-skill/network/members)
[![Project Maintained](https://img.shields.io/badge/Maintained-YES!-green.svg)](https://github.com/ahao0625/novel-arch-skill/pulse)

---

## 这是什么

这是一份 **AI 操作手册**，定义了 5 个核心操作：

| 操作 | 你告诉 AI | AI 做什么 |
|:---|:---|---:|
| 新建项目 | "开一本新书，大纲如下..." | 解析大纲 → 创建目录 → 填充设定/人物/大纲文件 → 自检 |
| 写入章节 | "写第 5 章" | 读设定速查 → 按四阶段写作 → 质检 → 更新日志/伏笔/索引 |
| 更新设定 | "加一个角色" | 定位文件 → 修改 → 同步速查锚点 → 记变更日志 |
| 运行审计 | "检查最近 10 章" | 逐项检查设定/角色/伏笔/红线 → 输出审计报告 |
| 关卷存档 | "本卷写完" | 生成快照 → 刷新锚点 → 完善卷概述 → 更新总索引 |

## 使用方式

```
1. 将 SKILL.md 全文粘贴到任意 AI 对话中
   支持：Claude、ChatGPT、DeepSeek、通义千问、Kimi 等
2. 输入你的需求，例如：

   "请按操作手册执行：新建一个玄幻小说项目，书名为《我为百代共主》，
    共 9 卷，200 万字。以下是大纲：[粘贴大纲]"

3. AI 按手册自动执行，每步自检后输出结果
```

## 一句话原理

> 不是给 AI 一个工具，而是给 AI 一份它自己能读懂的操作手册。
> AI 本身就是执行引擎，不需要任何外部依赖。

## 为什么是纯文本

| 传统方案 | 本方案 |
|:---|---:|
| 绑定特定平台/IDE | 任何 AI 平台通用 |
| 需要安装脚本/插件 | 零安装，零配置 |
| 平台升级可能失效 | 纯文本，永久可用 |
| 换个工具重新学习 | 一份指令通吃所有 AI |

## 功能特性

- **10+3 模块化目录**：世界设定、人物档案、故事大纲、时间线、伏笔悬念、正文、索引、日志、审计、模板
- **5 个核心操作**：新建项目、写入章节、更新设定、运行审计、关卷存档
- **字段级规范**：每个字段标注必填/推荐/可选，AI 不会模糊执行
- **自检嵌在每一步**：每做完一步自己检查，不一致即时发现
- **内容标注规则**：【待补充】/【待设定】/【AI 推断】/【AI 建议】，AI 不自作主张编造
- **反跑偏守御体系**：章节元数据、设定速查锚点、排除指令、变更日志、快照存档、红线清单、审计健康检查

## 文件结构

```
novel-arch-skill/
├── SKILL.md                    ← AI 操作手册（核心，复制到 AI 对话使用）
├── README.md                   ← 本文件
├── CHANGELOG.md                ← 更新日志
├── LICENSE                     ← MIT 许可证
├── install.sh                  ← （可选）WorkBuddy 安装脚本
├── .editorconfig               ← 编辑器配置
├── .github/workflows/          ← CI/CD
├── references/
│   └── ai-novel-architecture.md ← 架构方案全文
└── scripts/
    └── setup_project.py        ← （可选）项目搭建脚本
```

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
