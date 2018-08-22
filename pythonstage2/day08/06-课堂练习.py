# 1.匹配以数字开头中间内容不管以数字结尾, 结尾不要4或者7
# 2.匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
# 3.匹配出11位手机号码
# 4.匹配出微博中的话题, 比如: #幸福是奋斗出来的#

import re

match_obj = re.match("^\d.*[0-35-68-9]$", "5hello8")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

# \.: 表示对正则表达式的.进行转义，让它作为一个普通的点进行匹配数据

match_obj = re.match("[a-zA-Z0-9_]{4,20}@163\.com", "hello@163.com")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

# 不考虑号段
match_obj = re.match("1\d{10}", "18818188888")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

# 考虑号段
match_obj = re.match("1[3-8]\d{9}", "18818188888")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

match_obj = re.match("1[3-8]\d{8}[0-35-68-9]", "18818188889")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

#幸福是奋斗出来的#
# match_obj = re.match("#.+?#", "#幸福是奋#斗出来的#")
# if match_obj:
#     print(match_obj.group())
# else:
#     print("匹配失败")

match_obj = re.match("#[^#]+#", "#幸福是奋#斗出来的#")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")