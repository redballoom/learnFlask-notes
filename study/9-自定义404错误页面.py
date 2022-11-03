# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/30-15:37
# @File:9-自定义404错误页面.py

"""
# 自定义错误页面使用方式
# 1.404 的错误页面
@app.errorhandler(404)
def page_notFound(e):
    return render_template('404.html'),404


# 2. 500 的错误处理
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'),500

"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '这是首页'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)


