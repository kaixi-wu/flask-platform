from exts import db
from base_model import BaseModel


class User(BaseModel):
    __table__ = 'user'
    __table_args__ = {"comment": "用户基本信息表"}
    username = db.Column(db.String(80), unique=True, nullable=False, comment="用户名称")
    account = db.Column(db.String(80), unique=True, nullable=False, comment="用户账号")
    password = db.Column(db.String(80), nullable=False, comment="password")
    phone = db.Column(db.String(80), unique=True, comment="电话")
    email = db.Column(db.String(120), unique=True, nullable=False, comment="邮箱")
    enable = db.Column(db.Boolean, default=True, comment="启用状态，1禁用，0启用")

    def __repr__(self):
        return f'<User: {self.username}>'


class Role(BaseModel):
    __table__ = 'role'
    __table_args__ = {"comment": "角色信息表"}
    role_name = db.Column(db.String(80), unique=True, nullable=False, comment="角色名称")
    parent_role_id = db.Column(db.Integer, nullable=True, comment="父级角色")
    frontend = db.Column(db.Text, comment="前端权限")
    Backend = db.Column(db.Text, comment="后端权限")
    enable = db.Column(db.Boolean, default=True, comment="启用状态，1禁用，0启用")

    def __repr__(self):
        return f'<Role: {self.role_name}>'


class Permissions(BaseModel):
    __table__ = 'permissions'
    __table_args__ = {"comment": "权限信息表"}
    permission_name = db.Column(db.String(80), unique=True, nullable=False, comment="权限名称")
    permission_type = db.Column(db.String(80), nullable=False, comment="权限类型")
    permission_classify = db.Column(db.String(80), nullable=False, comment="权限分类")
    permission_address = db.Column(db.String(200), unique=True, nullable=False, comment="权限地址")

    def __repr__(self):
        return f'<Role: {self.role_name}>'


class UserRole(BaseModel):
    __table__ = 'user_role'
    __table_args__ = {"comment": "用户角色关联表"}
    user_id = db.Column(db.Integer, nullable=False, comment="用户id")
    role_id = db.Column(db.Integer, nullable=False, comment="角色id")
