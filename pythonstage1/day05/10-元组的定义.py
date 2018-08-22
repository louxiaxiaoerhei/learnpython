"""
元组和列表极其相似
列表是可变的数据类型(增删改查)
元组是不可变的数据类型(查)

相同点
保存任意数据类型
都是有序的数据类型
"""
"""
字符串 '' "" """"""
列表 []
元组 ()

"""

# 定义一个元组
my_tuple = (1, 3.14, True, "hello")
# print(my_tuple)
# 取值
# pi = my_tuple[1]
# print(pi)
# 修改TypeError: 'tuple' object does not support item assignment
# my_tuple[0] = 123

# 查看类型
# <class 'tuple'>
# print(type(my_tuple))


# 02 查:
# in
# if 3.14 in my_tuple:
#     print("存在")

# not in 不存在

# index
# index = my_tuple.index("hello")
# print(index)

# count
# count = my_tuple.count(1)
# print(count)

# 03: 定义一个特殊的元组
# 空元组
# my_tuple = ()
# my_tuple = tuple()
# print(type(my_tuple))
# 有且只有一个元素的元组
# 格式: 变量名 = (元素,)
# my_tuple = (3.14,)
# print(type(my_tuple))

# 04: 重新赋值
# my_tuple = (1, 2, 3)
# my_tuple = (2, 3, 4)
# print(my_tuple)

# 05: 循环遍历
# for
# for value in my_tuple:
#     print(value)

# while
# i = 0
# while i < len(my_tuple):
#     print(my_tuple[i])
#     i += 1

# 06: 为什么提出来元组类型(作用?)
# 从列表的角度分析
# 保证数据安全
my_list = (123, 3.14)
