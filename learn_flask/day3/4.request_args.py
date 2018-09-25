from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # 获取客户端在url中传入的查询字符串参数
    # http://127.0.0.1:5000/?info=itcast
    # http://127.0.0.1:5000/?info=itcast&name=python66
    info = request.args.get("info")
    name = request.args.get("name")
    # 输出请求的url和方法，请求头
    print(request.url)
    print(request.method)
    print(request.headers)
    return jsonify(info=info,name=name)

if __name__ == '__main__':
    app.run(debug=True)