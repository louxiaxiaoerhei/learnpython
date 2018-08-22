# 列表推导式 就是快速的创建一个有规则的列表

# 01:
# 需求: [1, 2, 3, ..., 100]
# # 01: 创建一个空的列表
# my_list = []
# # 循环
# for i in range(1, 101):
#     # 追加
#     my_list.append(i)
#
# print(my_list)
# 优化
# my_list = [i for i in range(1, 101)]
# print(my_list)

# 02:
# 需求: [2, 4, 6, 8, 10, ...100][1, 100]的偶数
# 创建一个空的列表
# my_list = []
# for i in range(1, 101):
#     # 判断
#     if i % 2 == 0:
#         my_list.append(i)
#
# print(my_list)

# 优化
# my_list = [i for i in range(1, 101) if i % 2 == 0]
# print(my_list)


# # 03:
# # 需求: 10个元素 都是中国
# my_list = []
# for _ in range(10):
#     my_list.append("中国")
# print(my_list)
#
# # 优化
# my_list = ["中国" for _ in range(10)]
# print(my_list)

# 04:
# 需求: [(0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3)]
# 定义一个列表
my_list = []
for i in range(2):
    for j in range(1, 4):
        # 构造一个元组
        my_tuple = (i, j)
        my_list.append(my_tuple)

# print(my_list)

# 优化
my_list = [(i, j) for i in range(2) for j in range(1, 4)]
print(my_list)