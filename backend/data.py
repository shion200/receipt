import mysql.connector
import MySQLdb

user = 'shion'
word = 'nekoneko'
mail = 'example@icloud.com'

conn = MySQLdb.connect(
    user = 'root',
    passwd = 'root',
    host = 'localhost',
    charset = 'utf8',
    db = 'userdata'
)

def create_user_table():
    c = conn.cursor()
    sql = """
        CREATE TABLE USERDATA(
            username VARCHAR(20),
            password VARCHAR(20),
            email    VARCHAR(20)
        )
    """
    c.exexute(sql)
    conn.commit()
    c.execute(all)
    for item in c:
        print(item)
    c.close
    
def data_write():
    all = """SELECT DISTINCT * FROM USERDATA"""
    c = conn.cursor()
    sql = ("""INSERT INTO USERDATA
           (username, password, email)
        VALUES
            (%s, %s, %s)
        """)
    data = [(user, word, mail)]
    c.exectemany(sql, data)
    conn.commit()
    c.execute(all)
    for item in c:
        print(item)
    c.close

create_user_table()


