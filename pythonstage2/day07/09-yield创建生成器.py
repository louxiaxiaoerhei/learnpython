def fibnacci(num):
    # num:表示生成数列的个数
    # 记录数列前面两个值
    a = 0
    b = 1
    # 记录生成数列的下标
    index = 0
    print("--11--")
    # 循环判断条件是否成立
    while index < num:
        result = a
        a, b = b, a + b
        index += 1
        print("--22--")
        # 当代码执行到yield的时候，代码会暂停，然后把结果返回给外界，下次启动生成器会在暂停的位置继续往下值
        yield result
        print("--333--")

result = fibnacci(5)
# print(result)

value = next(result)
print(value)
#
value = next(result)
print(value)

# for value in result:
#     print(value)