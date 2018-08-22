# # 写一个函数打印一条横线
# def print_line():
#     print("-"*10)
# # print_line()
#
# # 打印自定义行数的横线
# def print_num_line(num):
#     # _代表占位 防止报错
#     for _ in range(num):
#         print_line()
#
# print_num_line(8)



# 写一个函数求三个数的和
def add3num(a, b, c):
    return a + b + c

# ret = add3num(10, 20, 30)
# print(ret)

# 写一个函数求三个数的平均值
def average3num(num1, num2, num3):
    # 求和
    # ret = num1 + num2 + num3
    ret = add3num(num1, num2, num3)
    return ret / 3

result = average3num(10, 20, 30)
print(result)
