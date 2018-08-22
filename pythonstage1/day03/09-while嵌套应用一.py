"""
*
**
***
****
*****
"""
# print函数
# print("你好", end="\n") 简写 print("你好")
# print("你好", end="")
# print("世界")

# 分析行数
# i = 1
# while i <= 5:
#     print("*")
#     i += 1

# # 分析列数
# j = 1
# while j <= 5:
#     print("*", end="")
#     j += 1

# 整合
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1




