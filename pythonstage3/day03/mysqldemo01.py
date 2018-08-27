import pymysql


# 创建和数据库服务器的连接 服务器地址　　　端口　　　　用户名　　　　　密码  数据库名 通信使用字符和数据库字符集一致
conn = pymysql.connect(host='localhost', port=3306, user='root', password='root',database='jing_dong', charset='utf8')

# 获取游标
cursor = conn.cursor()

# 执行ＳＱＬ语句 返回值就是ＳＱＬ语句在执行过程中影响的行数
sql = """select * from goods;"""

row_count = cursor.execute(sql)
print("ＳＱＬ语句执行影响的行数%d" % row_count)

# 取出结果集中一行  返回的结果是一行　(1, '妲己', 2)
# print(cursor.fetchone())

# 取出结果集中的所有数据　　返回　((一行数据),(),())
# ((1, '妲己', 2), (2, '李白', 1), (3, '程咬金', 3), (4, '亚瑟', 5), (5, '荆轲', 99))
for line in cursor.fetchall():
    print("  ".join([str(line[i]) for i in range(len(line))]))

# 关闭游标
cursor.close()

# 关闭连接
conn.close()

