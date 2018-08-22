# 01:
# 定义一个变量
# 全局变量: 定义在函数外部的变量
# 作用域: 整个模块内部
# num = 10
#
# def func1():
#     print(num)
#
# print(num)
# func1()

# 02:
# # 定义一个全局变量
# num = 10
# def func2():
#     # 在函数内部定义了一个和全局变量名相同的局部变量
#     num = 20
#     # 20
#     print("内部", num)
#
# # 10
# print("开始", num)
# func2()
# # 10
# print("结束", num)

# 03:
# 需求: 利用函数修改全局变量的值
# 定义一个全局变量
num = 10
def func3():
    # 告知python 这不是定义一个和全局变量名相同的局部变量 而是修改全局变量的值
    global num
    num = 30

func3()
print(num)

