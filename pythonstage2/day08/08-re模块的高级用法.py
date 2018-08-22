import re

# 查找指定正则表达式，只查找一次
# pattern: 正则表达式
# string: 要匹配的字符串
match_obj = re.search("\d+", "苹果有10个 鸭梨5个")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

# match_obj = re.match("苹果有(\d+)个", "苹果有10个")
# if match_obj:
#     print(match_obj.group(1))
# else:
#     print("匹配失败")

# 查找指定正则表达式，查找多次
# pattern: 正则表达式
# string: 要匹配的字符串
result = re.findall("\d+", "苹果有10个 鸭梨5个")
print(result, type(result))


# sub: 根据正则表达式替换指定数据
# pattern: 正则表达式
# repl： 替换后的内容
# string 要替换的字符串
# count=0: 默认是0表示全部替换， count=1表示只替换一次
result = re.sub("\d+", "30", "阅读数:10 评论数:20", count=1)
print(result)

# 这里的match_obj不需要我们程序员去传入这个参数，系统自动传入正则表达式匹配的结果对象
def replace_str(match_obj):
    # 获取匹配结果数据
    value = match_obj.group()
    result = int(value) + 1
    # 提示： 返回的数据类型必须是字符串
    return str(result)

result = re.sub("\d+", replace_str, "阅读数:10")
print(result)


fruit_list_str = "苹果:鸭梨,香蕉:桃子"

# 1. 正则
# 2. 要匹配的字符串
# 3. maxsplit=0默认值是0表示全部分割，maxsplit=1表示分割1次
result = re.split(":|,", fruit_list_str, maxsplit=1)
print(result)

