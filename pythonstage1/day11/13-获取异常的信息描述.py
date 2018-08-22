

# 一个异常: except 异常类型 as 定义一个变量 保存信息描述:
# try:
#     print(num)
# except NameError as abc:
#     print("捕获到了异常", abc)


# 捕获异常
# 多个异常: except (异常类型1, 异常类型2, 异常类型...) as 定义一个变量 保存信息描述:
try:
    # 如果捕获到了异常 代码不再向下执行 直接进入except
    f = open("hm1.txt", "r")
    print(num)
except (FileNotFoundError, NameError) as e:
    print("捕获异常", e)