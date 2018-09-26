from flask import Flask,session
from config import config_dict

app = Flask(__name__)
# app.config['DEBUG'] = True

# 加载配置信息的实现形式三种：
# 1、使用配置对象加载配置信息,重点掌握
app.config.from_object(config_dict['production'])
# 2、使用配置文件加载配置信息，了解
# app.config.from_pyfile('settings.ini')
# 3、使用环境变量加载配置信息，了解
# app.config.from_envvar('SET')

@app.route('/')
def index():
    session['itcast'] = 'python14'
    return 'set session success'



if __name__ == '__main__':
    app.run()