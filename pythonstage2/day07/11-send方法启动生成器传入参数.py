def fibnacci(num):
    # num:表示生成数列的个数
    # 记录数列前面两个值
    a = 0
    b = 1
    # 记录生成数列的下标
    index = 0

    # 循环判断条件是否成立
    while index < num:
        result = a
        a, b = b, a + b
        index += 1
        # 当代码执行到yield的时候，代码会暂停，然后把结果返回给外界，下次启动生成器会在暂停的位置继续往下值
        # 提示： 让生成器启动的时候可以接收外界传入的参数
        result = yield result
        print(result)
        if result == "ok":
            return

fib = fibnacci(5)
# value = next(fib)
# print(value)
#
# value = fib.send("ok")
# print(value)

# 建议： 第一次启动生成器使用next函数，第二个启动生成器传入参数可以使用send方法
value = fib.send(None)
print(value)


value = fib.send("error")
print(value)