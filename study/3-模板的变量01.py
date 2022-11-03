# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/26-14:38
# @File:3-模板的变量01.py
"""
1.模板中的变量
- 变量是一种特殊的占位符，告诉模板引擎 该位置的值是从渲染模板时传递的数据中来获取的
@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)
    # name 和 movies 就是要传递到index.html中的占位变量

在模板中：
    {{变量名}}  模板中要动态传入的占位变量
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/first')
def index():
    return render_template('FirstTemplate.html', title='My First Template', )


if __name__ == '__main__':
    app.run(debug=True)
