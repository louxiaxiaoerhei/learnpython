# my_str = "哈哈，我要测试"

# utf-8 编码
# my_data = my_str.encode("utf-8")
# print(my_data)

# my_msg = "嘻嘻"
# #  gbk 编码
# my_msg_data = my_msg.encode("gbk")
#
# # 混合二进制数据
# data = my_data + my_msg_data

# 对二进制数据进行解码
# result = data.decode("utf-8", errors="ignore")
#
# print(result)




my_str = "哈哈，我要测试"

# utf-8 编码
my_data = my_str.encode("utf-8")
print(my_data)

my_data += "哈哈".encode("gbk")

# 对二进制数据进行解码
result = my_data.decode("utf-8", errors="ignore")

print(result)




