import os
# 01: 创建一个黑马文件夹
# os.mkdir("黑马文件夹")
# 进入黑马文件夹 创建10个文件[python16期1..10].txt
# os.chdir("黑马文件夹")
# for i in range(1, 11):
#     f = open("python16期%d.txt" % i, "w")
#     f.close()

# 批量修改文件名
# 进入黑马文件夹
os.chdir("黑马文件夹")
# 读取所有的文件名
name_list = os.listdir()
# 循环遍历
# python16期6.txt -> 顺义-python16期6.txt
for old_name in name_list:
    new_name = "顺义-" + old_name
    # 重命名
    os.rename(old_name, new_name)
