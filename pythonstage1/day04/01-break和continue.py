# break和continue 配合循环(while for)使用

# while-break
# 如果在while循环中执行了break 那么将终止循环
# break后面的代码将不再被执行
# i = 0
# while i < 5:
#     print(i)
#     if i == 2:
#         print("break前")
#         break
#         print("break后")
#     i += 1
# print("测试")

# for-break
# 和while-break结论是一样的
# for i in range(5):
#     print(i)
#     if i == 2:
#         print("break前")
#         break
#         print("break后")
#
# print("测试")

# while-continue
# 如果在while循环中执行了continue后 将提前结束本次循环 马上进入下次循环
# 如果执行了continue 后 continue后面的代码也将不再执行
# i = 0
# while i < 5:
#     i += 1
#     # ==2
#     if i == 2:
#         print("continue前")
#         continue
#         print("continue后")
#     print(i)
#
# print("测试")

# for-continue
# 结论和while-continue 一样的

for i in range(5):
    if i == 2:
        print("continue前")
        continue
        print("continue后")
    print(i)

print("测试")





















