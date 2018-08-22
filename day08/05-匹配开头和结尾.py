import re

# 以数字开头
match_obj = re.match("^\d.*", "5sdf")

if match_obj:
    # 获取匹配结果数据
    print(match_obj.group())
else:
    print("匹配失败")


# 以数字结尾
match_obj = re.match(".*\d$", "sdft5")

if match_obj:
    # 获取匹配结果数据
    print(match_obj.group())
else:
    print("匹配失败")

# 匹配以数字开头和以数字结尾，中间内容任意
match_obj = re.match("^\d.*\d$", "6sdft5")

if match_obj:
    # 获取匹配结果数据
    print(match_obj.group())
else:
    print("匹配失败")

# 匹配以数字开头和，中间内容任意， 不要4或者7结尾
# 总结： [^47]： 如果^在中括号里面表示除了指定字符都匹配
# ^: 表示以指定字符串开头
match_obj = re.match("^\d.*[^47]$", "6sdfta")

if match_obj:
    # 获取匹配结果数据
    print(match_obj.group())
else:
    print("匹配失败")
