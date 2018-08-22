
# # try中的
# try:
#     try:
#         print(num)
#     finally:
#         print("fianlly")
# except:
#     print("捕获到了异常")


# 函数中
# 01
# def func1():
#     try:
#         print(num)
#     except:
#         print("捕获异常")
#
# def func2():
#     func1()
#
# func2()

# 02
# def func1():
#     print(num)
#
# def func2():
#     try:
#         func1()
#     except:
#         print("捕获异常")
#
# func2()

# 03
# def func1():
#     print(num)
#
# def func2():
#     func1()
#
# try:
#     func2()
# except:
#     print("捕获到了异常")