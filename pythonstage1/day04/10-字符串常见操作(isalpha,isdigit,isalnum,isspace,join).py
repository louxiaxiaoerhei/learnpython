a = "   \n"
# # <23>isalpha
# flag = a.isalpha()
# print(flag)

# # <24>isdigit
# flag = a.isdigit()
# print(flag)

# <25>isalnum(数字 字母 数字字母)
# flag = a.isalnum()
# print(flag)

# <26>isspace
# flag = a.isspace()
# print(flag)

# <27>join
# mystr 中每个元素后面插入str,构造出一个新的字符串

# 列表类型
my_list = ["a", "b", "c", "d"]
# 列表 -> 字符串
# "a1b1c1d"
# ret = "1".join(my_list)
# print(ret)

# abcd
ret = "".join(my_list)
print(ret)
