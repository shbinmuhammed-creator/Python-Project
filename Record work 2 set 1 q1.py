
import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",password="admin",database="emp1")
mycursor=mydb.cursor()
n=int(input("Enter empno to be searched: "))
q="select * from employee where empno={}".format(n)
mycursor.execute(q)
data=mycursor.fetchone()
if data!=None:
     print("Found")
     print(data)
else:
     print("Not found")

