# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/26-17:26
# @File:3-模板的变量02.py

"""英雄技能信息的案例"""
from flask import Flask, render_template

app = Flask(__name__)


# 这里英雄为亚索
@app.route('/hero/<hero_name>')
def hero_info(hero_name=None):
    # return render_template('heroInformation.html', title='{}的技能名称'.format(hero_name),
    #                        name=hero_name, skill1='斩钢闪', skill2='风之壁障', skill3='踏前斩', skill4='狂风绝息斩')
    # 简单粗暴的传参,技能现在先写死

    # dic_data = {
    #     'title': f'{hero_name}的技能名称',
    #     'name': hero_name,
    #     'skill1': '斩钢闪',
    #     'skill2': '风之壁障',
    #     'skill3': '踏前斩',
    #     'skill4': '狂风绝息斩',
    # }
    # return render_template('heroInformation.html', hero_data=dic_data)

    # 更方便的方法
    title = f'{hero_name}的技能名称'
    name = hero_name
    skill1 = '斩钢闪'
    skill2 = '风之壁障'
    skill3 = '踏前斩'
    skill4 = '狂风绝息斩'
    # print(locals())
    # {'hero_name': '亚索', 'title': '亚索的技能名称', 'name': '亚索' ...}
    # locas() 作用以字典的方式创建变量 局部的变量名为key,值为value.
    return render_template('heroInformation.html', hero_data=locals())


if __name__ == '__main__':
    app.run(debug=True)