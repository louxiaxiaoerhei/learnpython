from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    # 使用响应对象
    response = make_response('set cookie')
    # 设置cookie,max_age设置cookie的有效期，单位秒
    response.set_cookie('itcast','python14',max_age=60)
    # 返回响应
    return response

# 获取cookie信息
@app.route('/get')
def get_cookie():
    print(request.headers)
    itcast = request.cookies.get('itcast')
    return itcast

if __name__ == '__main__':
    app.run(debug=True)