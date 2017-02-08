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

# 显示用户名称
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

# 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

# 斜线只可少写不可多写，有助于避免搜索引擎索引同一个页面两次
@app.route('/project/')
def project():
    return 'The project page'

# 建议采用这种
@app.route('/about')
def about():
    return 'The about page'

# 给 route() 装饰器提供 methods 参数
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

# 习题：输入http://127.0.0.1/sum/a/b时，其中a和b都是数字，服务器返回它们的和。
@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    return '%d' %(a+b)

if __name__ == '__main__':
    app.run(debug=True)