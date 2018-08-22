"""
集合是无序的(不支持下表索引)
集合是可变的数据类型
集合可以保存任意数据类型 但是不能存在任何可变的数据类型
集合因为每个元素的值必须是不同的 一般可以在实际开发中用于元素去重操作
"""

# 集合的定义
# my_set = {1, 3, 5, 7, 1, 4}
# <class 'set'>
# print(type(my_set))

# 定义一个特殊的集合
# my_set = set()
# print(type(my_set))

# 元素不能为可变的
# my_set = {1, 3, [1, 2]}

# 添加元素(add，update)
# 定义一个空的集合
# my_set = set()

# add -> append
# my_set.add(123)
# my_set.add(234)

# update -> extend
# my_set.update("abcd")
# print(my_set)

# 删除元素(remove，pop，discard)

my_set = {1, 3, 5, 7}

# remove
# remove(元素值) -> 如果有直接删除 如果没有 将报错
# my_set.remove(51)
# print(my_set)
# print(my_set)
# pop
# 随机删除集合中的一个元素
# ret = my_set.pop()
# print(ret)
# print(my_set)

# discard
# discard(元素值) -> 如果有直接删除 如果没有 什么也不做
# my_set.discard(31)
# print(my_set)

# in not in 适合于集合中
# if 3 in my_set:
#     print("存在")

# for循环
for value in my_set:
    print(value)