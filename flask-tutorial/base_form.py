from pydantic import BaseModel as pydanticBaseModel, Field
from typing import Union, Optional


def required_str_field(*args, **kwargs):
    """ 必传字段, 且长度大于1，防止传null、空字符串 """
    kwargs["min_length"] = 1
    return Field(..., **kwargs)


class BaseForm(pydanticBaseModel):
    def __setattr__(self, key, value):
        self.__dict__[key] = value

    pass
