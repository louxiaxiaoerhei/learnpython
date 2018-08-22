

"""
try:
    执行可能会发生异常的代码(类型1)
    执行可能会发生异常的代码(类型2)
    执行可能会发生异常的代码(类型...)
except (类型1, 类型2, 类型...):
    捕获到了异常做的事情
"""
# 捕获异常
try:
    # 如果捕获到了异常 代码不再向下执行 直接进入except
    f = open("hm.txt", "w")
    print(num)
except (FileNotFoundError, NameError):
    print("捕获异常")