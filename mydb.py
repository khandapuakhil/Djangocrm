import mysql.connector
dataBbase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Akhil@2002',


)
#prepare.a.cursor.object
cursorObject = 'dataBase'.cursor()
#create.a.database
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")