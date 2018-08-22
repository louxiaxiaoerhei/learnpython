
# 空列表 -> 对象
# 对象 -> 列表类
my_list = list()

# 鲁班 -> 对象
# 对象 -> 英雄类
# 自定义类(英雄类)
# 自定义类 类名 应该遵循大驼峰命名法

# 01: 经典类
class Hero:
    pass

# 02: 经典类
class Hero():
    pass

# 03: 新式类*****
class Hero(object):
    pass

# 如果在python3.x中 没有任何区别 都是继承object
# object是所有类的父类(基类)
# 如果在python2.x中 03是有父类的 01 和02 没有父类