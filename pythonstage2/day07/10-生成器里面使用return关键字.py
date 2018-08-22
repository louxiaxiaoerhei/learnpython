def fibnacci(num):
    # num:表示生成数列的个数
    # 记录数列前面两个值
    a = 0
    b = 1
    # 记录生成数列的下标
    index = 0
    print("111")
    # 循环判断条件是否成立
    while index < num:
        result = a
        a, b = b, a + b
        index += 1
        print("222")
        # 当代码执行到yield的时候，代码会暂停，然后把结果返回给外界，下次启动生成器会在暂停的位置继续往下值
        yield result
        print("333")
        # 当前生成器里面执行return关键字会抛出停止迭代的异常
        # return "ok"


result = fibnacci(5)
# print(result)

# value = next(result)
# print(value)

try:
    value = next(result)
    print(value)

except StopIteration as e:
    print(e.value)

# 总结： yield可以返回多次值，return只能返回一次值，并且抛出停止迭代的异常

# while True:
#     value = next(result)
#     print(value)