# |	匹配左右任意一个表达式
# (ab)	将括号中字符作为一个分组
# \num	引用分组num匹配到的字符串
# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串
import re

# 水果列表
fruit_list = ["apple", "banana", "pear", "peach"]

# 遍历列表
for fruit in fruit_list:
    match_obj = re.match("apple|pear", fruit)
    if match_obj:
        print("%s是我想要吃的" % match_obj.group())
    else:
        print("%s不是我想要吃的" % fruit)

# 匹配出163、126、qq等邮箱
match_obj = re.match("([a-zA-Z0-9_]{4,20})@(163|126|qq)\.com", "hello@163.com")

if match_obj:
    # 默认获取的是第0个分组的数据其实就是整个匹配到的数据
    # print(match_obj.group(0))
    # 获取指定分组数据
    print(match_obj.group(1))
    print(match_obj.group(2))

else:
    print("匹配失败")

# qq:10356

match_obj = re.match("(qq:)([1-9]\d{4,10})", "qq:10356")

if match_obj:
    print(match_obj.group(1))
    print(match_obj.group(2))
else:
    print("匹配失败")

# <html>hh</html>
# \\: 前面的反斜杠对后面的反斜杠进行了转义，最终表示一个真正的反斜杠 \num
match_obj = re.match("<([a-zA-Z1-6]+)>.*</\\1>", "<html>hh</html>")

if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

# \num	引用分组num匹配到的字符串
# <html><h1>www.itcast.cn</h1></html>
match_obj = re.match("<([a-zA-Z1-6]+)><([a-zA-Z1-6]+)>.*</\\2></\\1>", "<html><h1>www.itcast.cn</h1></html>")

if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

match_obj = re.match("<(?P<n1>[a-zA-Z1-6]+)><(?P<n2>[a-zA-Z1-6]+)>.*</(?P=n2)></(?P=n1)>", "<html><h1>www.itcast.cn</h1></html>")

if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")