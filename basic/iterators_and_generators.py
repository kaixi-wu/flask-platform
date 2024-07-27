"""
Fix=Noneriables.py
Author: kaixi-wu
Date: 2023-10-12
Description: This is a sample Python file.
"""
import sys

'''迭代器和生成器'''

student_name = ['Bob', 'Lucas', 'Jeremy', 'John', 'Tom']
iters = iter(student_name)

users = {
    'Alice': 'active',
    'Bob': 'inactive',
    'Charlie': 'active',
    'David': 'inactive',
    'Eve': 'active'
}

names = {
    "bryant": {"status": "active"},
    "kobe": {"status": "un_active"}
}
# name = input("please input your name:")
# for i in names:
#     if names[i]["status"] == "active":
#         print("good!")

print(sum(range(1, 101)))
print("_" * 10)
mn = map(lambda x: x ** 2, range(10))
for i in mn:
    print(i, end=',')

active_user = []
for user, status in users.items():
    if status == "active":
        active_user.append(user)
print(users.items())
print(active_user)


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


def squares(*args):
    for n in args:
        if n // 2 == 0:
            print(f"{n} this is squares!")
        else:
            print(f"{n} is odd!")


# print(squares(1, 2, 3, 4, 5, 6, 7))
print(list(map(lambda x: x ** 2, range(10))))
print([x**2 for x in range(10)])
print([{x: y} for x in [1, 4, 6] for y in [7, 4, 3]])
print(tuple((x, x**2) for x in range(10)))
'''生成器'''
name = ["WKX", "SXM", "ZP"]
age = [31, 18, 51]
param = []
param.append(name)
param.append(age)
print(list(zip(*param)))

print([(x, y) for x, y in zip(*param)])


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))