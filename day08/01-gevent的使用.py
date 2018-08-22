import gevent
import time

from gevent import monkey
# 打补丁，让gevent识别耗时操作(time.sleep, 网络请求, tcp accept(), tcp recv())，完成协程之间自动的切换执行
monkey.patch_all()


def task1():
    for i in range(5):
        print("task1...")
        time.sleep(0.2)
        # gevent.sleep(0.2)


def task2():
    for i in range(5):
        print("task2...")
        time.sleep(0.2)
        # gevent.sleep(0.2)

if __name__ == '__main__':
    # 创建协程1, 给协程指派任务并执行，提示： 创建协程完成以后就会执行
    g1 = gevent.spawn(task1)
    # 创建协程2, 给协程指派任务并执行，提示： 创建协程完成以后就会执行
    g2 = gevent.spawn(task2)

    # 主线程等待协程执行完成以后程序再退出
    # g1.join()
    # g2.join()

    # 如果程序会一直运行，那么可以不需要加上join操作，前提需要在循环里面捕获到耗时操作，才会切换到其它协程里面执行对应的任务
    while True:
        time.sleep(0.2)

        # 比如： accept， recv