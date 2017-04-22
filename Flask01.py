# -*- coding: utf-8 -*-

#!/usr/bin/python

from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/agent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/hello')
def hello_world():
    return '<h1>Hello World!</h1>'

# 显示用户名称
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User: %s' % username

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

# 第3节习题
@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    return '%d' %(a+b)

# 第4节习题
@app.route('/lesson4')
def lesson4():
    return render_template('lesson4.html')

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # 当请求形式为“GET”或者认证失败则执行以下代码
#     return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)