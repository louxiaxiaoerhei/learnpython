my_dict = {"name": "小明", "no": "001", "age": 22}

# <1>查看元素
# my_name = my_dict["name"]
# print(my_name)

# <2>修改元素(如果key存在)
# my_dict["no"] = "007"
# print(my_dict)

# <3>添加元素(如果key不存在)
# my_dict["sex"] = "男"
# print(my_dict)

# <4>删除元素
#
# 对字典进行删除操作，有一下几种：
#
#     del
#     clear()

# del
# del my_dict["age"]
# print(my_dict)

# clear
my_dict.clear()
print(my_dict)
