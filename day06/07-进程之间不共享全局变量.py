import multiprocessing
import time

# 定义全局变量
my_list = list()


# 添加数据
def add_data():
    for i in range(5):
        print("add", i)
        my_list.append(i)
        time.sleep(0.2)

    print("add_data:", my_list)


# 读取数据
def read_data():
    print("read_data:", my_list)


if __name__ == '__main__':
    # 创建添加数据的进程
    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)

    add_process.start()

    # 主进程等待添加数据进程执行完成以后程序再继续往下执行
    add_process.join()

    read_process.start()

    print("main:", my_list)

    # 总结： 进程之间不共享全局变量，因为进程之间相互独立。
    # 创建子进程相当于对主进程进行了一个拷贝，子进程其实就是主进程的一个副本