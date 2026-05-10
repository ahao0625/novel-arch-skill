#!/usr/bin/env python3
"""
novel-arch setup_project.py — AI 网文创作项目搭建工具

用法:
  python3 setup_project.py <项目路径> [选项]

选项:
  --type <题材>       小说类型（玄幻/都市/科幻/历史/悬疑/言情，默认：玄幻）
  --volumes <数字>    总卷数（默认：3）
  --with-optional     同时创建可选目录 11-13

示例:
  python3 setup_project.py /Users/ahao/Documents/trae_projects/我为百代共主 --type 玄幻 --volumes 9
"""

import os
import sys
import argparse
from pathlib import Path

def mkdir_p(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def write_file(path, content=""):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def setup_project(project_dir, novel_type, volumes, with_optional):
    project_dir = Path(project_dir)
    novel_type_name = novel_type

    # 适配目录名
    world_dir = {
        "都市": "01_时代背景",
        "历史": "01_时代与制度",
        "科幻": "01_科技与世界观",
        "悬疑": "01_故事背景",
        "言情": "01_世界设定",
    }.get(novel_type, "01_世界设定")

    print(f"🚀 正在创建项目: {project_dir}")
    print(f"   类型: {novel_type_name} | 卷数: {volumes}")

    # === 创建目录结构 ===

    # 01 世界设定（含守御文件）
    mkdir_p(project_dir / world_dir)
    world_files = [
        "总纲.md",
        "地理与势力.md",
        "规则体系.md",
        "设定速查锚点.md",
        "设定变更日志.md",
        "红线清单.md",
    ]
    for f in world_files:
        write_file(project_dir / world_dir / f)

    # 02 人物档案
    mkdir_p(project_dir / "02_人物档案")
    write_file(project_dir / "02_人物档案" / "人物档案全集.md")

    # 03 故事大纲
    mkdir_p(project_dir / "03_故事大纲")
    write_file(project_dir / "03_故事大纲" / "全书故事大纲.md")
    for v in range(1, volumes + 1):
        write_file(project_dir / "03_故事大纲" / f"第{v}卷·章节纲要.md")

    # 04 时间线
    mkdir_p(project_dir / "04_时间线")
    write_file(project_dir / "04_时间线" / "完整时间线.md")
    for v in range(1, volumes + 1):
        write_file(project_dir / "04_时间线" / f"第{v}卷时间线.md")

    # 05 伏笔与悬念
    mkdir_p(project_dir / "05_伏笔与悬念")
    write_file(project_dir / "05_伏笔与悬念" / "伏笔与揭秘体系.md")

    # 06 正文内容
    mkdir_p(project_dir / "06_正文内容")
    for v in range(1, volumes + 1):
        vol_dir = project_dir / "06_正文内容" / f"第{v}卷"
        mkdir_p(vol_dir)
        write_file(vol_dir / "卷概述.md")

    # 07 章节索引
    mkdir_p(project_dir / "07_章节索引")
    write_file(project_dir / "07_章节索引" / "总索引.md")
    for v in range(1, volumes + 1):
        write_file(project_dir / "07_章节索引" / f"第{v}卷索引.md")

    # 08 创作日志
    mkdir_p(project_dir / "08_创作日志")
    for v in range(1, volumes + 1):
        write_file(project_dir / "08_创作日志" / f"第{v}卷创作日志.md")
    write_file(project_dir / "08_创作日志" / "卷内章节摘要缓存.md")

    # 09 审计报告
    mkdir_p(project_dir / "09_审计报告")
    for v in range(1, volumes + 1):
        mkdir_p(project_dir / "09_审计报告" / f"第{v}卷")

    # 10 创作模板
    mkdir_p(project_dir / "10_创作模板")
    # 章节正文模板
    write_file(project_dir / "10_创作模板" / "章节正文模板.md",
"""---
章号: {章号}
卷: 第X卷
时间: {时间}
地点: {地点}
主角状态: {状态}
活跃角色: {角色}
本章核心: {一句话}
前情提要: {上一章结尾}
---

# 第{章号}章 {标题}

（正文内容）
""")
    # 章节纲要模板
    write_file(project_dir / "10_创作模板" / "章节纲要模板.md",
"""# 第X卷·第X章纲要

## 基本信息
- 章号：{章号}
- 标题：{标题}
- 字数预算：{预算}
- 情绪曲线：{低开高走/持续紧张/先抑后扬}

## 核心事件
1. {事件1}
2. {事件2}

## 涉及角色
- {角色1}: {作用}
- {角色2}: {作用}

## 伏笔操作
- 埋设：{伏笔编号}（{描述}）
- 回收：{伏笔编号}（{描述}）

## 章末钩子
- 类型：{悬念/暗示/回收/升级}
- 内容：{描述}
""")
    # 审计报告模板
    write_file(project_dir / "10_创作模板" / "审计报告模板.md",
"""## 第X-X章审计报告

### 🔴 Critical
1. [问题] 位置/引用 → 修复方案

### 🟡 Warning
1. [问题] → 建议

### 🟢 Info
1. [提示]

### 伏笔状态
| 编号 | 状态 | 埋设章节 | 备注 |
|:---:|:---:|:---:|:---|

### 结论
- [综合评估]
- [待解决问题]
""")
    # 卷概述模板
    write_file(project_dir / "10_创作模板" / "卷概述模板.md",
"""# 第X卷概述

## 基本信息
- 卷号：第X卷
- 章数范围：第X章 - 第Y章
- 总字数：{字数}

## 本卷核心事件
- {事件1}
- {事件2}

## 主角起止状态
- 起始：{起始等级/阶段}
- 结束：{结束等级/阶段}

## 新增角色
- {角色1}
- {角色2}

## 本卷关键悬念
- 埋设：{清单}
- 回收：{清单}
""")
    # 设定速查锚点模板
    write_file(project_dir / "10_创作模板" / "设定速查锚点模板.md",
"""# 设定锚点速查（当前状态）

## 当前状态
- 主角：| 当前等级：| 所在地：
- 本卷：第X卷 | 本卷核心矛盾：
- 当前时间：开篇后 X 年 X 月

## 势力关系（当前）
- 势力A → 势力B：
- 势力C → 势力D：

## 近况变化（最近20章内新揭露/变更的设定）
-

## 活跃悬念（待回收，按紧急度排序）
- [编号] 描述 → 已埋 X 章
""")

    # 根级文件
    write_file(project_dir / "创作工作流.md", "<!-- 请将 AI 网文创作架构方案中的「二、创作工作流」部分内容复制至此 -->\n")
    write_file(project_dir / "项目配置.md",
f"""# 项目配置

## 项目信息
- 书名：{project_dir.name}
- 类型：{novel_type_name}
- 目标字数：200 万字
- 单章字数：2000-3000 字
- 总卷数：{volumes} 卷
- 核心主题：（待填写）

## AI 行为指令
- 输出语言：中文
- 每次创作前必须读取：{world_dir}/设定速查锚点.md
- 每章完成后必须填写：08_创作日志/对应卷创作日志.md
- 每次审计前必须读取：{world_dir}/红线清单.md
- 角色档案读取规则：仅读取本章活跃角色的档案

## 写作风格锚点
- 文风取向：（待填写）
- 对标参考：（待填写）
- 禁用词汇：（待填写）
- 去 AI 痕迹策略：参照创作工作流中的禁令和限频词

## 项目约定
- 每卷完成后需生成设定快照
- 设定变更后须更新设定变更日志
- 章节元数据头部为必填项
""")

    # === 可选目录 ===
    if with_optional:
        # 11 素材库
        mkdir_p(project_dir / "11_素材库" / "images")
        write_file(project_dir / "11_素材库" / "参考资料.md")

        # 12 废弃稿
        for v in range(1, volumes + 1):
            mkdir_p(project_dir / "12_废弃稿" / f"第{v}卷")

        # 13 数据统计
        mkdir_p(project_dir / "13_数据统计")
        write_file(project_dir / "13_数据统计" / "创作数据统计.md")

    # 总结
    print(f"\n✅ 项目创建完成: {project_dir}")
    print(f"   目录数: {11 + volumes * 6 + (3 if with_optional else 0)}")
    print(f"   文件数: {34 + volumes * 6 + (3 if with_optional else 0)}")
    print(f"\n下一步:")
    print(f"  1. 编辑 {world_dir}/总纲.md 填入核心设定")
    print(f"  2. 编辑 03_故事大纲/全书故事大纲.md 规划情节")
    print(f"  3. 编辑 02_人物档案/人物档案全集.md 录入角色")
    print(f"  4. 编辑 项目配置.md 完善项目元信息")

def main():
    parser = argparse.ArgumentParser(description="AI 网文创作项目搭建工具")
    parser.add_argument("project_path", help="项目路径（含项目名）")
    parser.add_argument("--type", default="玄幻", help="小说类型（默认：玄幻）")
    parser.add_argument("--volumes", type=int, default=3, help="总卷数（默认：3）")
    parser.add_argument("--with-optional", action="store_true", help="同时创建可选目录")
    args = parser.parse_args()

    setup_project(args.project_path, args.type, args.volumes, args.with_optional)

if __name__ == "__main__":
    main()
