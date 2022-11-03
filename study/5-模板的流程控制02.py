# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/28-22:12
# @File:5-模板的流程控制02.py

# 模板的 for 控制结构

# 模板中的for控制结构
# {% for 变量 in 可迭代对象(list/tuple/dict/set/str...) %}
#     中间写循环体
# {% endfor %}

from random import choice
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/page')
def index():
    uname = '披甲龙龟'
    # 随机 abcd
    lis = ['A', 'B', 'C', 'D']
    random_word = [choice(lis) for _ in range(10)]

    # 用模板的for来遍历该字典
    dicts_data = {
        '疾风剑豪': '亚索',
        '暗裔剑魔': '亚托克斯',
        '无双剑姬': '菲奥娜',
        '无极剑圣': '易',
    }
    return render_template('Process-control-for.html', test_data=locals())


if __name__ == '__main__':
    app.run(debug=True)

