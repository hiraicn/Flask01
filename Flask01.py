# -*- coding: utf-8 -*-

#!/usr/bin/python

from flask import Flask
import json

app = Flask(__name__)     #创建一个wsgi应用

@app.route('/')           #添加路由：根
def hello_world():
    return 'Hello World!' #输出一个字符串

@app.route('/hello')
def do_hello():
    return '<h1>Hello, strange!'

@app.route('/json')
def do_json():
    hello = {"name":"strange","say":"hello"}
    return json.dumps(hello)

if __name__ == '__main__':
    app.run(debug=True)             #启动app的调试模式