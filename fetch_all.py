import mysql.connector

cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01', user='root', password='')
    cursor = conn.cursor()
    query = "SELECT ename, hiredate, salary FROM employee"
    cursor.execute(query)
    emps = cursor.fetchall()
    print(emps)

    for emp in emps:
        print('name = {}, hiredate = {}, salary = {}' .format(emp[0], emp[1], emp[2]))
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
