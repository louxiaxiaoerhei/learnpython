# 比较pythonic写法
# name = "小明"
# age = 22
# no = "009"
# 等价
# name, age, no = "小明", 22, "009"
# print(name, age, no)

# 定义一个变量
# a = 4
# if a >= 1 and a <= 10:
#     print("满足")
# 等价
# if 1 <= a <= 10:
#     print("满足")

# 拆包
# 定义一个列表
# my_list = ['小明', 20, '009']
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])

# 01: 自己定义
# 变量的个数需要和拆包的数据要一一对应
# name, age, no = ['小明', 20, '009']
# print(name)
# print(age)
# print(no)

# 02: 同事定义
# 需求: 对已有的列表进行拆包
# my_list = ['小明', 20, '009']
#
# name, age, no = my_list
#
# print(name)
# print(age)
# print(no)

# 03:
def deal_info(name, age):
    new_name = "你的名字叫做" + name
    new_age = "你的年龄为%d岁" % age
    return new_name, new_age

# my_name, my_age = deal_info("小明", 22)
# print(my_name)
# print(my_age)

# 字符串
c1, c2, c3 = "abc"
print(c1, c2, c3)
