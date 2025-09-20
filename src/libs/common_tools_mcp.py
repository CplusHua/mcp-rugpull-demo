from mcp.server.fastmcp import FastMCP
from common.utils import setup_logging
from common.config import Config
import uuid
import json
import requests
import re
from typing import Any, List, Tuple
# 设置日志
logger = setup_logging()

mcp_common_tools = FastMCP("MCP_COMMON_TOOLS")

@mcp_common_tools.tool()
def find_json_in_text(text: str) -> Tuple[bool, List[Any]]:
    """
    从文本中提取所有合法的 JSON 对象（支持嵌套）。

    参数：
        text (str): 输入的原始文本。

    返回：
        Tuple[bool, List[Any]]:
            - 第一个值为布尔类型，表示是否提取到合法 JSON；
            - 第二个值为合法 JSON 对象的列表。
    """
    results = []
    stack = []
    start_idx = None

    for i, char in enumerate(text):
        if char == '{':
            if not stack:
                start_idx = i
            stack.append(char)
        elif char == '}':
            if stack:
                stack.pop()
                if not stack and start_idx is not None:
                    candidate = text[start_idx:i+1]
                    try:
                        parsed = json.loads(candidate)
                        results.append(parsed)
                    except json.JSONDecodeError:
                        pass
                    start_idx = None

    return len(results) > 0, results



if __name__ == '__main__':
    common_tools.run(transport="sse")