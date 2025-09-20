# 使用官方 Python 3.11 作为基础镜像
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 复制本地文件到容器
COPY requirements.txt .

# 安装依赖
RUN pip install  -r requirements.txt # -i http://mirrors.tencentyun.com/pypi/simple --trusted-host mirrors.tencentyun.com

# 复制应用代码
COPY . .

# 指定容器启动时运行的命令
CMD ["python","app.py"]