#!/bin/bash
# novel-arch-skill install.sh
# 安装 novel-arch 技能到 WorkBuddy user skills 目录

set -e

SKILL_NAME="novel-arch"
SKILL_SRC="$(cd "$(dirname "$0")" && pwd)"
SKILL_DST="$HOME/.workbuddy/skills/$SKILL_NAME"

echo "📦 正在安装 novel-arch 技能..."
echo "   源: $SKILL_SRC"
echo "   目标: $SKILL_DST"

# 创建目标目录
mkdir -p "$SKILL_DST/scripts" "$SKILL_DST/references"

# 复制核心文件
cp "$SKILL_SRC/SKILL.md" "$SKILL_DST/"
cp "$SKILL_SRC/scripts/setup_project.py" "$SKILL_DST/scripts/"
cp "$SKILL_SRC/references/ai-novel-architecture.md" "$SKILL_DST/references/"
cp "$SKILL_SRC/references/ai-operations-manual.md" "$SKILL_DST/references/"

echo ""
echo "✅ 安装完成！技能已安装至: $SKILL_DST"
echo ""
echo "📖 使用方法："
echo ""
echo "   WorkBuddy 用户："
echo "     在对话中输入以下指令触发："
echo "     - \"新建一个小说项目\""
echo "     - \"按照架构方案创建项目\""
echo "     - \"初始化新书\""
echo ""
echo "   其他 AI 平台用户："
echo"     将 references/ai-operations-manual.md 的内容粘贴到 AI 对话中作为指令。"
echo "     AI 会自动按手册执行。"
