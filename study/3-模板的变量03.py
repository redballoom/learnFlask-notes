# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/26-22:32
# @File:3-模板的变量03.py

# 尝试传入不同的数据类型

from flask import Flask, render_template

app = Flask(__name__)


class LOLHero(object):
    def __init__(self):
        self.name = None

    def say(self):
        return '这是英雄信息~'


@app.route('/index')
def index():
    # 字符串类型
    title = '不同数据类型的模板传参'
    # 列表类型
    lists_data = ['提莫', '璐璐', '小法师', '小炮手', '波比']
    # 元组类型
    tuples_data = ('疾风剑豪', '暗裔剑魔', '无双剑姬', '无极剑圣')
    # 字典类型
    dicts_data = {
        '疾风剑豪': '亚索',
        '暗裔剑魔': '亚托克斯',
        '无双剑姬': '菲奥娜',
        '无极剑圣': '易',
    }
    # 类方法 （对象）
    hero = LOLHero()
    hero.name = '披甲龙龟'

    return render_template('differentDataTemplate.html', test_data=locals())


if __name__ == '__main__':
    app.run(debug=True)
