from base_enum import UserStatus, ErrorMessage as errorMessage
from werkzeug.security import check_password_hash, generate_password_hash
from ..blueprint import auth_blue
from flask import request, jsonify
from ..models.auth import User, Role
from exts import db

import functools
import logging


@auth_blue.post('/register')
def register():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            account = data.get('account')
        # print(f"data: {username}")
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif User.query.filter_by(username=username, delete=False).first():
            error = '用户已注册！'
        elif User.query.filter_by(email=email, delete=False).first():
            error = '用户已注册！'
        elif User.query.filter_by(account=account, delete=False).first():
            error = '用户已注册!'
        if error is None:
            try:
                new_user = User(username=username, email=email, account=account, password=generate_password_hash(password))
                db.session.add(new_user)
                db.session.commit()
                return "success"
            except Exception as e:
                return f"error: {e}"
    return error

#
# @auth_blue.route('/login', methods=('GET', 'POST'))
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         db = get_db()
#         error = None
#         user = db.execute(
#             'SELECT * FROM user WHERE username = ?', (username,)
#         ).fetchone()
#
#         if user is None:
#             error = 'Incorrect username.'
#         elif not check_password_hash(user['password'], password):
#             error = 'Incorrect password.'
#
#         if error is None:
#             session.clear()
#             session['user_id'] = user['id']
#             # return redirect(url_for('login_success'))
#             return "login success"
#         flash(error)
#
#     return render_template('auth/login.html')
#
#
# @auth_blue.before_app_request
# def load_logged_in_user():
#     user_id = session.get("user_id")
#     # logging.debug(request.headers)
#     # logging.debug('user_id is {}'.format(user_id))
#
#     if user_id is None:
#         g.user = None
#     else:
#         g.user = get_db().execute(
#             'SELECT * FROM user WHERE id = ?', (user_id,)
#         ).fetchone()
#         logging.debug(g.user)
#
#
# @auth_blue.route('/logout')
# def logout():
#     # session.clear()
#     # return redirect(url_for('login_out'))
#
#
# @auth_blue.route('/reset_password', methods=('GET', 'POST'))
# def reset_password():
#     # user_id = session.get('user_id')
#     if request.method == 'POST':
#         new_password = request.form['new_password']
#         old_password = request.form['old_password']
#         username = request.form['username']
#         error = None
#         if not new_password:
#             error = 'new_password is required.'
#         elif not old_password:
#             error = 'old_password is required.'
#         elif not username:
#             error = 'username is required.'
#         # 从g.user对象中取值即可
#         # user = db.execute(
#         #     'select * from user where id = ?', (user_id,)
#         # ).fetchone()
#
#         if not check_password_hash(g.user['password'], old_password):
#             return 'old password is error'
#         if old_password == new_password:
#             return "new password and old password is equal"
#         elif user_check(g.user["username"]):
#             try:
#                 logging.debug("pass {} user: {}".format(generate_password_hash(new_password), g.user['id']))
#                 logging.debug(f"update user set password = '{generate_password_hash(new_password)}' where id = {g.user['id']}")
#                 db.execute(
#                     f"update user set password = '{generate_password_hash(new_password)}' where id = {g.user['id']}")
#                 db().commit()
#                 return "user password rest success"
#             except Exception as e:
#                 db.rollback()
#                 logging.debug(e)
#                 return "重置密码失败！请重试！"
#
#     return render_template('auth/reset_password.html')
#
#
# def login_required(view):
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             return redirect(url_for('auth.login'))
#         return view(**kwargs)
#
#     return wrapped_view
#
#
# def user_check(username: str) -> bool:
#     db = get_db()
#     user = db.execute(
#         "select * from user where username = ? order by id desc", (username,)
#     ).fetchone()
#     if user is not None:
#         return True
#     else:
#         return False