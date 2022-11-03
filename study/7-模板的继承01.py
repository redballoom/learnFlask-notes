# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/30-13:57
# @File:7-模板的继承.py

# 模板的继承
#     类似于类的继承，如果在一个模板中出现的大量内容是另外一个模板的话，那么就可以使用继承的方式来简化开发
# 语法:
# 在父模板中
# 需要定义出现哪些内容在子模板中是可以被重写的
# {% block 块名 %}
# {% endblock %}

# block: 定义允许在子模板中被修改的内容
# 1.在父模板中正常显示,没有任何影响
# 2.在子模板中可以被重写(修改)


# 子模板中
#     使用 {% extends '父模板的名称' %} 来完成继承
#     使用 {% block 块名 %} 来重写父模板中的同名内容
# {% block 块名 %}
#     要覆盖父模板的内容
# {% endblock %}


# 允许通过{{super()}}来调用父模板中的内容
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/parent')
def index():
    return render_template('extends-parent.html', test_data=locals())


@app.route('/child')
def page():
    return render_template('extends-child.html', test_data=locals())


if __name__ == '__main__':
    app.run(debug=True)