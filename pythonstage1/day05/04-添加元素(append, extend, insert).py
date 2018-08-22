# 列表是可变的数据类型
# 定义一个空的列表
my_list = [0, 1, 2, 3]

# append(追加元素)
# 格式: 列表名.append(对象)
# my_list.append("hello")
# print(my_list)

# extend
# 格式: 列表名.extend(可迭代对象)
# 会把可迭代对象进行最小单元拆分然后保存到列表中
# my_list.extend("hello")
# print(my_list)
# 揣测
# for c in "hello":
#     my_list.append(c)
# print(my_list)

# insert(插入数据)
# 格式: 列表名.insert(下标索引, 对象)
# my_list.insert(-10, "hello")
# print(my_list)


# 添加可迭代对象
# append
# extend
# insert
# 会进行最小单元拆分
# extend

