"""
File: variables.py
Author: kaixi-wu
Date: 2023-10-12
Description: This is a sample Python file.
"""

import sys
import json

print(sys.path)
dir(sys)
dir()
# 追加模式打开的文件对象不支持读取
with open('./1.txt', 'w', encoding="UTF-8") as f:
    print(type(f))
    f.write("这是一个文本文件！")
with open('./1.txt', 'r', encoding="UTF-8") as f:
    # f.write("这是一个文本文件！")
    # 文件指针的操作在写入模式下不生效
    f.seek(0)
    line = f.read()
    print(line)


x = [1, 2, 3]
y = json.dumps(x)
print(y)

# try:
#     x = int(input("please input a int number: "))
#     print(x)
# except ValueError:
#     print("value is not int!!")

import random
import string


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


result = generate_random_string(300)
print(result)


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


re = Reverse("Bryant")
iter(re)
for i in re:
    print(i)

name = ['bryant', 'jeremy']
age = [39, 45]

data = {}
for n,a in zip(name,age):
    data[n] = a
data = json.dumps(data)
print(data)

user = {"admin", "pwd"}
