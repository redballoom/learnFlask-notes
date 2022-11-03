# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/11/1-21:01
# @File:10-修改模板的配置.py

"""模板的配置:
1. 修改配置
    修改flask中默认的templates和static文件夹
    app = flask(__name__,
                template_folder='你要修改的模板文件夹名称',
                static_url_path='你要修改的静态文件访问路径'
                static_folder='你要修改的静态文件夹名称'

template_folder : 设置模板的保存目录
static_url_path : 设置静态文件的访问路径（映射到WEB中的访问路径）
static_folder : 设置静态文件的保存目录（映射到项目中的目录名称）

"""
# # from flask import Flask
# #
# # app = Flask(__name__)
# #
# #
# # @app.route('/')
# # def index():
# #     return "This is index page"
# #
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
