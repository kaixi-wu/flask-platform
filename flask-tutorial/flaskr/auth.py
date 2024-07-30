import functools

import app
from BaseEnum import UserStatus, ErrorMessage as errormessage
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from .db import get_db

auth_blue = Blueprint('auth', __name__)


@auth_blue.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        if error is None:
            try:
                db.execute(
                    "insert into user (username, password) values (?, ?)", (username, generate_password_hash(password))
                )
                db.commit()
            except db.IntegrityError:
                raise error
            else:
                return {"success": True, "data": None}
        flash(errormessage.USER00001)

    return render_template('auth/register.html')


@auth_blue.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('login_success'))

        flash(error)

    return render_template('auth/login.html')


@auth_blue.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@auth_blue.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_out'))


@auth_blue.route('/reset_password', methods=('GET', 'POST'))
def reset_password():
    # user_id = session.get('user_id')
    if request.method == 'POST':
        new_password = request.form['new_password']
        old_password = request.form['old_password']
        db = get_db()
        username = request.form['username']
        error = None
        if not new_password:
            error = 'new_password is required.'
        elif not old_password:
            error = 'old_password is required.'
        elif not username:
            error = 'username is required.'

        # user = db.execute(
        #     'select * from user where id = ?', (user_id,)
        # ).fetchone()

        if not check_password_hash(g.user['password'], old_password):
            error = 'old password is error'
        if old_password == new_password:
            error = "new password and old password not equal"
        else:
            db.execute(
                'update user set password = ? where id = ?', (generate_password_hash(new_password), g.user_id)
            )
            get_db().commit()

        flash(error)

    return render_template('auth/reset_password.html')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)

    return wrapped_view
