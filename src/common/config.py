import dotenv
import os
dotenv.load_dotenv()
# 配置参数
Config = {
    "PROXY": {
        "https": os.getenv("CWALKER_PROXY_HTTPS"),
        "http": os.getenv("CWALKER_PROXY_HTTP")
    },
    "LOG_DIR": os.getenv("LOG_DIR", "logs"),
    "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
}

