# 字符串其实就是一个有序的字符序列
# 字符串中最小单元字符(元素)
# 01字符串的定义
a = 10
pi = 3.14
flag = True
# 保存 中文 或者 字母 或者 符号
my_str = "中国abc-="

# 02: '' 和 ""等价
# my_str1 = "abc"
# my_str2 = 'abc'
# if my_str1 == my_str2:
#     print("等价的")

# 03:使用三引号 可以保存文本的格式
# my_str3 = """你好
# 时间
# hello
# world"""
# print(my_str3)

# 04: 定义一个特殊的字符串(空字符串)
my_str4 = ""
print(type(my_str4))
# 或者
my_str4 = str()
# 如何计算字符串中有多少个元素(字符)
# len函数
l = len(my_str4)
print(l)


"""
内置函数
type 查看一个变量或者数据的类型
len 计算字符串中元素的个数
print 输出
input 输入
"""