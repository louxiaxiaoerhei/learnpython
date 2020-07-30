from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('demo_filter.html')

# 自定义过滤器一
# 建议使用：因为自定义过滤器不会写在实现程序实例的地方；
def list_filter(ls):
    list_data = list(ls)
    list_data.reverse()
    return list_data

# 添加过滤器给模板,自定义过滤器名称如果和内置过滤器重名，会发生重写内置过滤器。
app.add_template_filter(list_filter,'ls')

# 自定义过滤器二：
@app.template_filter('lss')
def list_filter(ls):
    list_data = list(ls)
    list_data.reverse()
    return list_data


if __name__ == '__main__':
    app.run(debug=True)