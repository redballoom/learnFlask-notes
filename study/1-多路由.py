# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/10-20:00
# @File:1-多路由.py
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '这是首页'


@app.route('/login')
def login():
    return '这是登录页面'


@app.route('/info')
def page_info():
    return '这是内容页面信息'


if __name__ == '__main__':
    app.run(debug=True)
