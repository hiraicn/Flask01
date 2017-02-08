# -*- coding: utf-8 -*-

#!/usr/bin/python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username     # 显示用户名称

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id      # 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据

@app.route('/project/')     # 斜线只可少写不可多写，有助于避免搜索引擎索引同一个页面两次
def project():
    return 'The project page'

@app.route('/about')        # 建议采用这种
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])       #给 route() 装饰器提供 methods 参数
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()



if __name__ == '__main__':
    app.run(debug=True)