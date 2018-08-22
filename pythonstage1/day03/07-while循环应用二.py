# 2. 计算1~100之间偶数的累积和（包含1和100）

# 定义一个变量 记录数字
num = 1
# 定义变量 保存数据
my_sum = 0
while num < 101:
    # 判断num是否为偶数
    if num % 2 == 0:
        my_sum += num
    num += 1

print("计算1~100之间偶数的累积和:%d" % my_sum)