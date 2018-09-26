from flask import Flask,session

app = Flask(__name__)
# 使用配置对象设置密钥
app.config['SECRET_KEY'] = 'KunQxCm1iQ8ixXGeT9muXbxQyczO8ij2DC4RZBse6hXpLBD07FpbX2RuzrtaniZnUX8='


# 状态保持：
# session：基于键值对的字符串，存储在客户端浏览器的cookie中的是session_id(key)，value存储在服务器；
@app.route('/')
def index():
    # 设置session信息
    session['itcast'] = 'python14'
    return 'set session success'

# 获取session
@app.route("/get")
def get_session():
    itcast = session.get('itcast')
    return itcast


if __name__ == '__main__':
    app.run(debug=True)