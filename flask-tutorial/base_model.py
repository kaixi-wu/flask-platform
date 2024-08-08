from flask_sqlalchemy import SQLAlchemy, BaseQuery as _BaseQuery
from datetime import datetime
from flask import g
from typing import Union


class BaseQuery(_BaseQuery):

    def filter_by(self, **kwargs):
        kwargs.setdefault('delete', False)
        return super(BaseQuery, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=BaseQuery)


class BaseModel(db.Model):
    __table__ = None
    __abstract__ = True

    db = db

    # 基类模型
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="主键自增")
    delete = db.Column(db.Boolean, default=False, nullable=False, comment="是否删除")
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now(), comment="创建时间")
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now(),
                            comment="更新时间")
    create_user = db.Column(db.Integer(), nullable=True, default=None, comment="创建数据的用户id")
    update_user = db.Column(db.Integer(), nullable=True, default=None, comment="修改数据的用户id")
    remark = db.Column(db.String(80), comment="备注")

    @classmethod
    def get_first(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def get_table_column_name_list(cls):
        return [column.name for column in cls.__table__.columns]

    def to_dict(self, pop_list: list = [], filter_list: list = []):
        if pop_list or filter_list:
            dict_data = {}
            for column_name in self.get_table_column_name_list():
                if filter_list:
                    if column_name in filter_list:
                        dict_data[column_name] = getattr(self, column_name)
                else:
                    if column_name not in pop_list:
                        dict_data[column_name] = getattr(self, column_name)
            return dict_data
        return {column.name: getattr(self, column.name, None) for column in self.__table__.columns}

    @classmethod
    def make_pagination(cls, form, get_filed=None, order_by=None, **kwargs):
        if get_filed is None:
            get_filed = cls.__table__.columns
        if order_by is None:
            order_by = cls.id
        col_name_list = [column.name for column in get_filed]  # 字段名称
        query_date = cls.db.session.query(*get_filed).filter(*form.get_query_filter(**kwargs)).order_by(order_by).all()
        return {
            "total": len(query_date),
            "data": [dict(zip(col_name_list, item)) for item in query_date]
        }

