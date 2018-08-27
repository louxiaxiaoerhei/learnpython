from pymysql import *

conn = connect(host='localhost', port=3306, user='root', password='root',database='jing_dong', charset='utf8')
cs = conn.cursor()

row_count = cs.execute("select * from goods;")

for temp in cs.fetchall():
    print(temp)
cs.close()
conn.close()
