import mysql.connector

cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01', user='root', password='ciao@200')
    cursor = conn.cursor()
    del1 = "DELETE FROM employee WHERE empno = %s"
    cursor.execute(del1, (1009, ))
    conn.commit()
    print('delete ', cursor.rowcount, "employees")

    query = "SELECT ename, hiredate, salary FROM employee"
    cursor.execute(query)

    for ename, hiredate, salary in cursor:
        print('name = {}, hiredate = {}, salary = {}'
              .format(ename, hiredate, salary))
    print('total ', cursor.rowcount, "employee")

except mysql.connector.Error as err:
    print(err)
finally:
    if cursor:
        cursor.close()
        print('close cursor')
    if conn:
        conn.close()
        print('close conn')




