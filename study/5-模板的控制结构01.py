# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/28-21:31
# @File:5-模板的控制结构01.py

# 模板的if控制结构

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/page')
def index():
    uname = '披甲龙龟'
    return render_template('Process-control-if.html', test_data=locals())


@app.route('/info')
def info():
    return '<img src="https://p1.ssl.qhimg.com/t014ee57f018c046471.jpg">'


@app.route('/login')
def login():
    return '这是登录页面'


if __name__ == '__main__':
    app.run(debug=True)


# 模板中的if控制结构
# {% if 条件 %}
#     中间写为True执行的代码
# {% else %}
#     中间写为False执行的代码
# {% endif %}
