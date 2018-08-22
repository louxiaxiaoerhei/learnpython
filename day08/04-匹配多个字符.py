# *	匹配前一个字符出现0次或者无限次，即可有可无
# +	匹配前一个字符出现1次或者无限次，即至少有1次
# ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
# {m}	匹配前一个字符出现m次
# {m,n}	匹配前一个字符出现从m到n次
import re

# *	匹配前一个字符出现0次或者无限次，即可有可无
match_obj = re.match("t.*o", "to")
if match_obj:
    # 获取匹配结果数据
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

# ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
match_obj = re.match("t.+o", "tsdfo")
if match_obj:
    # 获取匹配结果数据
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

# ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
match_obj = re.match("https?", "http")
if match_obj:
    # 获取匹配结果数据
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

# {m}	匹配前一个字符出现m次
match_obj = re.match("ht{2}p", "htp")
if match_obj:
    # 获取匹配结果数据
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

# {m,n}	匹配前一个字符出现从m到n次
match_obj = re.match("to{1,2}", "to")
if match_obj:
    # 获取匹配结果数据
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

# {m,}: 匹配前一个字符至少出现m次
match_obj = re.match("to{1,}", "tooo")
if match_obj:
    # 获取匹配结果数据
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

