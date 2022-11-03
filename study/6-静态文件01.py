# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/29-13:24
# @File:6-静态文件01.py

# 静态文件：css, js, 图片, 视频, 音频等。
# 静态文件的处理：
#     所有的静态文件都默认保存在项目文件夹中的 static 文件夹中，在访问静态文件时需要通过 /static/资源路径 来进行访问
# 静态文件的路径反向解析
#     url_for('static', filename='ahri.jpg')


from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    # 反向解析方式一
    # link=url_for('static', filename='images/ahri.jpg')
    return render_template('static-01.html', test_data=locals())


if __name__ == '__main__':
    app.run(debug=True)