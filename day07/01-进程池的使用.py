# 进程池： 根据执行的任务自动创建进程，完成多任务， 提示： 创建进程的时候是尽量少创建进程
import multiprocessing
import time

# 拷贝的工作任务
def copy_file():

    print("拷贝中...", multiprocessing.current_process().pid)
    # 提示：使用进程池创建进程是守护状态的进程，主进程退出，子进程就销毁了
    print(multiprocessing.current_process().daemon)
    time.sleep(2)


if __name__ == '__main__':
    # 创建进程池
    # 3:表示进程池中进程的最大个数， 如果不写这个参数默认是cpu的核数
    pool = multiprocessing.Pool(3)

    # 模拟大批量的任务，让进程池去执行
    for i in range(10):
        # 让进程池使用同步的方式去执行任务，同步： 一个进程把任务执行完另外一个进程才能执行
        # pool.apply(copy_file)
        # 让进程池使用异步的方式去执行任务， 异步： 表示多个进程一起执行，进程直接不会等待
        pool.apply_async(copy_file)

    # 关闭进程池，表示进程池以后不再执行其它任务了
    pool.close()
    # 主进程等待进程池执行完成以后程序再退出
    pool.join()









