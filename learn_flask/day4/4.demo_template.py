# 导入render_template函数，封装了Jinja2模板引擎
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 使用render_template函数调用模板
    # return '<h1>hello world</h1>'
    # 定义变量传给模板
    data = 'python14'
    data_dict = {'name':'python14','age':18}
    data_list = [2,4,5,6,7,9]
    return render_template('demo_template.html',data=data,data_dict=data_dict,data_list=data_list)

if __name__ == '__main__':
    app.run(debug=True)

