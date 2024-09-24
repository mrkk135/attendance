import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QPushButton
from copy_path import *

class FileDialogExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.openButton = QPushButton("Open File", self)
        self.openButton.clicked.connect(self.showDialog)
        layout.addWidget(self.openButton)

        self.setLayout(layout)
        self.setWindowTitle('Import file')
        self.setGeometry(300, 300, 300, 200)

    def showDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            path(fileName)
            path_writer()
            


def run():
    app = QApplication(sys.argv)
    ex = FileDialogExample()
    ex.show()
    sys.exit(app.exec_())

run()