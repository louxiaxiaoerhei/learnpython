import os
import shutil # 文件操作高级模块
import multiprocessing


# 拷贝文件的操作
def copy_file(src_dir_path, dst_dir_path, file_name):
    print(multiprocessing.current_process().pid)
    # 生成源文件的路径
    src_file_path = src_dir_path + "/" + file_name
    # 生成目标文件的路径
    dst_file_path = dst_dir_path + "/" + file_name
    # 打开目标文件
    with open(dst_file_path, "wb") as dst_file:
        # 打开源文件
        with open(src_file_path, "rb") as src_file:
            while True:
                # 循环读取源文件的中的数据
                src_file_data = src_file.read(1024)
                if src_file_data:
                    # 写入到目标文件里面
                    # 把源文件的数据写入到目标文件里面
                    dst_file.write(src_file_data)
                else:
                    break



if __name__ == '__main__':
    # 源目录的路径
    src_dir_path = "test"
    # 目标目录的路径
    dst_dir_path = "/home/python/Desktop/test"

    # 判断指定路径是否有目标文件夹
    if os.path.exists(dst_dir_path):
        # 删除指定路径的目录
        shutil.rmtree(dst_dir_path)

    # 创建目标文件夹
    os.mkdir(dst_dir_path)

    # 获取源目录里面文件名列表信息
    file_name_list = os.listdir(src_dir_path)

    # 创建进程池
    pool = multiprocessing.Pool(3)

    # 遍历文件名
    for file_name in file_name_list:
        print(file_name)
        # 使用进程池异步执行拷贝文件的操作，多个文件一起拷贝
        pool.apply_async(copy_file, args=(src_dir_path, dst_dir_path, file_name))

    # 关闭进程池，不再接收其它任务
    pool.close()
    # 主进程等待进程池执行完成以后程序在退出
    pool.join()



        # # 生成源文件的路径
        # src_file_path = src_dir_path + "/" + file_name
        # # 生成目标文件的路径
        # dst_file_path = dst_dir_path + "/" + file_name
        # # 打开目标文件
        # with open(dst_file_path, "wb") as dst_file:
        #     # 打开源文件
        #     with open(src_file_path, "rb") as src_file:
        #         while True:
        #             # 循环读取源文件的中的数据
        #             src_file_data = src_file.read(1024)
        #             if src_file_data:
        #                 # 写入到目标文件里面
        #                 # 把源文件的数据写入到目标文件里面
        #                 dst_file.write(src_file_data)
        #             else:
        #                 break