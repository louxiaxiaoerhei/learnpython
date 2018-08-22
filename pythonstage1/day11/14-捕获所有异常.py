
# 01
# try:
#     # 如果捕获到了异常 代码不再向下执行 直接进入except
#     f = open("hm1.txt", "r")
#     print(num)
#     print(10/0)
# except Exception:
#     print("捕获异常")

# try:
#     # 如果捕获到了异常 代码不再向下执行 直接进入except
#     f = open("hm1.txt", "r")
#     print(num)
#     print(10 / 0)
# except:
#     print("捕获异常")

# 捕获所有异常 而且获取异常信息描述
try:
    # 如果捕获到了异常 代码不再向下执行 直接进入except
    f = open("hm1.txt", "r")
    print(num)
    print(10/0)
except Exception as e:
    print("捕获异常")