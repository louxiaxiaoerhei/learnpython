import multiprocessing
import time

# def show():
#     while True:
#         while True:
#             print("哈哈")
#             return
#
# show()


# 向指定队列添加数据
def add_data(current_queue):
    for i in range(5):
        if current_queue.full():
            print("队列满了")
            # 执行return表示函数执行接收
            # return
            break

        print("add_data: ", i)
        current_queue.put(i)
        time.sleep(0.2)


# 向指定队列读取数据
def read_data(current_queue):
    while True:

        # 判断队列是否为空
        if queue.qsize() == 0:
            print("队列空了")
            break

        value = current_queue.get()
        print(value)


if __name__ == '__main__':
    # 创建消息队列
    queue = multiprocessing.Queue(3)

    # 创建添加数据的进程
    add_process = multiprocessing.Process(target=add_data, args=(queue, ))
    read_process = multiprocessing.Process(target=read_data, args=(queue, ))

    # 启动进程执行对应的任务
    add_process.start()
    add_process.join()
    read_process.start()