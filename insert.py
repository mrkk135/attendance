import sys
import pkg.conn as adds
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from copy_path import path_writer



class InsertStudentDetail(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.s_id = QtWidgets.QLabel(self.centralwidget)
        self.s_id.setGeometry(QtCore.QRect(80, 110, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_id.setFont(font)
        self.s_id.setObjectName("s_id")
        
        self.s_name = QtWidgets.QLabel(self.centralwidget)
        self.s_name.setGeometry(QtCore.QRect(80, 160, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_name.setFont(font)
        self.s_name.setObjectName("s_name")
        
        self.s_surname = QtWidgets.QLabel(self.centralwidget)
        self.s_surname.setGeometry(QtCore.QRect(80, 210, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_surname.setFont(font)
        self.s_surname.setObjectName("s_surname")
        
        self.s_class = QtWidgets.QLabel(self.centralwidget)
        self.s_class.setGeometry(QtCore.QRect(79, 260, 194, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_class.setFont(font)
        self.s_class.setObjectName("s_class")
        
        self.insert_id = QtWidgets.QLineEdit(self.centralwidget)
        self.insert_id.setGeometry(QtCore.QRect(310, 110, 250, 30))
        self.insert_id.setObjectName("insert_id")
        
        self.insert_class = QtWidgets.QComboBox(self.centralwidget)
        self.insert_class.setGeometry(QtCore.QRect(310, 260, 250, 30))
        self.insert_class.setObjectName("insert_class")
        self.insert_class.addItem("")
        self.insert_class.addItem("")
        self.insert_class.addItem("")
        self.insert_class.addItem("")
        
        self.insert_name = QtWidgets.QLineEdit(self.centralwidget)
        self.insert_name.setGeometry(QtCore.QRect(310, 160, 250, 30))
        self.insert_name.setObjectName("insert_name")

        
        self.insert_surname = QtWidgets.QLineEdit(self.centralwidget)
        self.insert_surname.setGeometry(QtCore.QRect(310, 210, 250, 30))
        self.insert_surname.setObjectName("insert_surname")
        
        self.s_path = QtWidgets.QLabel(self.centralwidget)
        self.s_path.setGeometry(QtCore.QRect(78, 310, 194, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_path.setFont(font)
        self.s_path.setObjectName("s_path")
        
        self.insert_image = QtWidgets.QPushButton(self.centralwidget)
        self.insert_image.setGeometry(QtCore.QRect(310, 310, 250, 30))
        self.insert_image.setObjectName("insert_image")
        self.insert_image.clicked.connect(self.img_path)

        self.s_path_show = QtWidgets.QLabel(self.centralwidget)
        self.s_path_show.setGeometry(QtCore.QRect(313, 350, 481, 21))
        self.s_path_show.setObjectName("s_path_show")
        
        self.mob = QtWidgets.QLabel(self.centralwidget)
        self.mob.setGeometry(QtCore.QRect(80, 380, 194, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mob.setFont(font)
        self.mob.setObjectName("mob")
        
        self.insert_mob = QtWidgets.QLineEdit(self.centralwidget)
        self.insert_mob.setGeometry(QtCore.QRect(310, 380, 250, 30))
        self.insert_mob.setObjectName("insert_mob")
        self.insert_dob = QtWidgets.QDateEdit(self.centralwidget)
        self.insert_dob.setGeometry(QtCore.QRect(310, 430, 250, 30))
        self.insert_dob.setObjectName("insert_dob")

        
        self.dob = QtWidgets.QLabel(self.centralwidget)
        self.dob.setGeometry(QtCore.QRect(77, 430, 194, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dob.setFont(font)
        self.dob.setObjectName("dob")
        
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(310, 510, 251, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.submit.setFont(font)
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit.setStyleSheet("background-color: rgb(0, 170, 0); color:white;")
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.show)
        self.submit.clicked.connect(self.show_alert)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_alert(self):
        time.sleep(2)
        alert = QMessageBox()
        alert.setWindowTitle("Insert")
        alert.setText("Record Inserted in database")
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()


    def show(self):
        id = self.insert_id.text()
        name = self.insert_name.text()
        surname = self.insert_surname.text()
        mob = self.insert_mob.text()
        dob = self.insert_dob.date()

        s_class = self.insert_class.currentText()
        print(id)
        print(name)
        print(surname)
        print(mob) 
        print(dob.toString("yyyy-MM-dd"))       
        birth = dob.toString("yyyy-MM-dd")       
        path = path_writer()
        print(s_class)
        adds.insert_std(id,name,surname,path,birth,s_class,mob)


    def img_path(self):
        from cmd_file import path_import
        path_import()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.s_id.setText(_translate("MainWindow", "Student ID            :"))
        self.s_name.setText(_translate("MainWindow", "Student Name       :"))
        self.s_surname.setText(_translate("MainWindow", "Student surname   :"))
        self.s_class.setText(_translate("MainWindow", "Class                     :"))
        self.insert_class.setItemText(0, _translate("MainWindow", ""))
        self.insert_class.setItemText(1, _translate("MainWindow", "TY-BBA(CA)"))
        self.insert_class.setItemText(2, _translate("MainWindow", "SY-BBA(CA)"))
        self.insert_class.setItemText(3, _translate("MainWindow", "FY-BBA(CA)"))
        self.s_path.setText(_translate("MainWindow", "Image(for scan)     :"))
        self.insert_image.setText(_translate("MainWindow", "SELECT IMAGE"))
        path = path_writer()
        self.s_path_show.setText(_translate("MainWindow", f"last image : {path}"))
        self.mob.setText(_translate("MainWindow", "Moblie no.             :"))
        self.insert_dob.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.dob.setText(_translate("MainWindow", "Day-of-Birth           :"))
        self.submit.setText(_translate("MainWindow", "Insert"))


def run():
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = InsertStudentDetail()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

run()