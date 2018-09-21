from flask import Flask
from werkzeug.routing import BaseConverter
from werkzeug.wrappers import Response,Request
app = Flask(__name__)
# 视图传参：<>
# url的<>中传入的参数,必须传入视图函数中
# <>里默认是unicode字符串，兼容数值
# 数值之间不兼容
# /区分路径?&#= 锚点
# http://127.0.0.1:5000/abc/e1234/asdf

# Rule类：存储了所有的url规则
# Map类：存储了所有的Rule类对象
# MapAdapter类：负责匹配url和请求方法，满足url和请求方法条件，调用对应的视图函数
# BaseConverter类:实现了正则匹配，匹配url规则。

@app.route('/<temp>')
def index(temp):
    return 'hello %s' % temp

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)