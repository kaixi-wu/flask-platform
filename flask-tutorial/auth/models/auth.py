from exts import db
from base_model import BaseModel

def __init__():
    pass
class User(BaseModel):
    __abstract__ = False
    __tablename__ = 'auth_user'
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
    __abstract__ = False
    __tablename__ = 'auth_role'
    __table_args__ = {"comment": "角色信息表"}
    role_name = db.Column(db.String(80), unique=True, nullable=False, comment="角色名称")
    parent_role_id = db.Column(db.Integer, nullable=True, comment="父级角色")
    frontend = db.Column(db.Text, comment="前端权限")
    Backend = db.Column(db.Text, comment="后端权限")
    enable = db.Column(db.Boolean, default=True, comment="启用状态，1禁用，0启用")

    def __repr__(self):
        return f'<Role: {self.role_name}>'


class Permissions(BaseModel):
    __abstract__ = False
    __tablename__ = 'auth_resource'
    __table_args__ = {"comment": "权限信息表"}
    resource_name = db.Column(db.String(80), unique=True, nullable=False, comment="权限名称")
    resource_type = db.Column(db.String(80), nullable=False, comment="权限类型")
    resource_classify = db.Column(db.String(80), nullable=False, comment="权限分类")
    resource_address = db.Column(db.String(200), unique=True, nullable=False, comment="权限地址")

    def __repr__(self):
        return f'<Role: {self.role_name}>'


class UserRole(BaseModel):
    __abstract__ = False
    __tablename__ = 'auth_user_role'
    __table_args__ = {"comment": "用户角色关联表"}
    user_id = db.Column(db.Integer, nullable=False, comment="用户id")
    role_id = db.Column(db.Integer, nullable=False, comment="角色id")


class RolePermissions(BaseModel):
    __abstract__ = False
    __tablename__ = 'auth_role_res'
    __table_args__ = {"comment": "角色权限关联表"}
    role_id = db.Column(db.Integer, nullable=False, comment="角色id")
    res_id = db.Column(db.Integer, nullable=False, comment="权限id")
