"""
字符串
列表
元组
字典
集合
"""

# for循环
# 字符串
for c in "hello":
    print(c)

print("-------------------")
for value in [1, 3, 5, 7]:
    print(value)

print("-------------------")
for value in (2, 4, 6, 8):
    print(value)

print("-------------------")
# for key in {"name": "xiaoming", "age": 22}.keys():
#     print(key)
#
# for value in {"name": "xiaoming", "age": 22}.values():
#     print(value)

# for item in {"name": "xiaoming", "age": 22}.items():
#     print("key=%s" % item[0])
#     print("values=%s" % item[1])
# 直接获取字典中元素的key 和 value
# for key, value in {"name": "xiaoming", "age": 22}.items():
#     print("key=%s" % key)
#     print("values=%s" % value)
print("-------------------")

# 定义一个列表
my_list = list("abcd")

# 打印每个数值 和对应每个元素的下标索引
# for value in my_list:
#     print("value=%s" % value)
#     index = my_list.index(value)
#     print("index=%d" % index)
# 打印每个数值 和对应每个元素的下标索引
for index, value in enumerate(my_list):
    print("value=%s" % value)
    print("index=%d" % index)