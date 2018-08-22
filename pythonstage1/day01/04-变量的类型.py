# type 内置函数 (python已经定义好的 程序员可以直接使用)
# type 就是用来查看变量的类型的
# 格式 type(变量名或者数值) -> 变量或者数值的类型

# 定义一个变量 保存一个人的名字
name = "小明"
# 查看变量的类型
# <class 'str'> str -> string 字符串类型
# print(type(name))
# print(name)

# 定义一个变量 保存一个人的年龄
age = 20
# <class 'int'>
# print(type(age))

# 定义一个变量 保存一个人的身高
height = 178.55
# <class 'float'>
# print(type(height))

# 定义一个变量 保存是否是男性
is_man = False
# <class 'bool'> -> 布尔
print(type(is_man))

"""
为什么python中提供了很多数据类型?
有限的内存 无限的变量 (降低用户体验)
合理的使用内存 提高计算机的性能

python的变量的数据类型,程序猿关心么?
程序媛只需要把数值写好即可 什么类型 python可以通过程序媛的数据自动推到出来对应的类型
"""

# 中国 = 11000
# print(中国)

