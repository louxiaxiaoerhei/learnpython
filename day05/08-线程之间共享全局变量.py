import threading
import time


# 定义全局变量
g_list = list() # => []


# 添加数据
def add_data():
    for i in range(5):

        # 因为需要修改全局变量的内存地址，所以需要加上global
        # global g_list
        # g_list = [1,2]

        # 这里不需要加上global,因为我这里没有修改全局变量的内存地址
        g_list.append(i)
        print("添加的数据为:", i)
        print(id(g_list))
        time.sleep(0.1)

    print("add_data:", g_list)


def read_data():
    print("read_data:", g_list)

if __name__ == '__main__':
    # 创建添加数据的线程
    add_thread = threading.Thread(target=add_data)
    read_thread = threading.Thread(target=read_data)

    add_thread.start()

    # 提示：主线程执行到time.sleep的时候需要延时1秒钟
    # time.sleep(1)

    # 线程等待
    # 提示： 主线程等待添加数据的线程执行完成以后程序在继续往下执行
    add_thread.join()

    read_thread.start()

    # 总结： 线程之间可以共享全局变量
