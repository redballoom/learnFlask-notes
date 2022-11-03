# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/26-14:03
# @File:3-总结.py

"""
1.搭建结构
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=1111)  # port指定端口

这样就是一个最简易的程序


2.路由
@app.route()  装饰器来设置访问路径
@app.route('/')  表示访问路径 /
def ...

@app.route('/index')  表示访问路径 /index
def ...

@app.route('/user/info-page')  表示访问路径 /user/info-page
def ...

@app.route('/user/<name>')  表示访问路径 /user/xxx  xxx:是在地址栏里传入的参数名
def user(name):
    return ''

@app.route('/user/<int:age>')  表示访问路径 /user/xxx  <int:age> 是指定了参数的类型  必须是类型转换器所支持的类型
def user(age):
    return ''
# Flask 中所支持的类型转换器：
# 缺省（默认不写的）     字符串型   不允许有 /
# int:                整形
# float:              浮点型
# path:               字符串型， 但允许有 /


3.路由的反向解析
url_for(funName, arg1=value1, arg2=value2)
    funName: 要反向生成地址的函数名
    arg1: 要传递给url的参数名和值
    ...


4.Templates - 模板
（用动态的方式来更新网页等）
- 模板的设置：
    Flask 默认会从程序实例所在模块同级目录的 templates 文件夹中寻找模板
- 渲染模板：
    使用 render_template() 函数可以把模板渲染出来，必须传入的参数为模板文件名 index.html
    使用语法：
        render_template('index.html', arg1=value1, arg2=value2)
        必须参数： 'index.html'
        可选参数： arg1 ...  要传递的模板变量占位符


"""