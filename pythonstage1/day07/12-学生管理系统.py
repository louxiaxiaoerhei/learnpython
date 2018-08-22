# 分析:保存学生信息数据 应该使用什么数据类型?
# 举例: 小明, 22 小红, 23
# {"name": "小明", "age": 22}
# {"name": "小红", "age": 23}
# 保存所有的学生写信息数据类型选择?
# 列表 pass 元组 pass 字典
# {"小明": {"name": "小明", "age": 22}, "小红": {"name": "小红", "age": 23}}
# all_dict = {"小明": {"name": "小明", "age": 22}, "小红": {"name": "小红", "age": 23}}

# 输入错误
def print_error_name():
    print("您输入的名字有误...")

# 定义一个字典 保存所有人的数据
all_dict = {}
print("      学生管理系统 V1.0")
print(" 1:添加学生")
print(" 2:删除学生")
print(" 3:修改学生")
print(" 4:查询学生")
print(" 5:显示所有学生")
index = input('请选择:')
# 判断
# 1:添加学生
if index == "1":
    # 引导用户输入名字和年龄
    my_name = input("请输入您的名字:")
    my_age = input("请输入您的年龄")
    # 构造一个字典
    my_dict = {"name": my_name, "age": my_age}
    # 保存
    all_dict[my_name] = my_dict
    print("保存数据成功...")

# 2:删除学生
elif index == "2":
    # 引导用户输入删除的名字
    my_name = input("请输入您的名字:")
    # 判断
    if my_name in all_dict:
        # 删除
        del all_dict[my_name]
        print("删除数据成功...")
    else:
        print_error_name()

# 3:修改学生
elif index == "3":
    # 引导用户输入修改的名字
    my_name = input("请输入您的名字:")
    # 判断
    if my_name in all_dict:
        # 引导用户输入新的年龄
        my_age = input("请输入新的年龄:")
        all_dict[my_name]["age"] = my_age
        print("修改数据成功...")
    else:
        print_error_name()
# 4:查询学生
elif index == "4":
    # 引导用户输入查询的名字
    my_name = input("请输入您的名字:")
    if my_name in all_dict:
        print("------个人信息数据------")
        print("姓名:%s" % my_name)
        print("年龄:%s" % all_dict[my_name]["age"])
        print("-----------------------")
    else:
        print_error_name()
# 5:显示所有学生
elif index == "5":
    print("----显示所有人的信息----")
    for k, v in all_dict.items():
        print("姓名:%s" % v["name"])
        print("年龄:%s" % v["age"])
    print("-----------------------")


print(all_dict)