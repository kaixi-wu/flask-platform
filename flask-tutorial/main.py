import os

from flask import Flask, g
from logging import log
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import config
from exts import db
from flask_migrate import Migrate


def create_app(test_config=None):
    # create app and config the app
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config)
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    #  绑定app到数据库实例
    db.init_app(app)

    migrate = Migrate(app=app, db=db)

    # 测试数据库连接
    with app.app_context():
        with db.engine.connect() as conn:
            rs = conn.execute(text("select now() as curl_time from dual")).fetchone()
            print(rs)

    # 注册蓝图
    from auth.buleprint import auth_blue
    from business.buleprint import business_blue
    app.register_blueprint(auth_blue, url_prefix='/auth')
    app.register_blueprint(business_blue, url_prefix='/blog')
    app.add_url_rule('/', endpoint='index')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=80)



