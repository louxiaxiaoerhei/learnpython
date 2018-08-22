# 保存所有数据的字典
# all_dict = {"小明": {"name":"小明", "age":"22"}, "小红": {"name":"小红", "age":"23"}}
#
# # 分析 如何完成使用文件保存数据(内存 -> 硬盘)
# f = open("student.txt", "w", encoding="utf-8")
# f.write(str(all_dict))
# f.close()

# 分析 如何完成文件的数据读取到内存中(硬盘 -> 内存)
# 读取
f = open("student.txt", "r", encoding="utf-8")
# 读取
# "{'小明': {'name': '小明', 'age': '22'}, '小红': {'name': '小红', 'age': '23'}}"
ret = f.read()
# 关闭
f.close()

# 保存到all_dict中
all_dict = eval(ret)
print(type(all_dict))
