from base_form import BaseForm, required_str_field
from config import _admin_default_password
from base_form import BaseForm, PaginationForm
from ..models.auth import User
from typing import Optional
from pydantic import Field, field_validator
from base_enum import UserStatus


class LoginForm(BaseForm):
    """ 登录校验 """
    account: str = required_str_field(title="账号")
    password: str = required_str_field(title="密码")

    def depends_validate(self):
        if self.account == 'admin' and self.password == _admin_default_password:
            user = User.query.filter_by(account='admin').first()
        else:
            user = self.validate_data_is_not_exist(f'用户名或密码错误', User, account=self.account)
            self.validate_is_true(user.status != 0, f'用户已冻结，请联系管理员')
            self.validate_is_true(user.verify_password(self.password), f'用户名或密码错误')
        setattr(self, "user", user)


class RegisterForm(BaseForm):
    pass


class UserListForm(PaginationForm):
    """ 用户列表 """
    account: Optional[str] = Field(None, title="用户账号")
    username: Optional[str] = Field(None, title="用户名称")
    detail: Optional[bool] = Field(None, title="是否获取用户详情")
    status: Optional[UserStatus] = Field(None, title="用户状态")

    @classmethod
    @field_validator("detail")
    def validate_detail(cls, value):
        if value:
            cls.validate_is_true(User.is_admin(), msg='非admin用户')

    def get_query_filter(self, *args, **kwargs):
        """ 查询条件 """
        filter_list = []
        # if not User.is_admin():  # 非管理员，只能获取到当前用户有的业务线的人
        #     pass
        if self.username:
            filter_list.append(User.username.like(f'%{self.username}%'))
        if self.account:
            filter_list.append(User.account.like(f'{self.account}%'))
        if self.status:
            filter_list.append(User.status == self.status.value)
        return filter_list

    def depends_validate(self):
        user = User.query.filter_by().all()
        setattr(self, "user", user)
