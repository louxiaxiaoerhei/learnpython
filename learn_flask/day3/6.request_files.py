from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    # 获取postman发送过来文件对象
    abc = request.files.get('abc')
    abc.save('./index.html')

    return 'save image success'

if __name__ == '__main__':
    app.run(debug=True)