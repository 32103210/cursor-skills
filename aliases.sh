#!/bin/bash

# Cursor Skills 快捷命令别名
# 使用方法：将以下内容添加到 ~/.zshrc 或 ~/.bashrc
#
# source ~/.cursor/skills-cursor/aliases.sh

# 同步 skills
alias skills-sync='~/.cursor/skills-cursor/sync-skills.sh'

# 查看同步日志
alias skills-log='tail -f ~/.cursor/skills-sync.log'

# 查看最近 20 条日志
alias skills-log-recent='tail -20 ~/.cursor/skills-sync.log'

# 进入 skills 目录
alias skills-cd='cd ~/.cursor/skills-cursor'

# 查看 skills 状态
alias skills-status='cd ~/.cursor/skills-cursor && git status'

# 快速提交并推送
alias skills-push='cd ~/.cursor/skills-cursor && git add . && git commit -m "Update skills: $(date +%Y-%m-%d)" && git push'

# 拉取最新
alias skills-pull='cd ~/.cursor/skills-cursor && git pull'

# 查看提交历史
alias skills-history='cd ~/.cursor/skills-cursor && git log --oneline -10'

echo "Cursor Skills 别名已加载 ✓"
echo "可用命令: skills-sync, skills-log, skills-cd, skills-status, skills-push, skills-pull"
