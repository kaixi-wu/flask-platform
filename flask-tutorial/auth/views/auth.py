from base_enum import UserStatus, ErrorMessage as errorMessage
from werkzeug.security import check_password_hash, generate_password_hash
from ..blueprint import auth_blue
from flask import request, jsonify, session, g
from ..models.auth import User, Role
from exts import db

import functools
import logging


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return jsonify({"success": False, "data": "登录信息已失效"})
        return view(**kwargs)
    return wrapped_view


@auth_blue.before_request
def load_logged_in_user():
    user_id = session.get("user_id")
    logging.debug(request.headers)
    logging.debug('user_id is {}'.format(user_id))

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()
        logging.debug(g.user)


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


@auth_blue.route('/login', methods=('POST',))
def login():
    if request.method == 'POST':
        account = request.json.get('account')
        password = request.json.get('password')
        error = None
        user = User.query.filter_by(account=account).first()

        if user is None:
            error = '用户未注册'
        elif not check_password_hash(user.password, password):
            error = '密码错误'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            # return redirect(url_for('login_success'))
            return jsonify({'message': '登录成功'})
    return jsonify({'error': error})


@auth_blue.route('/logout')
def logout():
    session.clear()
    return jsonify({"success": True, "data": None})


@login_required
@auth_blue.post('/reset_password')
def reset_password():
    user_id = session.get('user_id')
    if request.method == 'POST':
        new_password = request.json.get('new_password')
        old_password = request.json.get('old_password')
        account = request.json.get('account')
        error = None
        if not new_password:
            error = 'new_password is required.'
        elif not old_password:
            error = 'old_password is required.'
        elif not account:
            error = 'account is required.'

        if not check_password_hash(g.user.password, old_password):
            return jsonify({"success": False, "data": "旧密码错误"})

        if old_password == new_password:
            return jsonify({"success": False, "data": "新密码不能与旧密码相同"})

        try:
            user = User.query.get(user_id)
            user.password = generate_password_hash(new_password)
            db.session.commit()
            return jsonify({"success": True, "data": "密码修改成功"})
        except Exception as e:
            db.session.rollback()
            logging.error(f"密码重置时出错: {e}")
            return jsonify({"success": False, "data": "密码修改失败"})

    return jsonify({"success": False, "data": "仅支持POST请求"})


@auth_blue.get('/user/list')
def user_list():
    if request.method == 'GET':
        users = User.query.filter_by(delete=False).all()
        return jsonify({'data': [{
            'username': user.username,
            'email': user.email,
            'enable': user.enable} for user in users], 'success': True})
