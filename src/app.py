# -*- coding: utf-8 -*-
from starlette.applications import Starlette
from starlette.routing import Mount, Host
from starlette.staticfiles import StaticFiles
from pathlib import Path


from common.utils import setup_logging
from libs.malicious_mcp_rugpull import mcp_rugpull
from libs.mcp_model_sampling import mcp_sampling
# 设置日志
logger = setup_logging()

def run_server_mcp_evil_add():
    # Mount the SSE server to the existing ASGI server
    # mcp_evil 是mcp_rugpull禁用log_mcp_tool_usage工具后的版本
    mcp_evil = mcp_rugpull
    mcp_evil.remove_tool("log_mcp_tool_usage")
    mcp_evil.remove_tool("get_weather")
    # mcp_evil.remove_tool("send_message")

    app = Starlette(
        routes=[
            # 静态文件托管，访问 /static/... 会读取 local_dir/static/ 下的文件
            Mount('/static', app=StaticFiles(directory=Path(__file__).parent/'static'), name='static'),
            Mount('/', app=mcp_rugpull.sse_app()),

        ]
    )
    # Run the app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
def run_server_mcp_get_weather():
    # Mount the SSE server to the existing ASGI server
    mcp_rugpull.remove_tool("add")
    mcp_rugpull.remove_tool("send_message")
    mcp_rugpull.remove_tool("log_mcp_tool_usage")

    app = Starlette(
        routes=[
            # 静态文件托管，访问 /static/... 会读取 local_dir/static/ 下的文件
            Mount('/static', app=StaticFiles(directory=Path(__file__).parent/'static'), name='static'),
            Mount('/', app=mcp_rugpull.sse_app()),

        ]
    )
    # Run the app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
def run_server_mcp_rugpull():
    # Mount the SSE server to the existing ASGI server
    mcp_rugpull.remove_tool("add")
    mcp_rugpull.remove_tool("send_message")
    mcp_rugpull.remove_tool("get_weather")
    app = Starlette(
        routes=[
            # 静态文件托管，访问 /static/... 会读取 local_dir/static/ 下的文件
            Mount('/static', app=StaticFiles(directory=Path(__file__).parent/'static'), name='static'),
            Mount('/', app=mcp_rugpull.sse_app()),

        ]
    )
    # Run the app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)

def run_server_mcp_sampling():
    # Mount the SSE server to the existing ASGI server
    app = Starlette(
        routes=[
            # 静态文件托管，访问 /static/... 会读取 local_dir/static/ 下的文件
            Mount('/static', app=StaticFiles(directory=Path(__file__).parent/'static'), name='static'),
            Mount('/', app=mcp_sampling.sse_app()),

        ]
    )
    # Run the app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
if __name__ == '__main__':
    run_server_mcp_rugpull()


