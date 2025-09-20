# server.py
import datetime
import os

from fastmcp import FastMCP,Context
from common.utils import setup_logging,send_message_all_in_one
from common.config import Config

mcp_sampling = FastMCP("mcp_sampling_demo")

@mcp_sampling.tool()
async def analyze_sentiment(text: str, ctx: Context) -> dict:
    """
    使用客户端的 LLM 来分析情感（示例：返回 'positive'/'negative'/'neutral'）
    """
    # 可以直接传字符串 prompt，或传 messages（参考官方 API 支持）
    prompt = f"""Analyze the sentiment of the following text as positive, negative, or neutral.
Just output a single word: positive, negative, or neutral.
Text: {text}"""

    # 调用采样：会发送请求到 client，由 client 的 sampling_handler 实际调用 LLM
    response = await ctx.sample(prompt, temperature=0.0, max_tokens=20)

    # response 通常是 TextContent，主要取 .text
    sentiment_text = response.text.strip().lower()
    if "positive" in sentiment_text:
        sentiment = "positive"
    elif "negative" in sentiment_text:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {"text": text, "sentiment": sentiment}

if __name__ == "__main__":
    # 本地开发建议使用 stdio transport 或默认 run()，文档中有多种运行 & 部署方式
    # mcp.run(transport="stdio")
    # mcp_sampling.run()
    # 最安全的写法：用 asyncio.run 包裹
    import asyncio
    asyncio.run(mcp_sampling.run())
