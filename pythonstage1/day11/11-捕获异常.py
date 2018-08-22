# FileNotFoundError: [Errno 2] No such file or directory: 'hm.txt'
# FileNotFoundError -> 异常类型
# [Errno 2] No such file or directory: 'hm.txt' 异常信息描述


# 捕获异常 只是保证程序不再崩溃 不是解决了异常问题 (except进行处理)
"""
try:
    执行可能会发生异常的代码
except 异常类型:
    如果捕获到了异常 做的事情
"""
try:
    # 打开文件
    # f = open("hm.txt", "r")
    print("你好")
except FileNotFoundError:
    print("捕获到了异常")