#!/bin/bash

# 豆包MCP服务器启动脚本
# Doubao MCP Server Startup Script

echo "🚀 启动豆包品牌信息MCP服务器..."

# 检查Python环境
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: Python3 未安装"
    exit 1
fi

# 检查依赖
echo "📦 检查依赖..."
pip install -r requirements.txt

# 检查环境配置
if [ ! -f ".env" ]; then
    echo "⚠️  警告: .env 文件不存在，使用默认配置"
    echo "💡 提示: 复制 .env.example 并配置您的豆包API密钥"
fi

# 启动服务器
echo "🔄 启动MCP服务器..."
python3 doubao_mcp_server.py