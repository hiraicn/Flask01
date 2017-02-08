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

if __name__ == '__main__':
    app.run(debug=True)