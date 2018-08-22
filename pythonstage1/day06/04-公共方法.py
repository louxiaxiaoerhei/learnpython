
# # *运算符 打印三角形
# for i in range(1, 6):
#     print("*"*i)

# print(max([1, 3, 4, 6, 5]))
# print(max("abcdef"))


# del
# 列表: del 列表名[下标索引]
# 字典: del 字典名[key]

# 删除变量 了解(后期讲解)

# 多维列表/元祖访问的示例

my_list = [1, 3, 5, (2, 3, 5, {"name": "小明", "test": ["你好", "终于等到你"]}, 2)]

# 终于等到你
ret1 = my_list[3]
# (2, 3, 5, {'name': '小明', 'test': ['你好', '终于等到你']}, 2)
# print(ret1)
ret2 = ret1[3]
# {'name': '小明', 'test': ['你好', '终于等到你']}
# print(ret2)
ret3 = ret2["test"]
# ['你好', '终于等到你']
# print(ret3)
ret4 = ret3[1]
print(ret4)

#
ret = my_list[3][3]["test"][1]
print(ret)
