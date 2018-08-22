
# r w a -> 适用于文本文件(直接保存的是字符串) -> 记事本
# rb wb ab -> 适用于二进制文件(保存的是二进制) -> 图片 mp3 mp4

# wb
# f = open("hmhm.txt", "wb")
# # 准备好一个二进制数据
# 字符串 -> 二进制 编码
# ret = "你好".encode("utf-8")
# # <class 'bytes'>
# print(type(ret))
# f.write(ret)
# f.close()

# # rb
# f = open("hmhm.txt", "rb")
# ret = f.read()
# f.close()
# # 二进制 -> 字符串  解码
# print(ret.decode("utf-8"))

