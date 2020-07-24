import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="ZAKIR1234", database="Zakir")
mycursor=mydb.cursor()
mycursor.execute("select * from Student")


# for i in mycursor:
#     print(i)

# result=mycursor.fetchall()
result=mycursor.fetchone()
for j in result:
    print(j)