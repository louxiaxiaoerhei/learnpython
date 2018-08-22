
# 交集和并集( & 和 | )

# 定义两个列表
my_list1 = [1, 2, 3, 4]
my_list2 = [3, 4, 5, 6]

# 两个列表转成集合
my_set1 = set(my_list1)
my_set2 = set(my_list2)

# 交集
ret1 = my_set1 & my_set2
print(list(ret1))

# 并集
ret2 = my_set1 | my_set2
print(list(ret2))

# 去重
my_list = list("abcdefaba")
print(my_list)
#
ret3 = list(set(my_list))
print(ret3)

