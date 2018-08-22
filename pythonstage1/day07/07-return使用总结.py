"""
01: 标识着一个函数是一个有返回值的函数
02: 提前结束函数的调用
"""
# 01: 标识着一个函数是一个有返回值的函数
# def add2num(a, b):
#     return a + b
# ret = add2num(10, 20)
# print(ret)

# 02: 提前结束函数的调用
# def print_info(score):
#     if score > 100 or score < 0:
#         print("您输入的分数不合法...")
#     else:
#         if score >= 90:
#             print("优")
#         elif score >= 70:
#             print("良")
#         elif score >= 60:
#             print("中")
#         else:
#             print("差")
#
# print_info(100)


def print_info(score):
    if score > 100 or score < 0:
        print("您输入的分数不合法...")
        return

    if score >= 90:
        print("优")
    elif score >= 70:
        print("良")
    elif score >= 60:
        print("中")
    else:
        print("差")


print_info(110)