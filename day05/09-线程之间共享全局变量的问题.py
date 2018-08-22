import threading

# 定义全局变量
g_num = 0


# 任务1， 循环1000000次，每循环一次给全局变量加1
def task1():
    # 这里加上global是因为全局变量是不可变类型，数据改变内存地址会发生变化，所以必须加上global关键字
    global g_num
    for i in range(1000000):
        g_num += 1

    print("task1:", g_num)


# 任务2， 循环1000000次，每循环一次给全局变量加1
def task2():
    # 这里加上global是因为全局变量是不可变类型，数据改变内存地址会发生变化，所以必须加上global关键字
    global g_num
    for i in range(1000000):
        g_num += 1

    print("task2:", g_num)


if __name__ == '__main__':
    # 创建子线程
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    # 启动任务
    first_thread.start()
    # 主线程等待第一个线程执行完成以后再执行执行第二个线程
    first_thread.join()
    second_thread.start()

    # 总结： 多个线程对共享数据(全局变量)操作可能出现资源竞争，数据错乱的问题

    # 解决办法:

    # 原来的多个线程一起执行，线程瞬间变成了一个线程执行完另外一个线程去值，多任务瞬间变成了单任务
    # 提示：执行效率变低了。