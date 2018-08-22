# 变量是用来临时保存数据的 -> 内存
# 文件是用来做持久化保存数据的 -> 硬盘(磁盘)

# 打开文件的模式(操作文件的权限)
# r -> 只读模式
# w -> 只写模式
# a -> 追加模式
# 文件的打开
# open(需要打开的文件名, 操作文件的权限)
# FileNotFoundError: [Errno 2] No such file or directory: 'hm.txt'
# # r -> 只读模式
# 如果文件存在 直接打开 如果文件不存在 将报错
# f = open("hm.txt", "r")

# w -> 只写模式
# 如果文件存在 直接打开 如果文件不存在 会创建一个文件 并打开
# f = open("hm.txt", "w")

# a -> 追加模式
# 如果文件存在 直接打开 如果文件不存在 会创建一个文件 并打开
# f = open("hm1.txt", "a")


# 文件的关闭
f = open("hm.txt", "r")
# 文件关闭(当文件不再使用的时候 需要程序员关闭 释放内存)
# 默认情况下 如果程序退出 系统会检测 如果文件没有关闭 系统会帮我们关闭
f.close()