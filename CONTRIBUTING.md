# 贡献指南

感谢你对 **Novel Arch** 项目的关注！我们欢迎任何形式的贡献。

---

## 🎯 如何贡献

### 1. 报告 Bug 🐛

如果你发现了 Bug，请[创建 Issue](https://github.com/ahao0625/novel-arch-skill/issues/new?template=bug_report.md)，并包含以下信息：

- **Bug 描述**：简要描述问题
- **复现步骤**：如何触发这个 Bug
- **预期行为**：你期望发生什么
- **实际行为**：实际发生了什么
- **环境信息**：
  - Trae IDE 版本
  - 操作系统 (macOS/Windows/Linux)
  - 使用示例

### 2. 提出新功能 💡

如果你有新功能的想法，请[创建 Issue](https://github.com/ahao0625/novel-arch-skill/issues/new?template=feature_request.md)，并包含：

- **功能描述**：详细描述你的想法
- **使用场景**：这个功能能解决什么问题
- **替代方案**：是否有其他实现方式

### 3. 提交代码贡献 💻

#### 步骤一：Fork 本仓库

点击 GitHub 页面右上角的 **"Fork"** 按钮。

#### 步骤二：克隆你的 Fork

```bash
git clone https://github.com/ahao0625/novel-arch-skill.git
cd novel-arch-skill
```

#### 步骤三：创建分支

```bash
git checkout -b feature/你的功能名称
# 或者
git checkout -b fix/你修复的Bug名称
```

#### 步骤四：进行更改

- **添加新功能**：修改 `SKILL.md` 或添加新文件
- **修复 Bug**：确保问题被解决
- **完善文档**：改进 `README.md` 或添加示例

#### 步骤五：提交更改

```bash
git add .
git commit -m "feat: 添加了一个很棒的功能"
# 或者
git commit -m "fix: 修复了某个问题"
```

**Commit 消息规范**：

| 类型 | 说明 |
|------|------|
| `feat:` | 新功能 |
| `fix:` | Bug 修复 |
| `docs:` | 文档更新 |
| `style:` | 代码格式（不影响功能）|
| `refactor:` | 重构（既不是新功能也不是Bug修复）|
| `test:` | 添加测试 |
| `chore:` | 构建过程或辅助工具的变动 |

#### 步骤六：推送到你的 Fork

```bash
git push origin feature/你的功能名称
```

#### 步骤七：创建 Pull Request

1. 访问你的 Fork 页面
2. 点击 **"Compare & pull request"** 按钮
3. 填写 PR 描述：
   - **标题**：简要描述你的更改
   - **描述**：详细说明你的更改内容
   - **关联 Issue**：如果有的话，使用 `Closes #123` 或 `Fixes #123`
4. 点击 **"Create pull request"**

---

## 📋 Pull Request 规范

### PR 标题格式

```
<type>: <description>
```

示例：
- `feat: 添加写作节奏控制指南`
- `fix: 修复自我质检清单中的错误`
- `docs: 完善使用示例`

### PR 描述模板

```markdown
## 更改内容

- 更改点1
- 更改点2

## 关联 Issue

Closes #123

## 测试说明

1. 如何测试你的更改
2. 预期结果

## 截图（可选）

如果涉及 UI 更改，请提供截图
```

---

## 📝 代码规范

### SKILL.md 编写规范

1. **结构清晰**：使用 Markdown 标题层级 (`#`, `##`, `###`)
2. **示例充分**：每个功能都要有示例
3. **语言一致**：使用中文，专业术语可保留英文
4. **格式统一**：
   - 代码块使用 \`\`\` 包裹
   - 列表使用 `-` 或 `1.`
   - 强调使用 `**粗体**` 或 `*斜体*`

### 示例格式

```markdown
### 功能名称

**说明**：简要描述功能。

**使用示例**：

\```bash
# 示例代码
\```

**注意事项**：
- 注意点1
- 注意点2
```

---

## 🧪 测试指南

在提交 PR 之前，请确保：

1. **本地测试**：在 Trae IDE 中测试你的更改
2. **兼容性测试**：确保在不同场景下都能正常工作
3. **文档检查**：确保所有更改都有相应的文档更新

### 测试清单

- [ ] 在 Trae IDE 中加载 Skill
- [ ] 测试所有更改的功能
- [ ] 检查文档是否清晰易懂
- [ ] 确保没有语法错误

---

## 📷 社区准则

### 行为准则

- **友好尊重**：尊重所有贡献者
- **包容开放**：欢迎不同背景和经验的贡献者
- **建设性反馈**：提供有帮助的、尊重的反馈
- **接受责任**：如果犯了错误，承认并纠正它

### 沟通方式

- **Issues**：用于讨论功能、报告 Bug
- **Pull Requests**：用于提交代码贡献
- **Discussions**：用于一般讨论和问答

---

## 🎉 认谢贡献者

所有贡献者都会被添加到 `README.md` 的 **贡献者** 部分。

---

## ❓ 有问题？

如果你有任何问题，请：

1. 查看 [现有 Issues](https://github.com/ahao0625/novel-arch-skill/issues)
2. 创建新的 Issue，选择 **"Question"** 标签
3. 联系维护者：[ahao0625](https://github.com/ahao0625)

---

## 📄 许可证

通过贡献此项目，你同意你的贡献将在 MIT 许可证下发布。

---

**再次感谢你的贡献！** 🎉

每一次贡献都让这个项目变得更好。
