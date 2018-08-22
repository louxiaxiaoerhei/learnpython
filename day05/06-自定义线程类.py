from threading import Thread
from threading import current_thread
import time


# 自定义线程类
class CustomThread(Thread):

    # 提示： 如果自己提供了init方法，那么不会自动调用父类里面的init方法
    def __init__(self, num1, num2):
        # 手动调用父类的init方法
        super(CustomThread, self).__init__() # => super().init()
        self.num1 = num1
        self.num2 = num2

    # 模拟非常复杂的任务
    def task1(self):
        time.sleep(1)
        print("任务1执行完成", self.num1)

    # 模拟非常复杂的任务
    def task2(self):
        time.sleep(1)
        print("任务2执行完成", self.num2)

    # 执行自定义线程类里面的任务同一在run方法里面执行
    def run(self):
        print(current_thread())
        self.task1()
        self.task2()


if __name__ == '__main__':
    # 创建自定义线程对象
    custom_thread = CustomThread(1, 2)
    # run方法不能直接使用对象调用，如果这样调用不是在子线程里面执行，而是在主线程执行
    # custom_thread.run()
    # 提示： 以后启动线程统一使用start方法，start方法内部会自动调用run方法
    custom_thread.start()