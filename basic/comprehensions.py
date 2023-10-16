"""
File: dataType.py
Author: kaixi-wu
Date: 2023-10-12
Description: This is a sample Python file.
"""
"""
推导式
"""
# 字典推导式
'''提供三个数字，以三个数字为键，三个数字的平方为值来创建字典'''
num_list = [1, 22, 4]
num_dict = {num: num ** 2 for num in num_list}
print(num_dict)
print(type(num_dict))  # 输出dict

# 元组推导式（返回的是一个迭代器对象）
tuple_com = (x for x in 'abcdefg' if x not in 'abd')
print(tuple_com, type(tuple_com))

