"""
File: dataType.py
Author: kaixi-wu
Date: 2023-10-12
Description: This is a sample Python file.
"""
import sys

'''迭代器和生成器'''

student_name = ['Bob', 'Lucas', 'Jeremy', 'John', 'Tom']
iters = iter(student_name)


def a():
    for i in iters:
        if len(i) > 3:
            print(i)


def b():
    while True:
        try:
            print(next(iters))
        except StopIteration:
            sys.exit()


'''生成器'''


