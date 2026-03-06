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

### 快速同步（推荐）

```bash
# 一键同步（自动拉取、提交、推送）
~/.cursor/skills-cursor/sync-skills.sh
```

### 手动操作

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

## ⚙️ 自动同步设置

### 方式 1：使用安装脚本（推荐）

```bash
~/.cursor/skills-cursor/install-auto-sync.sh
```

提供两种定时方案：
- **launchd** (macOS 推荐)：系统级定时任务，每小时自动同步
- **cron**：传统定时任务，每小时自动同步

### 方式 2：手动配置 launchd

```bash
# 创建配置文件
cat > ~/Library/LaunchAgents/com.cursor.skills-sync.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.cursor.skills-sync</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/你的用户名/.cursor/skills-cursor/sync-skills.sh</string>
    </array>
    <key>StartInterval</key>
    <integer>3600</integer>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
EOF

# 加载任务
launchctl load ~/Library/LaunchAgents/com.cursor.skills-sync.plist
```

### 方式 3：添加快捷命令

在 `~/.zshrc` 或 `~/.bashrc` 中添加：

```bash
# 加载 skills 别名
source ~/.cursor/skills-cursor/aliases.sh
```

然后就可以使用：
- `skills-sync` - 同步 skills
- `skills-log` - 查看同步日志
- `skills-cd` - 进入 skills 目录
- `skills-status` - 查看 Git 状态
- `skills-push` - 快速提交并推送
- `skills-pull` - 拉取最新更新

## 📊 查看日志

```bash
# 实时查看同步日志
tail -f ~/.cursor/skills-sync.log

# 查看最近日志
tail -20 ~/.cursor/skills-sync.log
```

## 📄 许可

个人使用
