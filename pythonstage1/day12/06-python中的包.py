
# 一个包外面的模块 如果导入包内的模块

# # 01: import 包名.模块名
# import hm.hm_abc, hm.hm_123
# # 调用: 包名.模块名.变量名 | 函数名 | 类名
# print(hm.hm_abc.name)

# # 02: from 包名 import 模块名
# from hm import hm_abc
# # 调用: 模块名.变量名 | 函数名 | 类名
# print(hm_abc.name)

# 03: from 包名 import *
# 如果使用 from 包名 import * 导入模块 必须配合包中的__init__.py完成导入
# from hm import *
# 调用: 模块名.变量名 | 函数名 | 类名
# print(hm_123.name)

# # 04: as
# import hm.hm_123 as hmhm_123
# print(hmhm_123.name)