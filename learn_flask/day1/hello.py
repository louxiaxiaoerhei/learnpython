# 第一步：导入Flask类
from flask import Flask
from werkzeug.routing import BaseConverter


# 第二步：创建Flask程序的实例
# __name__参数的作用：确定程序所在的位置,会默认创建静态路由。
# Flask类必须传入字符串，不能传数值
# 如果传入的是标准模块名，会导致静态路由无法访问，不影响视图函数的访问。
# 如果传入的是任意字符串，都会创建静态路由。
app = Flask(__name__)

# def class if for assert True False
# 第三步：定义装饰器路由和视图函数
# 第一个参数，必须以斜线开始
@app.route('/',methods=['POST','GET'])
def hello2018():
    return 'hello world'


# 第四步：启动服务器
if __name__ == '__main__':
    # 查看路由映射,url的路径映射视图函数名
    print(app.url_map)
    # debug调试模式True表示开启，一般只在开发模式下使用，便于调试代码，代码不需要手动重启，自动更新代码
    # 生产模式下，一定不能开启，内存溢出，
    # app.run(debug=True)
    app.run()


