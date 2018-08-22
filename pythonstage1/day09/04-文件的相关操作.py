# 导入模块
import os
import shutil
# 1. 文件重命名
# rename(old, new)
# os.rename("hm.txt", "hm123.txt")

# 2. 删除文件
# os.remove("itcast[复件].txt")

# 3. 创建文件夹
# os.mkdir("黑马文件夹")

# 4. 获取当前目录
# ret = os.getcwd()
# print(ret)

# 5. 改变默认目录
# # 绝对路径:带有盘符的路径
# # 相对路径: ./(在当前路径) 或者 ../(当前路径的上一级)
# print(os.getcwd())
# # os.chdir("C:\北京黑马顺16期代码")
# os.chdir("./")
# print(os.getcwd())

# 6. 获取目录列表
# 以.开头的文件 称之为隐藏文件
# name_list = os.listdir()
# print(name_list)

# 7. 删除文件夹(删除空的文件夹)
# os.rmdir("黑马文件夹")

# 8.shutil.rmtree
# 创建文件
# os.mkdir("黑马文件夹")
# 在黑马文件夹下面创建一个itheima.txt文件
# 进入目录下
# os.chdir("黑马文件夹")
# print(os.getcwd())
# f = open("itheima.txt", "w")
# f.close()

# os.rmdir("黑马文件夹")
shutil.rmtree("黑马文件夹")