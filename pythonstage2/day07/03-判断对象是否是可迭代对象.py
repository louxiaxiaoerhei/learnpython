# 可迭代对象有: 列表，元组，字典，字符串，集合，range
from collections import Iterable

# 判断对象是否是指定类型
result = isinstance([2, 4], Iterable)
print(result)


result = isinstance((2, 4), Iterable)
print(result)


result = isinstance({"name": "小明"}, Iterable)
print(result)

result = isinstance("hello", Iterable)
print(result)

result = isinstance({1, 5}, Iterable)
print(result)


result = isinstance(range(4), Iterable)
print(result)

num = 5

result = isinstance(num, Iterable)
print(result)


result = isinstance(num, int)
print(result)
# for value in num:
#     print(value)

class AAAA(object):
    pass

aa = AAAA()

result = isinstance(aa, AAAA)
print(result)

# for value in aa:
#     print(value)

def show(name):
    if isinstance(name, str):
        print("字符串")
    else:
        print("不是字符串")


show("2")