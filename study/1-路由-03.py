# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/18-19:51
# @File:1-路由-03.py

# 路由中设置HTTP请求方法
# Flask路由设置规则也允许设置对应的请求方法，只有将匹配上请求方法的路径交给视图处理函数取执行
# 格式：
# @app.route('/post', methods=['POST'])
# def post():
#     return xxx
# * 只有post请求方式允许访问 localhost:5000/post
# from flask import Flask, url_for
#
# app = Flask(__name__)
#
#
# @app.route('/post', methods=['POST', 'GET'])
# def post():
#     # 因为页面默认请求都是get，而post是由表单产生
#     return '假装是post请求'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


# url的解析：
# 正向解析：程序自动解析，根据@app.route()中设置的访问路径来匹配处理函数
# 反向解析：通过视图处理函数的名称自动生成视图处理函数的访问路径
# Flask中提供了 url_for() 函数，用于反向解析url

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/language/<name>/<age>')
def url(name, age):
    return '<h1>您当前使用的编程语言是{}版本是{}</h1>'.format(name, age)


@app.route('/url')
def page_url():
    # 链接地址 /python 像爬虫中经常需要拼接的链接部分 这即是反向解析的url地址
    link = url_for('url', name='python', age='v-3.8')
    print(link)
    # resp = '<a href="'+link+'">'+link+'</a>'
    resp = '<a href="'+link+'">反向解析后的地址：' + link+' </a>'
    return resp


if __name__ == '__main__':
    app.run(debug=True)


# 反向解析：
# def index(name):
#     return 'name is {}.'.format(name)
#
# 1、url_for('index')  # /
# 2、url_for('index', name='3')  # index/3
