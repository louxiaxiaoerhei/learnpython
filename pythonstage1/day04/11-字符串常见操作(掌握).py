# 字符串的分割(字符串 -> 列表)
# a = "abcbdbf"
# ret1 = a.split("b")
# print(ret1)

# 字符串的拼接(列表 -> 字符串)
# my_list = ["1", "2", "3"]
# # 1a2a3
# ret2 = "".join(my_list)
# print(ret2)

#
# ret3 = "我是" + "中国人"
# ret4 = "我是%s" % ("中国人")
# print(ret4)

# 字符串子串查找
# a = "abcbdbf"
# find
# index = a.find("c")
# print(index)

# 字符串子串替换
# replace
# ret5 = a.replace("b", "中国")
# print(ret5)

# 去除字符串两侧空白符
# strip

# 使用index方法查找子串的下标索引
# 非零即真 零则假
# if 0:
#     print("哈哈")
a = "abcbdbf"
my_str = "b"
if a.count(my_str):
    index = a.index(my_str)
    print(index)
else:
    print("%s不存在" % my_str)
