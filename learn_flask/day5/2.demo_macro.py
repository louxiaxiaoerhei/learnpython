from flask import Flask,render_template

app = Flask(__name__)
# 宏：本质是函数，macro
# 一般用来实现动态代码的封装，实现模板页面动态功能代码。

@app.route('/')
def index():
    return render_template('demo_macro.html')

if __name__ == '__main__':
    app.run(debug=True)