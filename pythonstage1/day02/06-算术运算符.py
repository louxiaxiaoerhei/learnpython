"""
+ 	加 	两个对象相加 a + b 输出结果 30
- 	减 	得到负数或是一个数减去另一个数 a - b 输出结果 -10
* 	乘 	两个数相乘或是返回一个被重复若干次的字符串 a * b 输出结果 200
/ 	除 	b / a 输出结果 2
// 	取整除 	返回商的整数部分 9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
% 	取余 	返回除法的余数 b % a 输出结果 0
** 	指数 	a**b 为10的20次方， 输出结果 100000000000000000000
"""

# 定义两个变量
num1 = 10
num2 = 100
# +
ret1 = num1 + num2
print(ret1)
# -
ret2 = num1 - num2
print(ret2)

# /
ret3 = num2 / num1
print(ret3)

# // 	取整除
ret4 = num2 // num1
print(ret4)

# % 	取余
ret5 = num2 % num1
print(ret5)

# ** 	指数
ret6 = num1 ** num2
print(ret6)
print(type(ret6))