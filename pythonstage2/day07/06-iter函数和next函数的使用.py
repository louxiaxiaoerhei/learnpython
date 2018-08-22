# iter函数： 获取可迭代对象身上的迭代器， 会调用可迭代对象身上的__iter__的方法
# next函数: 获取迭代器中的下一个值，会调用迭代器对象身上的__next__的方法


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
        # print("xxx")
        if self.index < len(self.my_list):
            value = self.my_list[self.index]

            self.index += 1

            return value
        else:
            # 如果迭代完成需要抛出停止迭代的异常
            raise StopIteration


# 创建的是可迭代对象
my_list = MyList()
# 获取可迭代对象身上的迭代器
my_iterator = iter(my_list)

print(my_iterator)

# 根据迭代器获取迭代器中的下一个值
# value = next(my_iterator)
# print(value)

# 提示： while循环不会自己不会停止迭代的异常，需要自己添加
# while True:
#     try:
#         value = next(my_iterator)
#         print(value)
#     except StopIteration:
#         break

# 遍历的是迭代器对象
for value in my_iterator:
    print(value)


# 总结： for循环的本质
# 1. 如果for循环遍历的是可迭代对象，for循环内部会通过iter函数获取可迭代对象的迭代器，然后通过next函数获取迭代器中的下一个值
# 2. 如果for循环遍历的是迭代器对象， for循环内部会通过next函数获取迭代器中的下一个值
# 3. for循环内部自己捕获了停止迭代的异常，程序员自己不需要进程捕获异常的操作