from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    # 获取post请求的表单参数
    name = request.form.get("name")
    password = request.form.get("password")
    return jsonify(name=name,password=password)

if __name__ == '__main__':
    app.run(debug=True)