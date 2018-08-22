# 生成器是一个特殊的迭代器，可以使用next和for循环取值
# result = [i * 2 for i in range(4)]
# print(result)
# 创建生成器
generator1 = (i * 2 for i in range(4))
print(generator1)

# value = next(generator1)
# print(value)

for value in generator1:
    print(value)