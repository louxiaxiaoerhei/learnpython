# __all__只能约束 模块导入方式为from 模块名 import *
# 只有保存在 __all__中的标识符名字 才可以成功导入使用
__all__ = ["name", "add2num"]

# 变量 -> 函数 -> 类 -> 模块 -> 包

# 定义一个全局变量
name = "制作模块"

# 定义一个函数
def add2num(a, b):
    return a + b

# 定义一个类
class Person(object):
    pass

# 测试(自测)
# 定义一个函数 测试函数
def main():
    print(name)
    print(add2num(10, 22))
    print(Person())

"""
main() 什么时候调用
如果在本模块 进行自测 应该调用 (__main__)
如果别其他模块引用 不应该调用 (hm_itcast)
"""
# print(__name__)
# 判断语句(判断程序的入口)
if __name__ == '__main__':
    main()

