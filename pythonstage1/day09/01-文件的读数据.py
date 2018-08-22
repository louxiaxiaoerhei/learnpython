# # 创建一个文件
# f = open("hm.txt", "w", encoding="utf-8")
# # 写入数据
# f.write("你好中国")
# # 关闭文件
# f.close()

# 读数据(read)
# 01 read
# # 打开文件
# f = open("hm.txt", "r", encoding="utf-8")
# # 读取数据
# ret = f.read()
# print(ret)
# # 关闭文件
# f.close()

# # <3>读数据（readlines）
# # 打开文件
# f = open("hm.txt", "r", encoding="utf-8")
# # 读取数据
# ret = f.readlines()
# # 打印
# print(ret)
# # 关闭文件
# f.close()

# <4>读数据（readline）
# # 打开文件
# f = open("hm.txt", "r", encoding="utf-8")
# # 读取数据
# ret = f.readline()
# # 打印
# print(ret)
#
# # 读取数据
# ret = f.readline()
# # 打印
# print(ret)
# print("-"*10)
# # print("你好中国")
# # print("-"*10)
# # 关闭文件
# f.close()

# <5> read(num)

# 打开文件
f = open("hm.txt", "r", encoding="utf-8")
# 读取数据(一次读取一个字符(一个字节)))
ret = f.read(2)
print(ret)
# ret = f.read(1)
# print(ret)
# 关闭文件
f.close()

