# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/9/15-23:22
# @File:0-run.py
from flask import Flask
# 将当前运行的主程序构建成flask的应用
app = Flask(__name__)


# route Flask中的路由定义，定义用户的访问路径 “/” 在浏览器中表示根目录
@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'
    # 视图处理函数，该函数必须要有return 可以返回字符串或响应对象


if __name__ == '__main__':
    # 运行flask应用（启动Flask的服务）
    # app.run(debug=True, port=8080)
    # debug=True 是将当前的启动模式改为调试模式
    app.run(debug=True)

# http://localhost:8080 与 http://127.0.0.1:8080是一样的 默认端口:5000
