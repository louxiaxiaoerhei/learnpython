import threading


# 带有参数的任务
def task(name, age):
    # 获取当前线程的名字
    print(threading.current_thread().name)
    print(name, age)


if __name__ == '__main__':
    # # 创建子线程
    sub_thread = threading.Thread(target=task, args=("西施", 18), name="mythread")
    # 启动线程执行任务
    sub_thread.start()

    # # 创建子线程
    # sub_thread = threading.Thread(target=task, kwargs={"name": "潘安", "age": 20}, name="mythread")
    # # 启动线程执行任务
    # sub_thread.start()

    # 创建子线程
    # sub_thread = threading.Thread(target=task, args=("小白",), kwargs={"age": 20}, name="mythread")
    # # 启动线程执行任务
    # sub_thread.start()