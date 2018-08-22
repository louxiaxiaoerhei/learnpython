import random
# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配
#　一个学校，有3个办公室
school_list = [[], [], []]

# 保存八名老师
teacher_list = list("ABCDEFGH")
# 循环遍历teacher_list
for name in teacher_list:
    # 随机保存到school_list中的每个小列表(办公室)中
    index = random.randint(0, len(school_list) - 1)
    # 通过下标索引获取小列表 进行追加数据
    school_list[index].append(name)

print(school_list)