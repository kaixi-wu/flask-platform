"""
Fix=Noneriables.py
Author: kaixi-wu
Date: 2023-10-12
Description: This is a sample Python file.
"""

import os
import sys
from typing import TypeVar, Iterable, Generic
from datetime import date as date, time as time, datetime as datetime, timezone

print(os.getcwd())
print(sys.argv)

print(date.today())

print(date.weekday(date.today()))

now_time = time(hour=10, minute=24, second=44)
print(now_time)
print(datetime.utcnow())
print(datetime.now())
print(datetime.astimezone(datetime.now()))
print(datetime.now(timezone.utc))
fl = datetime.timestamp(datetime.now())
print(int(round(fl, 3) * 1000))


class MyClass:
    class_attr = "this is class attr"

    def __init__(self):
        self.x = "this is instance attr"

    def instance_method(self):
        print("this is instance method!")

    @staticmethod
    def stat():
        print("this is static method")

    @classmethod
    def class_method(cls):
        print('this is class method')

    def __instancecheck__(self, instance):
        pass


my_class = MyClass()
my_class.class_method()
print(MyClass.class_attr)
print(MyClass.instance_method(my_class))
my_class.stat()

# 定义泛型类型T
T = TypeVar('T')


def first(items: Iterable[T]) -> T:
    return next(iter(items))


class Stack(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()


number = list((1, 2, 3))

i = 23


def f():
    i = 21
    print(i)


i = 22
f()


def gen():
    yield 123


for i in gen():
    print(i)


def echo(value=None):
    print('this is yield test!!')
    try:
        while True:
            try:
                value = (yield value)
            except Exception as e:
                value = e
    finally:
        print('test is end!')


gent = echo(10)
print(next(gent))
gent.throw(StopIteration, 'stop error')
gent.send(6)
print(next(gent))
print(next(gent))
gent.close()


class Cls:
    x = 3


incls = Cls()
incls.x = incls.x + 1
print(incls.x)
print(Cls.x)

y = [0, 1]
i = 0
i, y[i] = 1, 2
print(i)  # i is updated, then x[i] is updated
print(y)
# assert 1==2

import asyncio


async def func():
    await asyncio.sleep(2)
    print("this is async def")


asyncio.run(func())

ob = 'bRyant'


def is_up(*args):
    for x in args:
        if any(char.isupper() for char in x):
            return True
    return False


print(is_up(ob))
