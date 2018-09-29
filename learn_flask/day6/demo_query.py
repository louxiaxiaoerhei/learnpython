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
    # 如果不指定表名，默认会创建同类名的表名，tb_users/tb_roles;
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    info = db.Column(db.String(32),unique=True)
    # 一对多映射：一方定义关系，多方定义外键
    # 在一对多的关系中，relationship定义在一方
    # 第一个参数表示的是另一方的类名，backref表示的是反向引用；
    # 使用：
    # 等号左边给一方使用，用来实现一对多的查询；
    # backref给多方使用，用来实现多对一的查询；
    user = db.relationship('User',backref='role')

    # 显示对象的可读字符串,__str__
    def __repr__(self):
        return 'role:%s' % self.info

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    email = db.Column(db.String(32),unique=True)
    pswd = db.Column(db.String(32))
    # 定义外键
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'name:%s' % self.name

"""
基本查询：
User.query.filter(User.name=='wang').all()
filter过滤查询，接收的参数，必须使用模型类的类名.字段名，不能使用等值，可以使用==、!=/
User.query.filter_by(name='chen').all()
filter_by过滤查询，接收的参数，只需要使用字段名，只能使用等值；相当于过滤查询中的精确查询。

User.query.order_by(User.id.desc()).all()
order_by查询排序，desc表示降序排序，asc表示升序排序
User.query.filter().paginate(1,2,False)
paginate分页查询的结果为paginate对象:第一个参数表示页数，第二个参数表示每页多少条数据，第三个参数False表示分页异常不报错
paginate.items获取分页后的数据
paginate.pages获取分页后的总页数
paginate.page获取当前页数

"""




@app.route('/')
def index():

    return 'hello world'

if __name__ == '__main__':
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()
    # 添加测试数据
    ro1 = Role(info='admin')
    ro2 = Role(info='user')
    # session：表示的是数据库会话对象，封装了数据库的操作，add、add_all、commit/rollback/delete
    db.session.add_all([ro1, ro2]) # 添加模型类对象给数据库会话对象
    db.session.commit() # 提交数据到数据库中
    us1 = User(name='wang', email='wang@163.com', pswd='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', pswd='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', pswd='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', pswd='456789', role_id=ro1.id)
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()

    app.run(debug=True)