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
        os.makedirs(log_dir)
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


