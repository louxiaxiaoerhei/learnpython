# id 就好比是宾馆的门牌号
# 保存数据的地址空间是系统自动分配的
# # 不可变数据类型的引用
a = 10
b = a
print("a=", id(a))
print("b=", id(b))
# 重新赋值
a = 20

# a = 20
print(a)
# b = 10
print(b)
print("a=", id(a))
print("b=", id(b))


# # 可变数据类型的引用
# a = [1, 2]
# b = a
# print("a=", id(a))
# print("b=", id(b))
#
# # 追加数据(在原有的基础上进行追加)
# a.append(3)
# print(a)
# print(b)
# print("a=", id(a))
# print("b=", id(b))
