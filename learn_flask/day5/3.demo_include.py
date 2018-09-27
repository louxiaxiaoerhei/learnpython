from flask import Flask,render_template,request

app = Flask(__name__)

# 包含：用来实现原始模板页面的完整复用.
# 通过视图传入的模板数据复用不了。
@app.route('/')
def index():
    return render_template('demo_include.html')

if __name__ == '__main__':
    app.run(debug=True)