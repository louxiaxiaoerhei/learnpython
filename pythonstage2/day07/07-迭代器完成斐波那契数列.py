# def show():
#     pass
#
#
# def show1():
#     pass

import sys

# 定义迭代器
class Fibonacci(object):

    def __init__(self, num):
        # num: 表示生成数列的个数
        self.num = num
        # 记录前面数列的两个值
        self.a = 0
        self.b = 1
        # 记录生成数列个数的下标
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.num:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.index += 1
            return result
        else:
            raise StopIteration


fib = Fibonacci(1000)
# result = next(fib)
# print(result)

for value in fib:
    print(value)

# 获取默认递归的次数
# count = sys.getrecursionlimit()
# print(count)
# 设置递归的次数
# sys.setrecursionlimit(2000)
#
# count = sys.getrecursionlimit()
# print(count)

# 总结：迭代器的好处:1. 节省内存，只有获取的值的是才去根据算法获取对应数值，2.没有上限控制