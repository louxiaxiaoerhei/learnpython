# 调用函数的时候 传入 名字 年龄
# 例如: 老王 30
# 通过函数内部进行数据处理
# 你的名字叫做老王
# 你的年龄为30岁
# 把新的数据返回给函数调用者
def deal_info(name, age):
    new_name = "你的名字叫做" + name
    new_age = "你的年龄为%d岁" % age
    # 如果一个函数返回多个数据的方式
    # 只需要把多个数据使用逗号隔开即可 就是一个元组类型
    return new_name, new_age

ret = deal_info("老王", 30)
print(type(ret))
print(ret[0])
print(ret[1])