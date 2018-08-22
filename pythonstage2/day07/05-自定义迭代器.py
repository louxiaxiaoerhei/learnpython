# 自定义可迭代对象: 在类里面定义__iter__的方法创建的对象就是可迭代对象
from collections import Iterable
from collections import Iterator


class MyList(object):
    def __init__(self):
        # 准备一个列表数据
        self.my_list = [1, 4, 6]

    def __iter__(self):
        # 需要一个迭代器，可迭代对象的本质是通过迭代器帮我们把数据获取出来的
        my_iterator = MyIterator(self.my_list)

        result = isinstance(my_iterator, Iterator)
        print("my_iterator:", result)
        return my_iterator


# 自定义迭代器对象: 在类里面提供一个__iter__和一个__next__的方法创建的对象就是迭代器对象
# 迭代器的作用: 记录数据的位置，根据位置在数据对象中获取对应的数据
class MyIterator(object):

    def __init__(self, my_list):
        self.my_list = my_list
        # 记录当前获取数据的下标
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.my_list):
            value = self.my_list[self.index]

            self.index += 1

            return value
        else:
            # 如果迭代完成需要抛出停止迭代的异常
            raise StopIteration


my_list = MyList()
result = isinstance(my_list, Iterable)
print(result)

for value in my_list:
    print(value)

# 提示： 遍历可迭代对象最终是通过迭代器获取数据的



