from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print('index run----')
    return 'index run'

# 在第一次请求前执行，只执行一次，before_first_request
@app.before_first_request
def before_first_request():
    print('before_first_request run-----')

# 在每次请求前都执行，before_request
# 作用：权限校验。
@app.before_request
def before_request():
    print("before request run-----")

# 在请求后没有异常的情况下执行，after_request,接收的参数为响应对象，必须返回响应
# 作用：可以在每次请求后设置响应的数据类型Content-Type:text/html/;;application/json;;image/jpg
@app.after_request
def after_request(response):
    print('after request run-----')
    print(response)
    return response

# 在请求后即使有异常也执行，teardown_request，接收的参数为异常信息，可以不返回异常信息
@app.teardown_request
def teardown_request(e):
    print('teardown request run-----')


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)

