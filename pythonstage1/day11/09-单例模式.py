# 单例模式
# 设计一个类: 通过这个类创建无数个对象 但是无数个对象得地址都是一样的
# 节约内存 提高性能

# 公用工具类
class HMTool(object):

    # 定义一个类属性 保存这个类创建的对象
    instance = None

    def __new__(cls, *args, **kwargs):

        # 判断instance是否有值
        if not cls.instance:
            # 第一次进入new方法
            cls.instance = object.__new__(cls)

        return cls.instance

    # 求和操作
    def add2num(self, a, b):
        return a + b

    # 圆周率
    def get_pi(self):
        return 3.1415926

t1 = HMTool()
print(t1)
print(t1.get_pi())

t2 = HMTool()
print(t2)
print(t2.add2num(10, 20))

#
# t1 = HMTool()
# print(t1)
# print(t1.get_pi())
#
#
# t2 = t1
# print(t2)
# print(t2.add2num(10, 20))

# # 空值类型 None == False
# ret = None
# # <class 'NoneType'>
# # print(type(ret))
# if not ret:
#     print("哈哈")