from flask import Flask
from werkzeug.routing import BaseConverter


app = Flask(__name__)


# 转换器：限制url中参数的数据类型
# 需求：不仅限制参数的数据类型，还要限制参数的长度

# 实现正则转换器类第一种形式：扩展性不好，正则表达式为固定格式；
class RegexConverter(BaseConverter):
    regex = '[0-9]{4}'
# 把自定义的转换器类添加到默认转换器中
app.url_map.converters['re'] = RegexConverter

@app.route('/<re:temp>')
def index(temp):
    return 'hello world%s' % temp

if __name__ == '__main__':
    app.run(debug=True)