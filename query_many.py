import mysql.connector

cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01', user='root', password='ciao@200')
    cursor = conn.cursor()
    query = "SELECT ename, hiredate, salary FROM employee" \
            " WHERE deptno = %s and title = %s"
    deptno= 200
    title = 'engineer'

    cursor.execute(query, (deptno, title))
    print('total ', cursor.rowcount, "employee")
    for ename, hiredate, salary in cursor:
        print('name = {}, hiredate = {}, salary = {}' .format(ename, hiredate, salary))
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
