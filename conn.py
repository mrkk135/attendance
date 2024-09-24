import mysql.connector

def database():
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2022",
                database= "face"    
                )
        return mydb

def import_name():
    data = database()
    name = []
    cur = data.cursor()
    cur.execute("SELECT * FROM student ;")
    result = cur.fetchall()
    for j in range(1):
        for i in result:
            name.append([*i])

    return name
