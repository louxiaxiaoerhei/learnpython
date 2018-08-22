# w a 都可以写入数据
# 如果文件存在 直接打开 如果文件不存在 将创建文件 并打开
# <1>写数据(write)
# w 先清空 然后写入
# # 01: 打开文件
# f = open("hm.txt", "w")
# 写入输入
# f.write("hello world")
# 关闭文件
# f.close()

# a (在原有的数据上进行追加数据)-> append
# f = open("hm.txt", "a")
# f.write("haha")
# f.close()

# # 特例:
# # 默认情况下 windows系统(中国) -> gbk (ascii)
# # pycharm -> utf-8(全球使用) -> Unicode(万国码)
# f = open("hm1.txt", 'w', encoding="utf-8")
# # 写入数据
# f.write("你好")
# # 关闭文件
# f.close()
