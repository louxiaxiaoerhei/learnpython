
# 定义一个变量 保存名字
name = "小明"
# 输出: 我的名字叫做小明
# %s -> s -> string
print("我的名字叫做%s" % name)

# 定义一个变量 保存年龄
age = 29
# 输出: 我的年龄为29岁
# %d -> d -> digit
print("我的年龄为%d岁" % age)

# 定义一个变量 保存身高
height = 178.55
# 输出: 我的身高为178.55
# 默认情况下 python保存小数点后面六位
# 实际的开发中 一般需要2位或者3位
# %f -> f -> float
print("我的身高为%.3f" % height)

# 定义一个变量 保存性别
is_man = False
# 输出: 是否是男性:True
# bool -> True = 1 False = 0
# print("是否是男性:%d" % is_man)
print("是否是男性:%s" % is_man)