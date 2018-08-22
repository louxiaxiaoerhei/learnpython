# # <2>import(全部导入)
# # 格式: import 模块名
# # 在一个模块中导入了另一个模块 另一个模块 就会进行这个模块扫描
# import hm_itcast
# # 调用: 模块名.变量名 或者 .函数名 或者 .类名
# print(hm_itcast.name)
# print(hm_itcast.add2num(10, 20))
# print(hm_itcast.Person())

# # <3>from…import(选择性导入)
# from hm_itcast import name, add2num, Person
# # 格式: from 模块名 import 变量名, 函数名, 类名
# # 调用 直接使用 不需要写模块名
# print(name)

# # <4>from … import * (全部导入 不需要写模块名)
# from hm_itcast import *
# print(name)
# print(add2num(10, 20))

# <5> as(给变量名 函数名 类型 起别名)
# from hm_itcast import name as my_name
# print(my_name)
# name = "小明"
# print(name)
# print(my_name)

# <6> 如果使用import 导入多个模块名
# import hm_itcast
# import random
# import keyword
import hm_itcast, random, keyword