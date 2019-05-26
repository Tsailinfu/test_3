import mysql.connector
conn = mysql.connector.connect(database='db01', user='root', password='')

conn.close()
# ---------------------------------------------
from mysql.connector import connection
conn = connection.MySQLConnection(database='db01', user='root', password='')

conn.close()
# ---------------------------------------------
import mysql.connector
config = {'database':'db01', 'user':'root', 'password':'ciao@200'}

conn = mysql.connector.connect(**config)
conn.close()
