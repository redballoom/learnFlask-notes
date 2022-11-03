# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/15-20:15
# @File:1-路由-02.py
from flask import Flask

# 1.多URL的路由匹配
# 允许在一个视图处理函数中设置多个url路由规则

app = Flask(__name__)


@app.route('/')
@app.route('/index')
# 就是根路径和根路径下index都展示同一页面 --> 首页
def index():
    return '<h1>这是首页</h1>'


if __name__ == '__main__':
    app.run(debug=True)