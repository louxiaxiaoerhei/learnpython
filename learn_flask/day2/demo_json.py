from flask import Flask,jsonify
import json
app = Flask(__name__)

# json：本质是字符串，基于键值对的字符串；
# 数据格式对象，
# 轻量级的数据交互格式；
#
# {""}
@app.route('/')
def index():
    # 字典
    info = {'name':'python14','age':18}
    # json模块把字典转成json字符串
    json_info = json.dumps(info)
    print(type(json_info))
    # return info # 返回字典
    # 把json字符串转成字典
    # json只能是双引号的基于键值对的字符串。
    # info2 = '{"name":"python14","age":18}'
    # info2 = "{'name':'python14','age':18}"
    # dict_data = json.loads(info2)
    # print(type(dict_data))
    # json.load()
    # json.dump()
    return json_info # 使用json模块的dumps返回json字符串
    # return jsonify(info) # 使用Flask内置的jsonify方法返回json字符串

if __name__ == '__main__':
    app.run(debug=True)