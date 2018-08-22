import multiprocessing
import time


def work():
    for i in range(5):
        print("工作中...")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子进程
    sub_process = multiprocessing.Process(target=work)
    # 1. 子进程销毁的方式1
    # # 设置守护主进程, 主进程退出子进程直接销毁
    # sub_process.daemon = True
    sub_process.start()

    # 主进程延时0.5秒
    time.sleep(0.5)
    # 2. 让子进程销毁(终止执行)
    sub_process.terminate()
    print("over")
