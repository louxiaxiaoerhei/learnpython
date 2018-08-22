# 不可变数据类型(b = b + b 和 b += b 是等价的 都是重新赋值)

## b = b + b
# # 定义一个有参数的函数
# def func(b):
#     b = b + b
#     print("b=", b)
#
#
# a = 10
# func(a)
# print("a=", a)


# b += b
# 定义一个有参数的函数
# def func(b):
#     b += b
#     print("b=", b)
#
#
# a = 10
# func(a)
# print("a=", a)


# 可变数据类型
# # b = b + b (重新赋值)
# def func(b):
#     b = b + b
#     print("b=", b)
#
#
# a = [1, 2]
# func(a)
# print("a=", a)

# b += b(类似于b.extend(b))改变其本身
def func(b):
    b += b
    print("b=", b)


a = [1, 2]
func(a)
print("a=", a)



