import threading
import time


# 任务
def work():
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)


def task():
    for i in range(100):
        print("任务执行中...")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子线程
    # 2. daemon=True 设置守护主线程
    sub_thread = threading.Thread(target=work, daemon=True)
    # 1. 设置守护主线程，主线程退出子线程执行销毁，不再执行对应子线程里面的代码
    # 提示： 子线程以后会依赖主线程，主线程退出子线程执行销毁
    # sub_thread.setDaemon(True)

    # 创建子线程
    second_thread = threading.Thread(target=task, daemon=True)

    # 启动线程执行对应的任务
    sub_thread.start()
    second_thread.start()

    time.sleep(1)
    print("over")
    exit()

    # 总结： 主线程会等待所有的子线程执行完成以后程序再退出



