from flask import Flask, redirect, url_for

app = Flask(__name__)

# redirect重定向：
# 作用：当项目或网站文件发生变化的时候，
# 重新想一个新的url地址，发送网络请求
@app.route('/abc')
def index():
    # 定义活动页面
    url = 'http://www.hao123.com'
    return redirect(url)
    # return render_template('goods.html') # 商品页面

# login、register、order、goods等等

# url_for的使用：反向解析
# 因为url_for扩展性更强，相对于url地址，视图函数名更稳定，不容易变化。
@app.route('/')
def url_for_demo():
    return redirect(url_for('index'))

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)