import mysql.connector
from mysql.connector import errorcode

conn = None
try:
    conn = mysql.connector.connect(database='db01', user='root', password='')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('user or password error !!!')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database doesn't existed !!!")
    else:
        print(err)
finally:
    if conn:
        print('database is closed')
        conn.close()