# and 	x and y 	布尔"与"：如果 x 为 False，x and y 返回 False，否则它返回 y 的值。 	True and False， 返回 False。
# or 	x or y 	布尔"或"：如果 x 是 True，它返回 True，否则它返回 y 的值。 	False or True， 返回 True。
# not 	not x 	布尔"非"：如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 	not True 返回 False, not False 返回 True


# and 与
# 全真则真 一假则假
# 名字
# name = "admin1"
# passwd = "12345"
# # 判断
# if name == "admin" and passwd == "12345":
#     print("登录成功...")

# or 或
# 一真则真 全假则假
# name = "admin1"
# passwd = "123451"
# if name != "admin" or passwd != "12345":
#     print("您输入的用户名或者密码错误...")

# not 非
# 非真则假 非假则真
flag = not False
print(flag)