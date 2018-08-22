import multiprocessing
import time
import os


# 跳舞
def dance():

    # 获取当前进程，也就是说这个代码以后在那个进程里面执行
    print("dance:", multiprocessing.current_process())
    # 获取当前进程的编号
    print("dance pid:", multiprocessing.current_process().pid, os.getpid())
    # 获取子进程对应的父进程的编号
    print("dance ppid:", os.getppid())
    for i in range(5):
        print("跳舞中...")
        time.sleep(0.2)
        # 根据进程编号杀死指定进程
        # 1. 进程编号
        # 2. 强制杀死进程
        os.kill(os.getpid(), 9)


# 唱歌
def sing():

    # 获取当前进程，也就是说这个代码以后在那个进程里面执行
    print("sing:", multiprocessing.current_process())
    # 获取当前进程的编号
    print("sing pid:", multiprocessing.current_process().pid)
    # 获取子进程对应的父进程的编号
    print("sing ppid:", os.getppid())
    for i in range(5):
        print("唱歌中...")
        time.sleep(0.2)

if __name__ == '__main__':
    # 获取当前进程，也就是说这个代码以后在那个进程里面执行
    print("main:", multiprocessing.current_process())
    print("main pid:", multiprocessing.current_process().pid)
    # 创建子进程
    # group: 表示进程组，默认值必须使用None
    # target:表示执行的目标函数或者方法
    # args: 以元组的方式给目标任务传参
    # kwargs: 以字典的方式给目标任务传参
    # name: 表示进程名，默认的命名格式： Process-1, xxxxx
    dance_process = multiprocessing.Process(target=dance)
    sing_process = multiprocessing.Process(target=sing)

    # 启动线程
    dance_process.start()
    sing_process.start()