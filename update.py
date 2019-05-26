import mysql.connector

cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01', user='root', password='ciao@200')
    cursor = conn.cursor()
    upd = "UPDATE employee SET salary = %s WHERE empno = %s"
    upd_data = (51000, 1009)
    cursor.execute(upd, upd_data)
    conn.commit()
    print('update ', cursor.rowcount, "employees")

    query = "SELECT ename, hiredate, salary FROM employee WHERE empno = %s"
    empno = 1009
    cursor.execute(query, (empno, ))
    emp = cursor.fetchone()
    if emp is not None:
        print('name = {}, hiredate = {}, salary = {}'
              .format(emp[0], emp[1], emp[2]))
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




