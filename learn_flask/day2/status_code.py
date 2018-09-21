from flask import Flask, abort
from werkzeug.wrappers import Response
app = Flask(__name__)


# 状态码
# 返回自定义的状态码的作用：实现前后端的数据交互。
"""
var params = {}
$.ajax({
    url:'/',
    type:'get',
    data:JSON.stringify(params),
    dataType:'json' # 后端返回的数据格式
    contentType:'application/json' # 发送到后端的数据格式
    success:function(response){
        if (response.errno == '0'){
            alert()
        }elif(response.errno == '4101')
            alert(reponse.errmsg)
        }
    }
})

errno=0,errmsg='OK'
errno=4101,errmsg='未查询到数据'

"""
@app.route('/index')
def index():
    # return后面可以直接返回状态码，可以返回不符合http协议的状态码
    return 'hello world',4101

# 异常处理
# abort函数用来实现错误信息的捕获，类似于python中raise语句,一般用来实现自定义的错误信息，提高用户体现。
# abort函数一被触发，后面的代码不会执行，一般会在try中使用abort。
# abort函数只能抛出符合http协议的异常状态码，不能自定义，本质是异常处理。
@app.route('/')
def hello():
    # a = 1
    # print(a)
    # try:
    #     pass
    # except Exception as e:
    #     abort(500)
    return 'hello 404',666

# errorhandler装饰器接收的参数为状态码,该装饰器修饰的函数，必须接受异常信息作为参数
@app.errorhandler(500)
def error_handler(e):
    return '您访问的页面过期了，请访问***页面'



if __name__ == '__main__':
    app.run(debug=True)