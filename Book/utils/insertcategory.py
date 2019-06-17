from pymysql import *

def add_test_users():
    usersvalues = [("文学"),("儿童文学"),("国外小说"),("艺术"),("计算机"),("教育"),("小说"),("计算机"),("漫画")]
    conn = connect(host="localhost", port=3306, user="root", password='123456', database='book', charset='utf8')
    cs = conn.cursor()  # 获取光标
    # 注意这里使用的是executemany而不是execute，下边有对executemany的详细说明
    # sql = "insert into book_list_bookcategory(id,category) values(%d, %s)"
    cs.executemany('INSERT INTO book_list_bookcategory (category) VALUES( %s )', usersvalues)
    conn.commit()
    cs.close()
    conn.close()
    print('OK')
add_test_users()
