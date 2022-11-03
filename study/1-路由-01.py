# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/15-19:34
# @File:1-路由-01.py
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


# 1.基本带参路由
# <name> 后续要传递的参数， 一个参数的路由
# @app.route('/show/<name>')
# def show1(name):
#     # 函数中，name表示的就是手动在地址栏上传递过来的数据
#     return "<h1>Hello ~ {}</h1>".format(name)


# 2.带多个参数的路由  连个参数的路由
# 在<>中的参数必须跟传递的相同
# @app.route('/manyShow/<title>/<page>')
# def many_show(title, page):
#     return "<h1>这是关于{}的内容，第{}页</h1>".format(title, page)


# 3.指定参数类型的路由  <int: page>: 表示page参数是一个整形的数值而非默认的字符


@app.route('/article.html/<title>/<float:page>')
def many_show(title, page):
    return f"<h1>你用的{escape(title)}的版本号是{escape(page)}</h1>"

    # return "<h1>这是关于%s的内容，第%d页</h1>" % (title, page)
    # 以占位符的方式来接收参数，只能是字符串类型
    # page 此时为整形，并非字符串
    # Flask 中所支持的类型转换器
    # 缺省（默认不写的）     字符串型
    # int:                整形
    # float:              浮点型
    # path:               字符串型， 但允许有 /


if __name__ == '__main__':
    app.run(debug=True)
