"""
File: variables.py
Author: kaixi-wu
Date: 2023-10-12
Description: This is a sample Python file.
"""

'''
常见的数据类型有：int, float, str, bool
常用数据类型：list，tuple，set，dict
'''
# 创建字符串
# 单引号
string = 'henry'
# 双引号
string_ant = "hello world!!"
# 三引号(多行字符串)
string_three = '''
this is my house！
get out！！
'''
# 或者
string_four = """
this is my house！
get out！！
"""

print("hen" in string)

"""字符串常见操作"""
# 1、获取字符串长度
length = len(string)
print(length)

# 字符串全部为小写
print('hello world!!'.lower())
# 字符串全部为小写
print('hello world!!'.upper())
# 判断是否全部为小写
print('hello world!!'.islower())
