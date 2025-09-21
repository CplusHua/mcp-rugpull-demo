# 使用官方 Python 3.11 作为基础镜像
FROM python:3.12

# 设置工作目录
WORKDIR /app

# 复制本地文件到容器
COPY . .

# 安装依赖
RUN pip install uv
RUN uv sync
EXPOSE 8000-8010


# 指定容器启动时运行的命令
CMD ["./start.sh"]