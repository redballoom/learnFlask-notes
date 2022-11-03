# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/28-22:43
# @File:5-模板的流程控制03.py

# 宏 就是在模板中声明的函数/方法，可以直接在模板中调用
# 使用：
# 声明
# {% macro show(img1)%} #标签声明宏
# <img src='{{img1}}'>
# {% endmacro %}


# 为了代码的整洁和 方便重复使用，允许将宏放在单独的模板文件中声明定义
# 1.创建一个macro.html
# 2.在别的页面调用
#     导入 macro.html
#         {% import 'macro.html' as macros %}\
#     调用语句
#         {% macros.show(args) %}

# 调用
# {{show(args)}}


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    uname = '小熊维尼'
    lists = [f'这是第{i}段' for i in range(10)]

    # 图片链接列表
    img_list = [
        'https://c2.im5i.com/2022/10/06/jtdol.jpg',
        'https://c2.im5i.com/2022/10/06/jtGxJ.jpg',
        'https://c2.im5i.com/2022/10/06/jthnz.jpg',
        'https://c2.im5i.com/2022/10/06/jtwM5.jpg',
        'https://c2.im5i.com/2022/10/06/jbmNS.jpg',
    ]
    return render_template('templates-fun.html', test_data=locals())


if __name__ == '__main__':
    app.run(debug=True)
