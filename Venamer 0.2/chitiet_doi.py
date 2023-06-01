from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Ui_Form_doi(QDialog):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 750)

        Form.setWindowIcon(QtGui.QIcon('logo.png'))
        
    def loaddata(self, Form, files, doi, kituthem, doithanh, count):
        row = 0
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 800, 751))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(files))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(0,400)
        self.tableWidget.setColumnWidth(1,400)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        for file in files:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(file))

            if file[len(file)-len(doi):len(file)] == str(doi):
                if doi != '':
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(file[0:int(len(file))-int(len(doi))]+doithanh))
                else:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(file[0:int(len(file))-int(len(doi))]+'.'+doithanh))
            else:
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(file))



            row = row + 1



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Xem Trước"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Trước"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Sau"))
