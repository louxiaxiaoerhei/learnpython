# elif -> else if (否则如果)
"""
[90, 100] -> 优
[80, 90) -> 良
[60, 80) -> 中
[0, 60) -> 差
"""

# 定义一个变量 保存分数
# score = 55
# if score >= 90 and score <= 100:
#     print("优")
# elif score >= 80 and score < 90:
#     print("良")
# elif score >= 60 and score < 80:
#     print("中")
# elif score >= 0 and score < 60:
#     print("差")

# 改成
# score = 88
# if score >= 90:
#     print("优")
# elif score >= 80:
#     print("良")
# elif score >= 60:
#     print("中")
# elif score >= 0:
#     print("差")
#
# print("测试")

# 改成
# score = 188
# if score >= 0 and score <= 100:
#     if score >= 90:
#         print("优")
#     elif score >= 80:
#         print("良")
#     elif score >= 60:
#         print("中")
#     elif score >= 0:
#         print("差")
#
#     print("测试")
# else:
#     print("您输入的分数不合法...")

# 改成
score = 88
# 定义一个变量
name = "优"
if score >= 0 and score <= 100:
    if score >= 90:
        pass
    elif score >= 80:
        name = "良"
    elif score >= 60:
        name = "中"
    else:
        name = "差"

    print(name)
else:
    print("您输入的分数不合法...")


# pass 占位 防止程序报错
if True:
    pass

# if
# if-else
# if-elif-...
# if-elif-...-else