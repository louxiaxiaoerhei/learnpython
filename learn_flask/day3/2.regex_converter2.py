from flask import Flask
from werkzeug.routing import BaseConverter
from werkzeug.wrappers import Request,Response


app = Flask(__name__)


# 转换器：限制url中参数的数据类型
# 需求：不仅限制参数的数据类型，还要限制参数的长度

# 实现正则转换器类第二种形式：扩展性更强，正则表达式为函数的参数；
class RegexConverter(BaseConverter):
    def __init__(self,map,*args):
        super(RegexConverter, self).__init__(map)
        # print(map)
        self.regex = args[0]
        # print(args[0])

# 把自定义的转换器类添加到默认转换器中
app.url_map.converters['re'] = RegexConverter

@app.route('/<re("[a-zA-Z]{3}"):temp>')
def index(temp):
    return 'hello world%s' % temp

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)