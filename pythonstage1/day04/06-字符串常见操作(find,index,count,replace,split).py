# 定义一个字符串
a = "Aababcadbef"

# # <1>find
# # 检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1
# index = a.find("q")
# print(index)

# # <2>index
# # 跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
# index = a.index("q")
# print(index)

# <3>count
# 返回 str在start和end之间 在 mystr里面出现的次数
# count = a.count("a", 0, 2)
# print(count)

# # <4>replace
# # 字符串是不可变的数据类型
# # 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
# ret = a.replace("a", "A", 2)
# print(a)
# print(ret)

# <5>split
ret = a.split("a")
# <class 'list'>
print(type(ret))
print(a)
print(ret)