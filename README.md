# Cursor Skills 个人技能库

这是我的个人 Cursor Agent Skills 集合，用于在不同环境间同步。

## 📦 包含的 Skills

### 基础工具
- **create-rule**: 创建 Cursor 规则，用于持久化 AI 指导
- **create-skill**: 创建新的 Agent Skill
- **update-cursor-settings**: 修改 Cursor/VSCode 用户设置

### 专业工具
- **ljg-paper**: 论文深读器，执行学术论文分析管线

## 🚀 快速开始

### 在新环境中安装

```bash
# 备份现有配置（如果有）
mv ~/.cursor/skills-cursor ~/.cursor/skills-cursor.backup

# 克隆仓库
git clone <your-repo-url> ~/.cursor/skills-cursor
```

### 更新 Skills

```bash
cd ~/.cursor/skills-cursor
git pull
```

### 添加新 Skill

```bash
cd ~/.cursor/skills-cursor
mkdir my-new-skill
cd my-new-skill
# 创建 SKILL.md 文件
git add .
git commit -m "Add new skill: my-new-skill"
git push
```

## 🔧 环境特定配置

如果某个 skill 在不同环境需要不同配置：

1. 创建 `SKILL.local.md` 文件（不会被同步）
2. 在 `SKILL.md` 中引用环境特定配置

## 📝 同步说明

- 通用配置文件会自动同步
- `*.local.md` 文件不会同步（环境特定）
- 定期 `git pull` 获取最新更新

## 🛠️ 维护

```bash
# 查看状态
git status

# 提交更改
git add .
git commit -m "Update skills"
git push

# 同步最新
git pull
```

## 📄 许可

个人使用
