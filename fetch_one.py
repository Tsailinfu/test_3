import mysql.connector

cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01', user='root', password='ciao@200')
    cursor = conn.cursor()
    query = "SELECT ename, hiredate, salary FROM employee " \
            "WHERE empno = %s"
    empno = 1001
    cursor.execute(query, (empno, ))
    emp = cursor.fetchone()
    if emp is not None:
        print(emp)
        print('name = {}, hiredate = {}, salary = {}'.format(emp[0], emp[1], emp[2]))
    else:
        print("no data")
    print("total", cursor.rowcount, "employee")
except mysql.connector.Error as err:
    print(err)
finally:
    if cursor:
        cursor.close()
        print('close cursor')
    if conn:
        conn.close()
        print('close conn')
