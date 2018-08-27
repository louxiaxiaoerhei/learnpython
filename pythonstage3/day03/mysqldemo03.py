from pymysql import *


class Jd(object):
    def __init__(self):
        super().__init__()
        self.conn = connect(host='localhost', port=3306, user='root', password='root', database='jing_dong',
                            charset='utf8')
        self.cs = self.conn.cursor()

    def show_goods(self):
        self.cs.execute("select * from goods")
        for temp in self.cs.fetchall():
            print(temp)

    @staticmethod
    def show_menu():
        print("-" * 10)

    def run(self):
        self.show_menu()
        self.show_goods()
        input()

    def __del__(self):
        self.cs.close()
        self.conn.close()


if __name__ == '__main__':
    jd = Jd()
    jd.run()
