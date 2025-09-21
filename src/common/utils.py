# -*- coding: utf-8 -*-
import logging
import os
import sys
import time
from logging.handlers import RotatingFileHandler
from common.config import Config


# 写一个各个类都可以自动调用的日志处理函数
def setup_logging():
    # 配置日志
    logger = logging.getLogger(__name__)
    logger.setLevel(Config.get("LOG_LEVEL", "INFO"))
    # 创建日志目录
    log_dir = Config.get("LOG_DIR")
    if not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir)
        except FileExistsError:
            # 多模块竞争创建目录时可能会出现此错误，忽略即可
            pass
    # 创建日志文件
    log_file = os.path.join(log_dir, "mcp.log")
    # 创建日志处理器
    handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
    # 创建日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # 添加处理器
    logger.addHandler(handler)
    # 添加控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


# 写一个feishu webhook发送消息的函数
def send_feishu_message(message):
    # TODO: 实现发送消息到飞书的功能
    webhook_url = os.getenv("FEISHU_WEBHOOK_URL")
    if webhook_url:
        # TODO: 实现发送消息到飞书的功能
        import requests
        headers = {"Content-Type": "application/json"}
        message = str(message)
        data = {"msg_type": "text", "content": {"text": message}}
        response = requests.post(webhook_url, headers=headers, json=data)
        if response.status_code == 200:
            logging.info("消息发送成功")
        else:
            logging.error("消息发送失败，错误码：%s，错误信息：%s", response.status_code, response.text)
    else:
        logging.warning("未配置FEISHU_WEBHOOK_URL，无法发送消息到飞书")
        return False
    return True

def send_message_all_in_one(message):
    message = message.replace("\n", "\\n")
    if type(message) == str:
        pass
    else:
        message = str(message)
    return send_feishu_message(message)
