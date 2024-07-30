import os
from flask import Flask, render_template


def create_app(test_config=None):
    # create app and config the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return 'hello'

    @app.route('/login')
    def login_success():
        return 'login success!!'

    @app.get('/log')
    def login_out():
        return 'login out!!!'

    from . import db
    db.init_app(app)

    from . import auth, blog
    app.register_blueprint(auth.auth_blue, url_prefix='/auth')
    app.register_blueprint(blog.blog_blue)
    app.add_url_rule('/', endpoint='index')

    return app
