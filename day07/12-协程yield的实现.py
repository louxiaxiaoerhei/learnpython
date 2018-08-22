# 协程: 又成为用户级线程， 在不开辟线程的基础上可以完成多任务，多个任务按照一定顺序交替执行
# 如何理解协程: 在def关键字里面只看到一个yield关键字就是表示是一个协程
# 学习协程的目的： 就是在单线程的基础上完成多任务
import time


# 协程1
def work1():
    for i in range(10):
        print("work1。。。。")
        time.sleep(0.2)
        yield


# 协程2
def work2():
    for i in range(10):
        print("work2。。。。")
        time.sleep(0.2)
        yield


if __name__ == '__main__':
    # 创建协程
    g1 = work1()
    g2 = work2()

    for i in range(10):
        next(g1)
        next(g2)



