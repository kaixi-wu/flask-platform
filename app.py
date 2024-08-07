import json
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.get('/login')
def login():
    return "login success!"


name = ['bryant', 'jeremy']
age = [39, 45]


def login_post(post_name):
    # data = {}
    # for n, a in zip(name, age):
    #     data[n] = a
    # json_data = json(data)
    return post_name + "world!!"


@app.post('/login/<post_name>')
def post_login(post_name: str):
    # result = login_post(post_name)
    return login_post(post_name)


user = {"admin", "password123"}
_LOGIN_ERROR = 'username or password error!'


@app.post("/loginInfo/<username>/<password>")
def login_assert(username, password):
    if request.method == 'POST':
        print("username:{1},password:{0}".format(password, username))
        # if (username == list(user.keys())[0]) & (password == list(user.values())[0]):
        if username == list(user)[0] and password == list(user)[1]:
            return "user {} login success!!".format(username)
        else:
            print("username:{1},password:{0}".format(password, username))
            return _LOGIN_ERROR
    else:
        return "req method not post!"


if __name__ == '__main__':
    app.run()
