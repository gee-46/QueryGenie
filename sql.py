import sqlite3

## Connect ti sqlite 
connection =sqlite3.connect('student.db')

## create a cursor object to insert record, create table, delete table, update table
cursor = connection.cursor()

## create a table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

## insert SOME MORE RECORDS 

cursor.execute("INSERT INTO STUDENT VALUES('JOHN','10TH','A',85)")
cursor.execute("INSERT INTO STUDENT VALUES('AMY','10TH','B',90)")
cursor.execute("INSERT INTO STUDENT VALUES('DAVID','10TH','A',78)")
cursor.execute("INSERT INTO STUDENT VALUES('SARA','10TH','B',92)")
cursor.execute("INSERT INTO STUDENT VALUES('MIKE','10TH','A',80)")

## display all the records
print("The inserted records are:")

data=cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

    ## Close the connection
    connection.commit()
    connection.close
     


