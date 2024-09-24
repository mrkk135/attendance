from main import livecamp
from gui.theme import *
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class site:

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

