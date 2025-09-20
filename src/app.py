# -*- coding: utf-8 -*-
from starlette.applications import Starlette
from starlette.routing import Mount, Host


from common.utils import setup_logging
from libs.malicious_mcp_rugpull import mcp_rugpull
# 设置日志
logger = setup_logging()

if __name__ == '__main__':
    # Mount the SSE server to the existing ASGI server
    app = Starlette(
        routes=[
            Mount('/', app=mcp_rugpull.sse_app()),
        ]
    )
    # Run the app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


