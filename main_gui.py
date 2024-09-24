import sys ,conn ,csv
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets



class MainHome(object):
    def setupUi(self, MainWindow,tname):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1000)
        MainWindow.setStyleSheet("QPushButton{border-radius :20%;color: rgb(255, 255, 255); }QMainWindow{background-color: rgb(255, 255, 255);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setGeometry(QtCore.QRect(0, 0, 1920, 80))
        self.top_bar.setStyleSheet("background-color: rgb(17, 79, 172);")
        self.top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")


        self.idenity = QtWidgets.QFrame(self.top_bar)
        self.idenity.setGeometry(QtCore.QRect(50, 5, 390, 70))
        self.idenity.setStyleSheet("color:#ffffff;")
        self.idenity.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.idenity.setFrameShadow(QtWidgets.QFrame.Raised)
        self.idenity.setObjectName("idenity")

        
        self.profile = QtWidgets.QLabel(self.idenity)
        self.profile.setGeometry(QtCore.QRect(0, 0, 70, 70))
        self.profile.setStyleSheet("border-radius:35%;background-color: rgb(0, 0, 255);")
        self.profile.setText("")
        self.profile.setTextFormat(QtCore.Qt.PlainText)
        self.profile.setPixmap(QtGui.QPixmap("gui/icons/profile.png"))
        self.profile.setScaledContents(True)
        self.profile.setObjectName("profile")


        self.t_name = QtWidgets.QLabel(self.idenity)
        self.t_name.setGeometry(QtCore.QRect(90, 20, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.t_name.setFont(font)
        self.t_name.setObjectName("t_name")


        self.logout_btn = QtWidgets.QPushButton(self.top_bar)
        self.logout_btn.setGeometry(QtCore.QRect(1710, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.logout_btn.setFont(font)
        self.logout_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui/icons/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_btn.setIcon(icon)
        self.logout_btn.setObjectName("logout_btn")



        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(115, 160, 170, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.start_btn.setFont(font)
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn.setStyleSheet("QPushButton{background-color: rgb(56, 255, 62);}QPushButton:hover{background-color: rgb(4, 240, 0);}")
        self.start_btn.setObjectName("start_btn")
        self.start_btn.clicked.connect(self.start)

        self.insert_btn = QtWidgets.QPushButton(self.centralwidget)
        self.insert_btn.setGeometry(QtCore.QRect(300, 160, 170, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.insert_btn.setFont(font)
        self.insert_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.insert_btn.setStyleSheet("QPushButton{background-color: rgb(0, 145, 255);color:#ffffff;}QPushButton:hover{background-color: rgb(1, 98, 255);}")
        self.insert_btn.setObjectName("insert_btn")
        self.insert_btn.clicked.connect(self.insert)


        self.report_btn = QtWidgets.QPushButton(self.centralwidget)
        self.report_btn.setGeometry(QtCore.QRect(490, 160, 170, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.report_btn.setFont(font)
        self.report_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.report_btn.setStyleSheet("QPushButton{background-color: rgb(255, 38, 49);}QPushButton:hover{background-color: rgb(216, 0, 3);}")
        self.report_btn.setObjectName("report_btn")
        

        
        self.table = QtWidgets.QFrame(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(60, 307, 1800, 671))
        self.table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.table.setObjectName("table")


        self.header_table = QtWidgets.QTableWidget(self.table)
        self.header_table.setGeometry(QtCore.QRect(30, 0, 1801, 41))
        self.header_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.header_table.setObjectName("header_table")
        self.header_table.setColumnCount(6)
        self.header_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.header_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.header_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.header_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.header_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.header_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.header_table.setHorizontalHeaderItem(5, item)
        self.header_table.horizontalHeader().setVisible(True)
        self.header_table.horizontalHeader().setDefaultSectionSize(290)
        self.header_table.verticalHeader().setVisible(False)

        self.tableWidget = QtWidgets.QTableWidget(self.table)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 1801, 631))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(80)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(291)

        self.Print_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Print_btn.setGeometry(QtCore.QRect(1770, 250, 93, 28))
        self.Print_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Print_btn.setStyleSheet("QPushButton{background-color: rgb(212, 212, 212);color :#000;}QPushButton:hover{background-color: rgb(181, 181, 181);}")
        self.Print_btn.setObjectName("Print_btn")

        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(1660, 250, 93, 28))
        self.clear_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_btn.setStyleSheet("QPushButton{background-color: rgb(212, 212, 212);color :#000;}QPushButton:hover{background-color: rgb(181, 181, 181);}")
        self.clear_btn.setObjectName("clear_btn")
        self.clear_btn.clicked.connect(self.clear)

        self.refesh = QtWidgets.QPushButton(self.centralwidget)
        self.refesh.setGeometry(QtCore.QRect(1600, 250, 40, 28))
        self.refesh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refesh.setStyleSheet("QPushButton{background-color: rgb(212, 212, 212);color :#000;}QPushButton:hover{background-color: rgb(181, 181, 181);}")
        self.refesh.setText("")
        self.refesh.clicked.connect(self.getdata)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("gui/icons/sync.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refesh.setIcon(icon1)
        self.refesh.setObjectName("Print_btn_2")

        self.retranslateUi(MainWindow,tname)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def getdata(self):        
        mydb = conn.database()
        cur = mydb.cursor()
        
        cur.execute(f"SELECT '' FROM student ;")
        result = cur.fetchall()
                    
        self.tableWidget.setRowCount(0)
        for row_number , row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for col_number , data in enumerate(row_data):
                self.tableWidget.setItem(row_number,col_number,QtWidgets.QTableWidgetItem(str(data)))


        
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        try:   
            with open(f"csv/{current_date}.csv", "r") as file:
                data = list(csv.reader(file, delimiter=","))

                with open(f"csv/{current_date}.csv", "r") as file:
                    data = list(csv.reader(file, delimiter=","))
                student_list =[]

                for i in range(len(data)):
                    student_list.append(data[i][0])

                char_to_remove1 ="['"
                char_to_remove2 ="']"

                new_list = [s.replace(char_to_remove1, '') for s in student_list]
                final_name_list = [s.replace(char_to_remove2, '') for s in new_list]

                
                for i in final_name_list:
                        cur = mydb.cursor()

                        cur.execute(f"SELECT id,s_name, s_surname, mob,class ,bod FROM student WHERE s_name = '{i}' ;")
                        result = cur.fetchall()
                        self.tableWidget.setRowCount(80)
                        for row_number , row_data in enumerate(result):
                            self.tableWidget.insertRow(row_number)
                            for col_number , data in enumerate(row_data):
                                self.tableWidget.setItem(row_number,col_number,QtWidgets.QTableWidgetItem(str(data)))
        except Exception as e :
             print(e)
            
    def start(self):
        from cmd_file import path_livecam
        path_livecam()
    
    def insert(self):
        from cmd_file import path_insert
        path_insert()
    def clear(self):
        import conn
        mydb = conn.database()
        cur = mydb.cursor()
        
        cur.execute(f"SELECT '' FROM student ;")
        result = cur.fetchall()
                    
        self.tableWidget.setRowCount(0)
        for row_number , row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for col_number , data in enumerate(row_data):
                self.tableWidget.setItem(row_number,col_number,QtWidgets.QTableWidgetItem(str(data)))




    def retranslateUi(self, MainWindow,tname):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.t_name.setText(_translate("MainWindow", tname ))
        self.logout_btn.setText(_translate("MainWindow", "Logout"))
        self.start_btn.setText(_translate("MainWindow", "START"))
        self.insert_btn.setText(_translate("MainWindow", "NEW ENTRY"))
        self.report_btn.setText(_translate("MainWindow", "REPORTS"))
        item = self.header_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student ID"))
        item = self.header_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Student Name"))
        item = self.header_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Student Surname"))
        item = self.header_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phone Number"))
        item = self.header_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Class"))
        item = self.header_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Date of Birth"))
        self.Print_btn.setText(_translate("MainWindow", "Print"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))


def run(tname):
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = MainHome()
        ui.setupUi(Form,tname=tname)
        Form.show()
        sys.exit(app.exec_())

run('Admin')