# 注释是服务于变量

# 文档说明 可以应用于函数 或者方法

# 定义一个函数 计算两个数的求和操作
def add2num(a, b):
    """
    计算两个数的求和操作
    :param a: 数字1
    :param b: 数字2
    :return: 没有返回值
    """
    ret = a + b
    print(ret)

add2num(10, 20)
help(add2num)