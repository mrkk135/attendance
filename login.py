from PyQt5 import QtCore, QtGui, QtWidgets
import sys, mysql.connector

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1114, 729)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 30, 1041, 661))
        self.widget.setStyleSheet("QPushButton#pushButton{background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));    color:rgba(255, 255, 255, 210);    border-radius:5px;}QPushButton#pushButton:hover{    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));}QPushButton#pushButton:pressed{    padding-left:5px;    padding-top:5px;    background-color:rgba(150, 123, 111, 255);}QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{    background-color: rgba(0, 0, 0, 0);    color:rgba(85, 98, 112, 255);}QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{    color: rgba(131, 96, 53, 255);}QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{    padding-left:5px;    padding-top:5px;    color:rgba(91, 88, 53, 255);}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(80, 30, 891, 591))
        self.label.setStyleSheet("border-image: url(gui/img/ssr.jpg);border-top-left-radius: 50px;border-bottom-right-radius: 50px;")
        

        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 441, 591))
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0, 80);border-top-left-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(520, 30, 451, 591))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);border-bottom-right-radius: 50px;")
        

        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(590, 100, 171, 40))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")


        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(590, 180, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);border:none;border-bottom:2px solid rgba(46, 82, 101, 200);color:rgba(0, 0, 0, 240);padding-bottom:7px;")
        
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(590, 260, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);border:none;border-bottom:2px solid rgba(46, 82, 101, 200);color:rgba(0, 0, 0, 240);padding-bottom:7px;")
        

        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(640, 370, 190, 40))

        
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(301, 345, 181, 16))
        self.label_5.setStyleSheet("color:rgba(0, 0, 0, 210);")
        self.label_5.setObjectName("label_5")

        
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(140, 70, 331, 511))
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 75);")


        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(160, 110, 271, 40))



        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(80, 30, 441, 591))
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 75);")


        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(160, 110, 271, 40))


        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)


        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(150, 150, 291, 131))


        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255, 255, 255, 170);")
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(150, 230, 271, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_9.setObjectName("label_9")
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.user= self.lineEdit
        self.password = self.lineEdit_2
        self.pushButton.clicked.connect(self.clicked)


    def clicked(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2022",
        database= "face"    
        )

        cur = mydb.cursor()
        cur.execute(f"SELECT t_username , t_passd from login_detail where t_username = '{self.user.text()}';")
        result = cur.fetchall()
        for x in result:
                u = x[0]
                p = x[1]
                if u == self.user.text():
                        if p == self.password.text():
                                import os
                                os.system("C:/Users/kamle/AppData/Local/Microsoft/WindowsApps/python3.11.exe d:/face_project/main_gui.py")


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.pushButton.setText(_translate("Form", "L o g  I n"))
        self.label_7.setText(_translate("Form", "SSR COLLEGE "))
        self.label_8.setText(_translate("Form", "Make The "))
        self.label_9.setText(_translate("Form", "CHANGE"))

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec_())
