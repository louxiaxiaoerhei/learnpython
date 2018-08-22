import gevent
# 导入网络请求的模块
import urllib.request
from gevent import monkey
# 打补丁失败耗时操作
monkey.patch_all()


# 下载图片的函数
def download_img(img_url, img_name):
    # 获取当前协程
    result = gevent.getcurrent()
    print(result)
    try:
        # 根据图片的地址打开网络资源
        # response: 表示图片在网络中的资源数据
        response = urllib.request.urlopen(img_url)
        with open(img_name, "wb") as img_file:
            while True:
                # 读取网络资源数据(图片的二进制数据)
                img_data = response.read(1024)
                if img_data:
                    # 把读取的图片二进制数据写入到指定文件里面
                    img_file.write(img_data)
                else:
                    break
    except Exception as e:
        print("图片下载异常:", e)
    else:
        print("图片下载成功:", img_name)


if __name__ == '__main__':
    # 图片地址
    img_url1 = "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3338444161,3567926268&fm=27&gp=0.jpg"
    img_url2 = "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3506739232,2945471821&fm=27&gp=0.jpg"
    img_url3 = "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1293860636,1088191402&fm=27&gp=0.jpg"

    # 创建协程
    g1 = gevent.spawn(download_img, img_url1, "1.jpg")
    g2 = gevent.spawn(download_img, img_url2, "2.jpg")
    g3 = gevent.spawn(download_img, img_url3, "3.jpg")
    print(g1, g2, g3)
    # 主线程等待所有的协程执行完成以后程序再退出
    gevent.joinall([g1, g2, g3])

