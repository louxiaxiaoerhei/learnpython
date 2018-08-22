# 03: 应用于自定义排序中 -> 配合列表的sort

# stus = [{"name": "zhangsan", "age": 18}, {"name": "lisi", "age": 19}, {"name": "wangwu", "age": 17}]

# 排序 :[{"name": "wangwu", "age": 17}, {"name": "zhangsan", "age": 18}, {"name": "lisi", "age": 19}]
# TypeError: unorderable types: dict() < dict()
# stus.sort()
# print(stus)

# 自定义排序 匿名函数
# 格式:需要排序的列表.sort(key=lambda 临时变量(列表的每个元素):临时变量[key])
# age
# stus.sort(key=lambda dict:dict["age"])
# print(stus)
# name
# stus.sort(key=lambda dict:dict["name"])
# print(stus)

# # 扩展
# my_list = [[12, 1, 20], [5, 3, 31], [90, 3, 1]]
# # 第三个元素排序
# my_list.sort(key=lambda new_list:new_list[2], reverse=True)
# print(my_list)
