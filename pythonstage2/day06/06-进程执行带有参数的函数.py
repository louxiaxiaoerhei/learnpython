import multiprocessing


# 显示人员信息
def show_info(name, age):
    print("我叫:%s 年龄:%d" % (name, age))
    # print(name, age)

if __name__ == '__main__':
    # # 创建子进程
    sub_process = multiprocessing.Process(target=show_info, args=("杨钰莹", 18))

    sub_process.start()


    # 创建子进程
    # sub_process = multiprocessing.Process(target=show_info, kwargs={"age": 18, "name": "杨钰莹"})
    #
    # sub_process.start()

    # 创建子进程
    # sub_process = multiprocessing.Process(target=show_info, args=("李四",), kwargs={"age": 18})
    #
    # sub_process.start()