# .	匹配任意1个字符（除了\n）
# [ ]	匹配[ ]中列举的字符
# \d	匹配数字，即0-9
# \D	匹配非数字，即不是数字
# \s	匹配空白，即 空格，tab键
# \S	匹配非空白
# \w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
# \W	匹配特殊字符，即非字母、非数字、非汉字
import re

# 1. pattern: 正则表达式
# 2. string: 要匹配的字符串
# 3. match_obj: 返回一个匹配结果对象
# .	匹配任意1个字符（除了\n）
match_obj = re.match("t.o", "t\no")
if match_obj:
    print(match_obj)
    # 获取匹配结果的字符串
    result = match_obj.group()
    print(result, type(result))
else:
    print("匹配失败")


# 1. pattern: 正则表达式
# 2. string: 要匹配的字符串
# 3. match_obj: 返回一个匹配结果对象
# [ ]	匹配列举中的任意一个字符
match_obj = re.match("葫芦娃[12]", "葫芦娃2")
if match_obj:
    print(match_obj)
    # 获取匹配结果的字符串
    result = match_obj.group()
    print(result, type(result))
else:
    print("匹配失败")

# 匹配银行卡的其中一位密码, 0-9
match_obj = re.match("[0-9]", "3")
if match_obj:
    print(match_obj)
    # 获取匹配结果的字符串
    result = match_obj.group()
    print(result, type(result))
else:
    print("匹配失败")


# 匹配银行卡的其中一位密码, 0-9
# \d =》 [0-9]
# \d	匹配数字，即0-9
match_obj = re.match("\d", "3")
if match_obj:
    print(match_obj)
    # 获取匹配结果的字符串
    result = match_obj.group()
    print(result, type(result))
else:
    print("匹配失败")

# \D	匹配非数字，即不是数字
match_obj = re.match("\D", "a")
if match_obj:
    print(match_obj)
    # 获取匹配结果的字符串
    result = match_obj.group()
    print(result, type(result))
else:
    print("匹配失败")

# 1. pattern: 正则表达式
# 2. string: 要匹配的字符串
# 3. match_obj: 返回一个匹配结果对象
# \s	匹配空白，即 空格，tab键
match_obj = re.match("葫芦娃\s[12]", "葫芦娃\t2")
if match_obj:
    print(match_obj)
    # 获取匹配结果的字符串
    result = match_obj.group()
    print(result, type(result))
else:
    print("匹配失败")


# 1. pattern: 正则表达式
# 2. string: 要匹配的字符串
# 3. match_obj: 返回一个匹配结果对象
# \S	匹配非空白
match_obj = re.match("葫芦娃\S[12]", "葫芦娃哈2")
if match_obj:
    print(match_obj)
    # 获取匹配结果的字符串
    result = match_obj.group()
    print(result, type(result))
else:
    print("匹配失败")

# 匹配某个网站中的一位密码，密码组成是有字母、数字、下划线
match_obj = re.match("[a-zA-Z0-9_]", "_")
if match_obj:
    print(match_obj)
    # 获取匹配结果的字符串
    result = match_obj.group()
    print(result, type(result))
else:
    print("匹配失败")

# 匹配某个网站中的一位密码，密码组成是有字母、数字、下划线
# [a-zA-Z0-9_]
# \w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
match_obj = re.match("\w", "哈")
if match_obj:
    print(match_obj)
    # 获取匹配结果的字符串
    result = match_obj.group()
    print(result, type(result))
else:
    print("匹配失败")

# \W	匹配特殊字符，即非字母、非数字、非汉字
match_obj = re.match("\W", "+")
if match_obj:
    print(match_obj)
    # 获取匹配结果的字符串
    result = match_obj.group()
    print(result, type(result))
else:
    print("匹配失败")