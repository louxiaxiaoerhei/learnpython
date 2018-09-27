from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置数据库的链接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/python14'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 需求：实现一对多的模型定义
# 角色(一方，管理员和普通用户)和用户(多方)
# 模型类必须继承db.Model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    info = db.Column(db.String(32),unique=True)
    # 一对多映射：一方定义关系，多方定义外键
    user = db.relationship('User',backref='role')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    email = db.Column(db.String(32),unique=True)
    pswd = db.Column(db.String(32))
    # 定义外键
    user = db.Column(db.Integer,db.ForeignKey('roles.id'))


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()

    app.run(debug=True)