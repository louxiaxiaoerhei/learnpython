import threading
import time


# 任务
def task():
    time.sleep(1)
    print(threading.current_thread().name)
    print("任务执行完成")


if __name__ == '__main__':
    # 模拟多个线程，去执行task任务
    for i in range(10):
        sub_thread = threading.Thread(target=task)
        print(id(sub_thread))
        sub_thread.start()

    # 总结： 线程之间执行是无序的，是由cpu调度决定的

