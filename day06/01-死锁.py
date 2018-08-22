# 死锁： 一直等待对方释放锁的情景叫做死锁。
import threading

# def show():
#     while True:
#         print("xxxx")
#         return
# show()


# 创建互斥锁
lock = threading.Lock()


# 根据下标去取值，保证同一时刻只能有一个线程去取值
def get_value(index):
    # 上锁，保证同一时刻只能有一个线程去执行
    lock.acquire()
    my_list = [1, 4, 5]
    # 判断下标是否越界
    if index >= len(my_list):
        print("下标越界:", index)
        # 这里必须要释放锁，因为当前线程取值不成功，不要影响后面的线程去取值，所有必须要释放
        # 否则出现死锁。
        lock.release()
        return

    value = my_list[index]
    print(value)
    # 释放锁，让后面的线程能够使用锁完成自己的任务
    lock.release()

if __name__ == '__main__':
    # 模拟大量线程
    for i in range(10):
        sub_thread = threading.Thread(target=get_value, args=(i, ))
        # 启动线程执行对应的任务
        sub_thread.start()


