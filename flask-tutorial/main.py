import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 创建 SQLAlchemy 实例
db = SQLAlchemy()


def create_app(test_config=None):
    # create app and config the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE='flaskr.sqlite',
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:Zhangping890@127.0.0.1/blog_test',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
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

    db.init_app(app)

    # 创建所有定义的数据库表
    with app.app_context():
        db.create_all()

    # 注册蓝图
    from auth.buleprint import auth_blue
    from blog.buleprint import blog_blue
    app.register_blueprint(auth_blue, url_prefix='/auth')
    app.register_blueprint(blog_blue, url_prefix='/blog')
    app.add_url_rule('/', endpoint='index')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=80)