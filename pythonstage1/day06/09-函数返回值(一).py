
# # 求和操作
# # 有返回值的函数(标识这一个有返回值的函数 函数内部 return 返回值)
# def add2num(a, b):
#     ret = a + b
#     return ret
#
# result = add2num(11, 22)
#
# print(result)


# python计算列表最大值的max
# my_list = [1, 3, 5]
# my_max = max(my_list)
# print(my_max)
import random
# 揣测max函数如何实现的
# 01: 定义一个列表 有5个元素[1, 100] 保存都是数字类型
# 定义一个空列表
my_list = []
for i in range(5):
    value = random.randint(-100, -10)
    my_list.append(value)

print(my_list)

# 定义一个计算最大值得函数
def hm_max(new_list):
    # 定义一个变量 设定一个假设的最大值
    my_num = new_list[0]
    for value in new_list:
        if value > my_num:
            my_num = value

    return my_num

# 调用
ret = hm_max(my_list)
print("最大值:%d" % ret)


