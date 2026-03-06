#!/bin/bash

# Cursor Skills 同步脚本
# 用途：自动同步本地 skills 与 GitHub 仓库

set -e

SKILLS_DIR="$HOME/.cursor/skills-cursor"
LOG_FILE="$HOME/.cursor/skills-sync.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log() {
    echo -e "${BLUE}[${TIMESTAMP}]${NC} $1" | tee -a "$LOG_FILE"
}

success() {
    echo -e "${GREEN}✓${NC} $1" | tee -a "$LOG_FILE"
}

warning() {
    echo -e "${YELLOW}⚠${NC} $1" | tee -a "$LOG_FILE"
}

error() {
    echo -e "${RED}✗${NC} $1" | tee -a "$LOG_FILE"
}

# 检查目录是否存在
if [ ! -d "$SKILLS_DIR" ]; then
    error "Skills 目录不存在: $SKILLS_DIR"
    exit 1
fi

cd "$SKILLS_DIR"

# 检查是否是 Git 仓库
if [ ! -d ".git" ]; then
    error "不是 Git 仓库"
    exit 1
fi

log "开始同步 Cursor Skills..."

# 1. 获取远程更新
log "📥 拉取远程更新..."
if git fetch origin; then
    success "获取远程更新成功"
else
    error "获取远程更新失败"
    exit 1
fi

# 2. 检查是否有本地修改
if [[ -n $(git status -s) ]]; then
    warning "检测到本地修改"
    
    # 显示修改的文件
    echo ""
    git status -s
    echo ""
    
    # 提交本地修改
    log "📝 提交本地修改..."
    git add .
    
    # 生成提交信息
    COMMIT_MSG="Auto-sync: $(date '+%Y-%m-%d %H:%M:%S')"
    
    if git commit -m "$COMMIT_MSG"; then
        success "本地修改已提交"
    else
        warning "没有需要提交的更改"
    fi
fi

# 3. 检查是否需要合并
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse @{u})
BASE=$(git merge-base @ @{u})

if [ "$LOCAL" = "$REMOTE" ]; then
    success "已是最新版本"
elif [ "$LOCAL" = "$BASE" ]; then
    log "📥 拉取远程更新..."
    if git pull --rebase origin main; then
        success "更新成功"
    else
        error "更新失败，可能存在冲突"
        exit 1
    fi
elif [ "$REMOTE" = "$BASE" ]; then
    log "📤 推送本地更新..."
    if git push origin main; then
        success "推送成功"
    else
        error "推送失败"
        exit 1
    fi
else
    warning "本地和远程都有更新，尝试合并..."
    if git pull --rebase origin main; then
        success "合并成功"
        if git push origin main; then
            success "推送成功"
        else
            error "推送失败"
            exit 1
        fi
    else
        error "合并失败，请手动解决冲突"
        exit 1
    fi
fi

# 4. 显示当前状态
echo ""
log "📊 当前状态："
git log -1 --oneline
echo ""

success "同步完成！"
