# 取数据特别麻烦
# 切换获取的数据都是字符串类型
# hello10True
# my_str = "hello10True"
# hello = my_str[:5]
# print(hello)
# num = my_str[5:7]
# print(type(num))

# 想保存多个数据 而且保证多个数据的数据类型不发生改变
# 列表可以保存任意的数据类型
# 格式: 列表名 = [元素1, 元素2, ...]
# # 列表是有序的 -> 下标索引
# my_list = [1, 3.14, "hello", True, [1, 2]]
# # 查看类型<class 'list'>
# print(type(my_list))
# # 通过下标索引获取对应的元素
# pi = my_list[1]
# print(type(pi))

# 定义一个特殊的列表(空的列表)
# my_list = []
my_list = list()
# len(o) -> object(对象)
print(len(my_list))