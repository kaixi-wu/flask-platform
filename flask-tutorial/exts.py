# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


import os
import config

# 初始化db实例，未绑定app
db = SQLAlchemy()


def create_app(test_config=None):
    # create app and config the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    # 绑定app到数据库实例
    db.init_app(app)
    # migrate.init_app(app, db)

    # 测试数据库连接
    # with app.app_context() as ap:
    #     with db.engine.connect() as conn:
    #         rs = conn.execute(text("select now() as curl_time from dual")).fetchone()
    #         if rs is not None:
    #             print("database connect is success!!")

    # 注册蓝图
    from auth.blueprint import auth_blue
    from business.blueprint import business_blue
    app.register_blueprint(blueprint=auth_blue,  url_prefix="/auth")
    app.register_blueprint(blueprint=business_blue, url_prefix='/business')
    app.add_url_rule('/error', endpoint='index')

    return app






