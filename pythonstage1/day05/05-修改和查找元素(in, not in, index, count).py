
# 定义一个列表
my_list = [123, 123, 3.14, 1, True]

# 修改元素
# 格式: 列表名[下标索引] = 数值
# my_list[0] = 456
# print(my_list)

# in 判断一个元素是否在一个列表中
# if 123 in my_list:
#     print("123在列表中")

# not in 不存在
# if 456 not in my_list:
#     print("456不存在")

# index
# 如果找到返回下标索引 找不到就报错
# index = my_list.index(123)
# print(index)

# count 计算元素在列表中出现的次数
# count = my_list.count(1)
# print(count)

# 解决index保存文字
# 01
# if my_list.count(3.14):
#     index = my_list.index(3.14)
#     print(index)
# else:
#     print("不存在")

# 02:
# if 3.14 in my_list:
#     index = my_list.index(3.14)
#     print(index)
# else:
#     print("不存在")

# 03: 隐式len(my_list)
# if my_list:
#     print(len(my_list))
# else:
#     print("列表元素个数为0")