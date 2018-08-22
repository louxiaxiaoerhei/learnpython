# 在python中 循环: while 和 for
# 死循环 while
# 循环遍历可迭代对象(字符串 列表等)的时候 for
# 其他的应用场景 看个人喜好

# 01: 循环遍历可迭代对象 字符串
"""
for 临时变量 in 可迭代对象:
    代码
"""
# name = "hello"
# for c in name:
#     print(c)

# while循环
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# for循环
# range(5) -> [0, 5)
# for i in range(5):
#     print(i)

# while循环 6 7 8 9 10
# i = 6
# while i <= 10:
#     print(i)
#     i += 1
# for循环
# range(6, 11) -> [6, 11)
# random(6, 11) -> [6, 11]
# for i in range(6, 11):
#     print(i)