import multiprocessing
import time

if __name__ == '__main__':
    # 创建消息队列
    # 3:表示消息队列的最大个数， 默认值：-1，表示队列里面有任意多个数据
    queue = multiprocessing.Queue(3)

    # 向队列里面放入数据
    queue.put("hello")
    queue.put(1)
    queue.put([2,5])

    # 如果队列满了，使用put放入数据会等待，直到队列有空闲位置才能放入成功
    # queue.put((2, 3))

    # 如果队列满了，使用put_nowait放入数据不会等待，数据放入不成功会崩溃
    # queue.put_nowait((2, 3))

    # 建议： 向队列添加数据使用put方法

    # 总结: 队列可以放入任意类型的数据

    # for i in range(1000000):
    #     pass

    # 解决办法：　１．使用耗时操作
    # time.sleep(0.001)

    # 2. 通过qsize去判断是否为空

    if queue.qsize() == 0:
        print("队列为空")
    else:
        print("队列不为空")

    # 判断队列是否为空, 不可靠，需要加上一定的耗时操作
    # result = queue.empty()
    # print(result)
    # 判断队列是否满了
    # result = queue.full()
    # print(result)

    # 查看当前队列消息的个数
    size = queue.qsize()
    print("size:", size)
    # 获取队列里面的数据
    value = queue.get()
    print(value)
    # 查看当前队列消息的个数
    size = queue.qsize()
    print("size:", size)
    value = queue.get()
    print(value)
    value = queue.get()
    print(value)

    # 如果队列空了，那么使用get获取数据会等待，直到队列有数据才能获取
    # value = queue.get()
    # print(value)
    # 如果队列空了，那么使用get_nowait获取数据不会会等待，数据获取不成功会崩溃
    # value = queue.get_nowait()
    # print(value)
    # 建议： 获取数据使用get方法
    if queue.qsize() == 0:
        print("队列为空")
    else:
        print("队列不为空")