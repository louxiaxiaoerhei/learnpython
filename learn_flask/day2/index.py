from flask import Flask
# 如果传入标准模块名，只会影响static文件的访问。
app = Flask(__name__)

# 补充：
# 1、视图函数名不能重复；因为一个函数不能有两个返回值。
# 2、url可以重复；因为同一个url可以有不同的http请求方法。
# 3、路由的查找：因为路由是通过列表容器实现的，
# 查找顺序是从上到下，依次执行，如果找到，不会继续查找。
# 首先匹配路径、其次匹配请求方法，调用对应的视图函数
@app.route('/',methods=['POST'])
def index():
    print('hello world2019')
    # return 'hello world2019'
    return 'hello world2019'

# @app.route装饰器内部是调用了add_url_rule函数实现的功能。
# app.add_url_rule('/abc','index',index)


@app.route('/')
def index2018():
    return 'hello world2018'


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)

