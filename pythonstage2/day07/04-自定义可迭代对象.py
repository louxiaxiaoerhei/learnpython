# 自定义可迭代对象: 在类里面定义__iter__的方法创建的对象就是可迭代对象
from collections import Iterable


class MyList(object):
    def __iter__(self):
        # 需要一个迭代器，可迭代对象的本质是通过迭代器帮我们把数据获取出来的
        pass


my_list = MyList()
result = isinstance(my_list, Iterable)
print(result)

for value in my_list:
    print(value)




