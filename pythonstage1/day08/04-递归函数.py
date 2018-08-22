# 需求: x!
# 5的阶乘 5! = 5 * 4 * 3 * 2 * 1
# def func(num):
#     # 定义局部变量 保存乘积
#     ret = 1
#     while num > 0:
#         ret *= num
#         num -= 1
#     return ret
# result = func(5)
# print(result)

# 函数的嵌套调用完成
# 5! = 5 * 4 * 3 * 2 * 1


# # 1! = 1
# def func1(num):
#     if num == 1:
#         return num
#     else:
#         pass
# # ret = func1(1)
# # print(ret)
#
# # 2! = 2 * 1!
# def func2(num):
#     if num == 1:
#         return num
#     else:
#         return num * func1(num - 1)
# # print(func2(2))
#
# # 3! = 3 * 2!
# def func3(num):
#     if num == 1:
#         return num
#     else:
#         return num * func2(num - 1)
# # print(func3(3))
#
# # 4! = 4 * 3!
# def func4(num):
#     if num == 1:
#         return num
#     else:
#         return num * func3(num - 1)
# # print(func4(4))
#
# # 5! = 5 * 4!
# def func5(num):
#     if num == 1:
#         return num
#     else:
#         return num * func4(num - 1)
#
# print(func5(5))


# 递归函数: 函数内部自己调用自己本身
# 每次在进行递归调用的时候 都会消耗计算机的资源 如果不能停止 就会把计算机的资源耗尽(计算机死机 或者 卡死)
def func(num):
    # 给递归函数添加一个停止递归调用的结束条件
    if num == 1:
        return num
    else:
        return num * func(num - 1)


print(func(5))
