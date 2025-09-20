#!/bin/bash
set -e

# 启动三个进程到后台
uv run mcp_evil_add --reload &
PID1=$!

uv run mcp_sampling --reload &
PID2=$!

uv run mcp_rugpull --reload &
PID3=$!

uv run mcp_weather --reload &
PID4=$!

# 捕获 Ctrl+C，优雅退出
trap "kill $PID1 $PID2 $PID3 $PID4" SIGINT

# 等待所有子进程
wait
