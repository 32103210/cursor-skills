#!/bin/bash

# 安装自动同步脚本
# 提供多种定时同步方案

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}=== Cursor Skills 自动同步安装程序 ===${NC}\n"

SKILLS_DIR="$HOME/.cursor/skills-cursor"
SYNC_SCRIPT="$SKILLS_DIR/sync-skills.sh"

# 检查同步脚本是否存在
if [ ! -f "$SYNC_SCRIPT" ]; then
    echo -e "${YELLOW}错误：找不到同步脚本${NC}"
    exit 1
fi

echo "请选择自动同步方式："
echo ""
echo "1) launchd (macOS 推荐) - 系统级定时任务"
echo "2) cron - 传统定时任务"
echo "3) 手动运行（不安装自动同步）"
echo ""
read -p "请选择 [1-3]: " choice

case $choice in
    1)
        echo -e "\n${BLUE}安装 launchd 定时任务...${NC}"
        
        # 创建 launchd plist 文件
        PLIST_FILE="$HOME/Library/LaunchAgents/com.cursor.skills-sync.plist"
        
        cat > "$PLIST_FILE" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.cursor.skills-sync</string>
    
    <key>ProgramArguments</key>
    <array>
        <string>$SYNC_SCRIPT</string>
    </array>
    
    <key>StartInterval</key>
    <integer>3600</integer>
    
    <key>RunAtLoad</key>
    <true/>
    
    <key>StandardOutPath</key>
    <string>$HOME/.cursor/skills-sync.log</string>
    
    <key>StandardErrorPath</key>
    <string>$HOME/.cursor/skills-sync-error.log</string>
</dict>
</plist>
EOF
        
        # 加载 launchd 任务
        launchctl unload "$PLIST_FILE" 2>/dev/null || true
        launchctl load "$PLIST_FILE"
        
        echo -e "${GREEN}✓ launchd 任务已安装${NC}"
        echo -e "  - 每小时自动同步一次"
        echo -e "  - 日志文件: ~/.cursor/skills-sync.log"
        echo -e "  - 错误日志: ~/.cursor/skills-sync-error.log"
        echo ""
        echo "管理命令："
        echo "  查看状态: launchctl list | grep cursor"
        echo "  停止同步: launchctl unload $PLIST_FILE"
        echo "  启动同步: launchctl load $PLIST_FILE"
        echo "  立即运行: launchctl start com.cursor.skills-sync"
        ;;
        
    2)
        echo -e "\n${BLUE}安装 cron 定时任务...${NC}"
        
        # 检查是否已存在
        if crontab -l 2>/dev/null | grep -q "sync-skills.sh"; then
            echo -e "${YELLOW}⚠ cron 任务已存在，跳过安装${NC}"
        else
            # 添加到 crontab（每小时执行一次）
            (crontab -l 2>/dev/null; echo "0 * * * * $SYNC_SCRIPT >> $HOME/.cursor/skills-sync.log 2>&1") | crontab -
            
            echo -e "${GREEN}✓ cron 任务已安装${NC}"
            echo -e "  - 每小时自动同步一次"
            echo -e "  - 日志文件: ~/.cursor/skills-sync.log"
            echo ""
            echo "管理命令："
            echo "  查看任务: crontab -l"
            echo "  编辑任务: crontab -e"
            echo "  删除任务: crontab -e (然后删除对应行)"
        fi
        ;;
        
    3)
        echo -e "\n${YELLOW}跳过自动同步安装${NC}"
        echo "手动运行命令: $SYNC_SCRIPT"
        ;;
        
    *)
        echo -e "\n${YELLOW}无效选择${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}=== 安装完成 ===${NC}"
echo ""
echo "快速命令："
echo "  手动同步: ~/.cursor/skills-cursor/sync-skills.sh"
echo "  查看日志: tail -f ~/.cursor/skills-sync.log"
echo ""
