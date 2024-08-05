from base_form import BaseForm, required_str_field


class LoginForm(BaseForm):
    """ 登录校验 """
    account: str = required_str_field(title="账号")
    password: str = required_str_field(title="密码")
