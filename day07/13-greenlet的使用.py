import greenlet
import time


# 任务1
def task1():
    for i in range(5):
        print("任务1执行中。。。")
        time.sleep(0.2)
        # 切换到协程2执行对应的任务
        g2.switch()


# 任务2
def task2():
    for i in range(5):
        print("任务2执行中。。。")
        time.sleep(0.2)
        # 切换到协程1执行对应的任务
        g1.switch()

if __name__ == '__main__':
    # 创建协程并指定执行的任务
    g1 = greenlet.greenlet(task1)
    g2 = greenlet.greenlet(task2)

    # 切换到协程1里面执行对应的任务
    g1.switch()

