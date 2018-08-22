# 求和2个数
# def add2num(a, b):
#     return a + b
# ret = add2num(10, 20)
# print(ret)

# 求和3个数
# def add3num(a, b, c):
#     return a + b + c
# ret = add3num(10, 20, 30)
# print(ret)

# 求和n个数
# def addxnum(new_list):
#     # 定义一个变量 保存和
#     my_sum = 0
#     for value in new_list:
#         my_sum += value
#
#     return my_sum
#
# ret = addxnum([10, 20, 30, 40, 50])
# print(ret)

# 不定长参数之元组
def addxnum(*args):
    print(args[0])
    print(type(args))
    # 定义一个变量 保存和
    my_sum = 0
    for value in args:
        my_sum += value

    return my_sum

# 如果在调用一个不定长参数之元素 调用函数的时候 遵循位置参数调用即可
# ret = addxnum(10, 20, 30, 40, 50)
# print(ret)

# 注意点:
# 不定义参数之元素 -> 缺省参数 (默认值为 ())
# def my_func(*args):
#     print(args)
#
# my_func()

# 扩展
my_list = [1, 3, 5, 7]

def func(*args):
    print(args)

func(*my_list)