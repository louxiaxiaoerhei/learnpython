# # 定义一个函数 不定长参数之元组
# def my_func(*args):
#     pass
#
# # 如果调用函数的时候 使用位置参数方式调用
# my_func(1, 3, 5)
#
# # 定义一个函数 不定长参数之字典
# def print_info(**kwargs):
#     print(kwargs["name"])
#     print(kwargs["age"])
#
# # 如果调用函数的时候 使用关键字参数方式调用
# print_info(name="小明", age=22)

# 注意点:
# 不定长参数之字典 也是一个缺省参数(默认值为{})
# def my_func(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
# my_func()

# 扩展:
def my_func(**kwargs):
    print(kwargs)

my_dict = {"name": "小明", "age": 22}

my_func(**my_dict)