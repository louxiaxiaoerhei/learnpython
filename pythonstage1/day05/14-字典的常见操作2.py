
my_dict = {"name": "小明", "no": "001", "age": 22}

# <1>len() 键值对 元素

# <2>keys
# keys_list = my_dict.keys()
# print(list(keys_list))

# <3>values
# values_list = my_dict.values()
# print(list(values_list))

# <4>items
# items_list = my_dict.items()
# print(list(items_list))

# <5> 判断key是否存在
# in
# if "name" in my_dict:
#     print("存在")


# <6> 通过key获取value值得方式有几种
# 三种方式
# 01:
# my_name = my_dict["name"]
# print(my_name)

# 02:
"""
setdefault
# 如果key存在 那么直接获取value的值
# 如果key不存在 那么会使用设置的默认值 (会组成一个新的键值对添加到字典中)
"""
# my_name = my_dict.setdefault("name1", "哈哈")
# print(my_name)
# print(my_dict)

# 03:
"""
get
# 如果key存在 那么直接获取value的值
# 如果key不存在 那么会使用设置的默认值 (不会对字典做任何操作)
"""
# my_name = my_dict.get("name1", "哈哈")
# print(my_name)
# print(my_dict)o