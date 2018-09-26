from flask import Flask
# 1----导入flask_script扩展包
from flask_script import Manager


app = Flask(__name__)
# 2-----实例化Manager管理器对象
manage = Manager(app)

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    # 3-----代理app调用run方法启动服务器
    manage.run()