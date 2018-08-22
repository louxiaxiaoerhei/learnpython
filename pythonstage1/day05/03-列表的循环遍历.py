# 定义一个列表
my_list = [11, 3.14, "hello", True]

# 循环遍历
# for循环
# 列表是一个可迭代对象
# for value in my_list:
#     print(value)

# while循环
# 变量
i = 0
while i < len(my_list):
    # 通过下标索引获取列表中的元素
    value = my_list[i]
    print(value)
    i += 1