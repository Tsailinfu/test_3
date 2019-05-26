import mysql.connector

cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01', user='root', password='ciao@200')
    cursor = conn.cursor()
    ins = "INSERT INTO employee VALUES(%s, %s, %s, %s, %s, %s)"
    ins_data = (1009, '張子人', '2019/05/20', 50000, 100, 'engineer')
    cursor.execute(ins, ins_data)
    conn.commit()
    print('insert ', cursor.rowcount, "employees")

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




