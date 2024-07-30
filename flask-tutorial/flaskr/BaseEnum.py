import enum


class UserStatus(enum):
    NORMAL = 1
    CANCEL = 0


class ErrorMessage(enum):
    USER00001 = 'user.not.Registration'
