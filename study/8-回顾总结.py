# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/30-12:48
# @File:8-回顾总结.py
"""
一、 模板的语法：
    1.变量（占位变量）
        在视图中
            return render_template('xxx.html', variable1=arg1,variable2=arg2 ...)
            不美观，且臃肿。
            return render_template('xxx.html', params=locals())
            通过locals()方法把变量映射成字典来使用。

            允许传递到模板中使用的变量类型：
            数字， 字符串， 字典， 列表， 元组， 对象
            在模板中的用法：
                {{变量}}
                {{uname}}
                如果是用locals()方法创建的变量
                {{params.num}}
                {{params.list[1]}} or {{params.list.1}}
                对象：先实例化后再调用
                    类属性：{{params.hero.name}} 参考之前
                    类方法：{{params.hero.say()}}


    2.过滤器
        在变量输出之前改变变量的值
        {{变量 | 过滤器}}
        {{str | length}} 字符长度
        {{str | lower}}  字符小写
        {{str | title}}  字符每个单词首字母大写
        {{str | trim}}   去除字符前后空格
        ...
        有很多，具体自己去官网看看，包含python字符串中的一些方法啥的


    3.模板中的控制结构
        3-1 if 结构
            {% if 条件 %}
                要执行的代码
            {% endif %}

        3-2 if-else 结构
            {% if 条件 %}
                要执行的代码
            {% else %}
                要执行的代码
            {% endif %}

        3-3 for 结构
            {% for 变量 in 列表，元组，字典等可迭代对象 %}
            {% endfor %}


    4.模板中的宏（函数/方法）可复用的
        声明：
        {% macro 函数名() %}
            一些重复的代码（html/结构/变量...）
        {% endmacro%}

        调用：
        {{函数名()}}
        通常将宏单独放在一个文件中，哪里用哪里调用。
        1.创建网页：macro.html
        2.在要使用的网页文件中导入 macro.html
        {% import 'macro.html' as macros %}

        {{ macros.函数名() }}


    5.模板的包含
        我们的网页的头，尾。在实际开发中不可能每次都复制吧，这样代码不仅多还难维护，所以有了包含，把头 header和尾 footer 单独抽离出来分别保存到文件
        一些写死的不变的html内容，且又要在不同页面重复出现的，都可以使用这个方法。
        {% include 'xxx.html' %}


    6.静态文件
        在项目目录中，我们需要把所有静态文件存放在 static 文件夹中 (手动创建) 专业版直接创建Flask项目

        在模板中访问静态文件
        /static/images/xxx.jpg
        /static/js/xxx.js
        ...
        正向解析：<img src="/static/images/xxx.jpg" alt="">
        反向解析：<img src={{url_for('static', filename='images/xxx.jpg')}} alt="">


    7.模板的继承 （使用模板且需要小改动时）
        1.父级模板中
            {% block 块名 %}
                要在子模板中修改或重新的内容
            {% endblock %}
            block: 定义在子模版中允许被修改的内容部分,
                1.这部分在父模板中正常显示,不影响什么的
                2.而在子模版中允许被重写或修改

        2.子模板中
            使用 {% extends '父模板的名称(html)'%} 来实现模板的继承
            使用 {% block 块名 %}
                    ...
                {% endblock %}
            来覆盖父模板中的同名内容

            允许使用 {{super()}} 来继续调用父模板中的 block 块中的内容
            使用场景: 在不希望父模板中内容完全被覆盖,而是需要在其前后添加一些内容时可以使用super()来再次调用父模板中被覆盖的部分
"""