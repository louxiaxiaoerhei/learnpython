# # 第1种方式
# a = 4
# b = 5
# c = 0
#
# c = a # c = 4
# a = b # a = 5
# b = c # b = 4
#
# print(a)
# print(b)

# # 第2种方式
# a = 4
# b = 5
# a = a+b  # a = 9, b = 5
# b = a-b  # a = 9, b = 4
# a = a-b  # a = 5, b = 4
# print(a)
# print(b)

# 第3种方式
a, b = 4, 5
a, b = b, a # a = 5, b = 4

print(a)
print(b)