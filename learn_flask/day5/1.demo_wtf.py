from flask import Flask,render_template
# 1-----导入flask_wtf扩展包提供的表单类
from flask_wtf import FlaskForm
# 2-----导入wtf扩展提供的表单字段
from wtforms import StringField,PasswordField,SubmitField
# 3-----导入wtf扩展提供的验证函数
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)
# 设置密钥，根据密钥生成csrf_token
app.config['SECRET_KEY'] = '123'


# 需求：实现简单的注册页面，有文本标签、密码标签、按钮标签。
# 流程：
# 1、自定义表单类
class Form(FlaskForm):
    # 定义表单字段，添加验证函数
    user = StringField(validators=[DataRequired()])
    pswd = PasswordField(validators=[DataRequired()])
    pswd2 = PasswordField(validators=[DataRequired(),EqualTo('pswd')])
    submit = SubmitField('注册')


@app.route('/',methods=['GET','POST'])
def hello_world():
    # 2、实例化表单类对象,把表单对象传入模板
    form = Form()
    # 验证函数生效后，获取表单参数,返回值为布尔类型，
    # 不仅会验货表单中的数据是否满足验证器的要求
    # 还会验证表单中是否设置了csrf_token
    if form.validate_on_submit():
        user = form.user.data
        pswd = form.pswd.data
        pswd2 = form.pswd2.data
        print(user,pswd,pswd2)
        print(form.validate_on_submit())
    # 默认输出
    print(form.validate_on_submit())

    return render_template('demo_wtf.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
