import threading


# def show():
#     print("show")
#
# a = show
# a()


# 定义全局变量
g_num = 0
# 创建互斥锁, Lock 是一个变量指向的是一个函数
lock = threading.Lock()


# 任务1， 循环1000000次，每循环一次给全局变量加1
def task1():
    # 上锁
    lock.acquire()
    # 这里加上global是因为全局变量是不可变类型，数据改变内存地址会发生变化，所以必须加上global关键字
    global g_num
    for i in range(1000000):
        g_num += 1

    print("task1:", g_num)
    # 释放锁
    lock.release()


# 任务2， 循环1000000次，每循环一次给全局变量加1
def task2():
    # 上锁
    lock.acquire()
    # 这里加上global是因为全局变量是不可变类型，数据改变内存地址会发生变化，所以必须加上global关键字
    global g_num
    for i in range(1000000):
        g_num += 1

    print("task2:", g_num)
    # 释放锁
    lock.release()

if __name__ == '__main__':
    # 创建子线程
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    # 启动任务
    first_thread.start()
    second_thread.start()

    # 总结： 互斥锁可以解决全局变量资源竞争的问题，保证同一时刻只有一个线程去执行任务
    # 提示：加上互斥锁（同步锁）表示多任务瞬间变成单任务执行
