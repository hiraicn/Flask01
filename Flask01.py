from flask import Flask

app = Flask(__name__)


@app.route('/user/<user>')
def hello_world(user):
    return 'Hello %s' % user


if __name__ == '__main__':
    app.run()
