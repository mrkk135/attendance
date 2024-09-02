from main import livecamp
import mysql.connector

def home(Form):
    Form.close()
    livecamp()

def login():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2022",
    database= "face"    
    )
    
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM login_detail;")
    myresult = cursor.fetchall()

    for x in myresult:
        print(x )
