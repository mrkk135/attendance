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

def insert_std(id, name , sname, path ,boc ,sclass, mob ):
     insert = database()
     cur = insert.cursor()
     sql = "INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s)"
     val =[id,name,sname,path,boc,sclass,mob]
           
     r =  cur.execute(sql,val)
     insert.commit()   
     return 'okey'

     
