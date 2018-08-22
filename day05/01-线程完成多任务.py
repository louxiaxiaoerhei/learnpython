import threading  # 使用线程完成多任务的模块
import time


# 唱歌
def sing():
    # 获取当前代码执行的线程
    current_thread = threading.current_thread()
    print("sing:", current_thread)
    for i in range(5):
        print("唱歌...")
        # time.sleep(0.2)


# 跳舞
def dance():
    # 获取当前代码执行的线程
    current_thread = threading.current_thread()
    print("dance:", current_thread)
    for i in range(5):
        print("跳舞...")
        time.sleep(0.2)


if __name__ == '__main__':

    # 查看活动线程的列表
    print("1111", threading.enumerate(), type(threading.enumerate()))

    # 获取当前代码执行的线程
    current_thread = threading.current_thread()
    print("main:", current_thread)

    # # 单任务执行，因为只有一个线程
    # dance()
    # sing()
    # 创建跳舞的线程
    # group 表示线程组，这个值线程必须使用None
    # target 表示执行目标函数或者目标方法
    # name 表示线程的名字，可以不用设置，默认线程名字的格式为: Thread-1, ...
    # args 表示给函数或者方法传入参数的时候使用元组
    # kwargs 表示给函数或者方法传入参数的时候使用字典
    # daemon 表示创建的线程可以设置成为守护主线程
    sing_thread = threading.Thread(target=sing, name="sing")
    dance_thread = threading.Thread(target=dance, name="dance")

    # 查看活动线程的列表
    print("2222", threading.enumerate(), type(threading.enumerate()))

    # 启动线程执行对应的任务
    sing_thread.start()
    dance_thread.start()

    # 查看活动线程的列表
    print("3333", len(threading.enumerate()), type(threading.enumerate()))

    # 获取程序中活动线程的个数
    print("4444", threading.active_count())

    # 提示： 线程启动后才会把线程放到活动线程列表里面
    # 提示： 线程执行完任务以后就会销毁，会从活动线程列表里面移除这个线程对象





