import json
from flask import Flask, jsonify, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = b'u7j*76783NF'


@app.route('/', methods=['POST', 'GET'])
def index():  # put application's code here
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        app.logger.info('-----------')
        data = request.get_json()
        data['businessOrderNo'] = 'OR2024729471057103000'
    return jsonify(data)


name = ['bryant', 'jeremy']
age = [39, 45]


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


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
    app.run(port=8080)
