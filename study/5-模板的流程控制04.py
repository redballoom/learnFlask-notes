# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/29-0:16
# @File:5-模板的流程控制04.py

# 模板的包含
#     如 header 和 footer 可以单独拆出来，谁用我们引用就好啦，可以减少代码量

# 在多处重复使用的模板代码可以放在单独的文件中，可以被其他的模板所包含（引用）

# {% include 'xxx.html' %}  这段代码写在哪儿，哪里就调用该模板内容


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    uname = '小熊维尼'

    return render_template('index-2.html', test_data=locals())


if __name__ == '__main__':
    app.run(debug=True)


