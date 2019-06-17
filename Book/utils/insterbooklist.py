from pymysql import *

def add_test_users():
    usersvalues = [
        ("雅典的胜利：文明的奠基",'安东尼·艾福瑞特',"中信出版社",6,80.20,'static/images/goods/victory.jpg',6)
        ("中华上下五千年", '邵珠磊', "人民邮电出版社", 7, 14.20, 'static/images/goods/5000.jpg', 6)
    ]
    conn = connect(host="localhost", port=3306, user="root", password='123456', database='book', charset='utf8')
    cs = conn.cursor()  # 获取光标
    # 注意这里使用的是executemany而不是execute，下边有对executemany的详细说明
    # sql = "insert into book_list_bookcategory(id,category) values(%d, %s)"
    cs.executemany(
        'INSERT INTO book_list_booklist (name,author,press,num,price,image,category_id) VALUES( %s,%s,%s,%s,%s,%s,%s )',
        usersvalues)
    conn.commit()
    cs.close()
    conn.close()
    print('OK')
add_test_users()