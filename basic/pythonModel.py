"""
File: dataType.py
Author: kaixi-wu
Date: 2023-10-12
Description: This is a sample Python file.
"""

import sys
print(sys.path)
dir(sys)
dir()
f = open('./1.txt', 'w')
print(type(f))
f.write("这是一个文本文件！")
f.close()


import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

result = generate_random_string(300)
print(result)