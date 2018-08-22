import os
# 定义一个全局变量 保存所有的人数据
# {"小明": {"name":"小明", "age":"22"}, "小红": {"name":"小红", "age":"23"}}
all_dict = {}
# 保存文件名
file_name = "student.txt"

# 定义一个公共的函数
def print_error_name():
    print("您输入的名字有误...")

# 引导用户输入名字
def hm_input_name(type_desc):
    return input("请输入%s名字:" % type_desc)

def print_menu():
    print("---------------------------")
    print("      学生管理系统 V1.0")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有学生")
    print(" 6:保存数据")
    print(" 7:退出系统")
    index = input("请选择:")
    print("---------------------------")
    return index

# 0. 读取数据(硬盘  -> 内存)
def load_info():
    # 首先需要判断 保存数据的文件是否存在
    # 服务于第一次
    if not os.path.exists(file_name):
        # 创建文件
        f = open(file_name, "w", encoding="utf-8")
        # 写入数据
        f.write("{}")
        f.close()
        return

    # 读取数据
    f = open(file_name, "r", encoding="utf-8")
    # 读取数据
    ret = f.read()
    global all_dict
    # 数据类型转换
    all_dict = eval(ret)
    # 关闭文件
    f.close()

# 1:添加学生
def add_info():
    # 引导
    my_name = input("请输入名字:")
    my_age = input("请输入年龄:")
    # 构造字典
    my_dict = {"name": my_name, "age": my_age}
    # 保存数据
    all_dict[my_name] = my_dict
    print("保存数据成功...")


# 2:删除学生
def delete_info():
    # 引导用户
    my_name = hm_input_name("删除")
    if my_name in all_dict:
        del all_dict[my_name]
        print("删除数据成功...")
    else:
        print_error_name()


# 3:修改学生
def update_info():
    # 引导
    my_name = hm_input_name("修改")
    if my_name in all_dict:
        # 引导用户输入新的年龄
        my_age = input("请输入您新的年龄:")
        all_dict[my_name]["age"] = my_age
        print("修改数据成功...")
    else:
        print_error_name()

# 4:查询学生
def select_info():
    my_name = hm_input_name("查询")
    if my_name in all_dict:
        print("----------个人信息----------")
        print("姓名:%s" % my_name)
        print("年龄:%s" % all_dict[my_name]["age"])
    else:
        print_error_name()

# 5:显示所有学生
def show_all_info():
    print("----------python16期学生信息----------")
    for k, v in all_dict.items():

        print("姓名:%s" % k)
        print("年龄:%s" % v["age"])
        print("-"*40)


# 6:保存数据(内存  -> 硬盘)
def save_info():
    # 打开文件(创建)
    f = open("student.txt", "w", encoding="utf-8")
    # 写入数据
    f.write(str(all_dict))
    # 关闭文件
    f.close()
    print("内存 -> 硬盘 成功...")

# 定义一个启动整个系统的函数
def run():
    load_info()
    while True:
        index = print_menu()
        if index == "1":
            add_info()
        elif index == "2":
            delete_info()
        elif index == "3":
            update_info()
        elif index == "4":
            select_info()
        elif index == "5":
            show_all_info()
        elif index == "6":
            save_info()
        elif index == "7":
            print("欢迎下次使用...")
            break
        else:
            print("输入错误...")

run()




