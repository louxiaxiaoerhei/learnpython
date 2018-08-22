
# 定义一个复杂的函数
# 形参:正常参数, 缺省参数, 不定长参数(元组, 字典)
# 函数定义的形参顺序: 正常参数 -> (缺省参数和不定长参数之元组顺序可互换) -> 不定长参数之字典
def my_func(a, b=10, *args, **kwargs):
    # 1
    print("a=%d" % a)
    # 2
    print("b=%d" % b)
    # 3, 4, 5, 6
    print("args=", args)
    # xm 22
    print("kwargs=", kwargs)

# 函数的调用
my_func(1, name="xm", age=22)
