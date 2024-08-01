from exts import db
from datetime import datetime


class BaseModel(db.Model):
    # 基类模型
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="主键自增")
    delete = db.Column(db.Boolean, default=False, nullable=False, comment="是否删除")
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now(), comment="创建时间")
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now(),
                            comment="更新时间")
    create_user = db.Column(db.Integer(), nullable=True, default=None, comment="创建数据的用户id")
    update_user = db.Column(db.Integer(), nullable=True, default=None, comment="修改数据的用户id")
    remark = db.Column(db.String(80), comment="备注")


