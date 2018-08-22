
# 古法师傅类
# 继承:单继承
class Master(object):
    pass

# 现代师傅类
# 继承:单继承
class School(object):
    pass

# 徒弟类
# 继承:多继承
class Prentice(Master, School):
    pass

# 徒弟徒弟类
# 继承: 单继承 -> 多层继承
class PrenticePrentice(Prentice):
    pass