
# 定义一个有返回值的函数(函数内部 有写 return 返回值)
# 如果一个函数中有多个return 但是如果只要一个执行了 后面的return将都不在执行
# 如果执行了return return后面代码将不再执行
# 如果一个函数执行了return 就标识这函数的调用结束
# 对照循环中的break
def my_func():
    print("-111111111")
    return "111111111"

    print("-2222222222")
    return "2222222222"

    print("-333333333333")
    return "333333333333"

ret = my_func()
print(ret)