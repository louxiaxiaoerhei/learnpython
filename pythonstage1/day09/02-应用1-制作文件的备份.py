# # 01: 准备好一个文件
# f = open("itcast.txt", "w", encoding="utf-8")
# # 写入数据
# f.write("你还哦的恢复上课哈十几个地理环境阿里事发后胡欠款金额安抚不好看`1wjhjkds")
# # 关闭文件
# f.close()


# # 制作文件的备份
# # 01: 读取源文件的数据
# old_f = open("itcast.txt", "r", encoding="utf-8")
# # 读取数据
# ret = old_f.read()
# # 关闭文件
# old_f.close()
# # 02: 把源文件的数据写入新文件中
# # 创建新文件
# new_f = open("itcast[复件].txt", "w", encoding="utf-8")
# # 写入数据
# new_f.write(ret)
# # 关闭文件
# new_f.close()

# 如果一次读取大量数据 会导致内存暴涨
# 解决方法: 边读取边写入

# 01: 读取源文件的数据
old_f = open("itcast.txt", "r", encoding="utf-8")
# 创建新文件
new_f = open("itcast[复件].txt", "w", encoding="utf-8")

# 死循环
while True:
    # 读取源文件数据
    ret = old_f.read(2)
    if ret:
        # 写入数据
        new_f.write(ret)
    else:

        break

# 关闭文件
old_f.close()
new_f.close()