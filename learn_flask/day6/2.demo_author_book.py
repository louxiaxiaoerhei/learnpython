from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# 导入wtf扩展提供的表单类、验证函数、字段类型
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
# 配置数据库的链接,动态追踪修改、展示sql语句
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = '123'
# 在请求过程中自动提交数据
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

"""
需求：作者图书案例
思路分析：
1、添加数据：web表单，wtf扩展，验证函数、自定义表单类，密钥，csrf
2、删除数据：点击删除标签，应该告诉后端，要删除哪条数据？前端传参，/delete_author/<int:主键id>;
3、业务逻辑：查询数据，定义模型类，author/book，配置数据库的链接等信息
4、数据展示：使用模板，使用语句{%for%}{%endfor%}

流程：先实现简单的功能，然后在拓展新的功能。

"""
db = SQLAlchemy(app)

# 定义模型类,作者和图书
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))

    def __repr__(self):
        return '作者：%s' % self.name

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True)
    info = db.Column(db.String(32))

    def __repr__(self):
        return '书籍：%s' % self.info

# 自定义表单类
class Form(FlaskForm):
    wtf_author = StringField(validators=[DataRequired()])
    wtf_book = StringField(validators=[DataRequired()])
    wtf_submit = SubmitField('保存')

# 业务逻辑
@app.route('/',methods=['GET','POST'])
def index():
    # 实例化表单类对象
    form = Form()
    # 异常处理，对数据库的增删改查操作需要try，调用第三方接口要try
    try:
        # 查询数据库，获取数据
        author = Author.query.all()
        book = Book.query.all()
    except Exception as e:
        print(e)
        author,book = None,None
    # 获取表单参数
    if form.validate_on_submit():
        wtf_au = form.wtf_author.data
        wtf_bk = form.wtf_book.data
        # 保存数据，必须要通过模型类保存
        au = Author(name=wtf_au)
        bk = Book(info=wtf_bk)
        try:
            # 提交数据
            db.session.add_all([au,bk])
            db.session.commit()
        except Exception as e:
            print(e)
            # 如果提交数据发生异常，需要进行回滚
            db.session.rollback()
        # 提交数据后需要再次查询数据库
        author = Author.query.all()
        book = Book.query.all()

    return render_template('demo_author_book.html',form=form,author=author,book=book)

# 删除作者
@app.route("/delete_author/<int:id>")
def del_author(id):
    # 根据id查询数据库
    au = Author.query.get(id)
    # au = Author.query.filter(Author.id==id).first()
    # au = Author.query.filter_by(id=id).first()
    try:
        db.session.delete(au)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    # 删除数据后，需要动态展示删除后的数据，因为index视图函数已经实现了查询，所以
    # 直接重定向到index视图函数即可
    return redirect(url_for('index'))

# 删除书籍
@app.route('/delete_book<int:id>')
def del_book(id):
    bk = Book.query.filter(Book.id==id).first()
    try:
        db.session.delete(bk)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    return redirect(url_for('index'))


if __name__ == '__main__':
    # 先删除表，再创建表
    db.drop_all()
    db.create_all()
    au_xi = Author(name='我吃西红柿')
    au_qian = Author(name='萧潜')
    au_san = Author(name='唐家三少')
    bk_xi = Book(info='吞噬星空')
    bk_xi2 = Book(info='寸芒')
    bk_qian = Book(info='飘渺之旅')
    bk_san = Book(info='冰火魔厨')
    # 把数据提交给用户会话
    db.session.add_all([au_xi, au_qian, au_san, bk_xi, bk_xi2, bk_qian, bk_san])
    # 提交会话
    db.session.commit()
    app.run(debug=True)