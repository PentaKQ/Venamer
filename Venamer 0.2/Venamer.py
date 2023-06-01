from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget
import os
from datetime import date
from datetime import datetime
import time
import io
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic import loadUi
from chitiet_doiten import Ui_Form_doiten
from chitiet_doi import Ui_Form_doi
from chitiet_xoa import Ui_Form_xoa
from chitiet_thay import Ui_Form_thay
from chitiet_them import Ui_Form_them
now = datetime.now()
vitriType = 'dau'
doi_coso = True
doi_gioihan = False
xoa_gioihan = False
them_gioihan = False
thay_gioihan = False



class Ui_Venamer(object):
    def setupUi(self, Venamer):
        Venamer.setObjectName("Venamer")
        Venamer.resize(942, 734)
        Venamer.setWindowIcon(QtGui.QIcon('logo.png'))
        self.centralwidget = QtWidgets.QWidget(Venamer)
        self.centralwidget.setObjectName("centralwidget")
        self.Link = QtWidgets.QLabel(self.centralwidget)
        self.Link.setGeometry(QtCore.QRect(370, 0, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Link.setFont(font)
        self.Link.setObjectName("Link")
        self.duongdan = QtWidgets.QLineEdit(self.centralwidget)
        self.duongdan.setGeometry(QtCore.QRect(90, 50, 771, 21))
        self.duongdan.setInputMethodHints(QtCore.Qt.ImhNone)
        self.duongdan.setInputMask("")
        self.duongdan.setText("")
        self.duongdan.setClearButtonEnabled(True)
        self.duongdan.setObjectName("duongdan")
        self.JobTab = QtWidgets.QTabWidget(self.centralwidget)
        self.JobTab.setGeometry(QtCore.QRect(90, 180, 771, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.JobTab.sizePolicy().hasHeightForWidth())
        self.JobTab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.JobTab.setFont(font)
        self.JobTab.setObjectName("JobTab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_theoso = QtWidgets.QGroupBox(self.tab)
        self.groupBox_theoso.setGeometry(QtCore.QRect(20, 20, 721, 351))
        self.groupBox_theoso.setAutoFillBackground(True)
        self.groupBox_theoso.setObjectName("groupBox_theoso")
        self.label_4 = QtWidgets.QLabel(self.groupBox_theoso)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_theoso)
        self.label_5.setGeometry(QtCore.QRect(290, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_xemtruoc = QtWidgets.QLineEdit(self.groupBox_theoso)
        self.lineEdit_xemtruoc.setGeometry(QtCore.QRect(40, 300, 621, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_xemtruoc.setFont(font)
        self.lineEdit_xemtruoc.setInputMask("")
        self.lineEdit_xemtruoc.setText("")
        self.lineEdit_xemtruoc.setMaxLength(32767)
        self.lineEdit_xemtruoc.setFrame(False)
        self.lineEdit_xemtruoc.setReadOnly(True)
        self.lineEdit_xemtruoc.setClearButtonEnabled(False)
        self.lineEdit_xemtruoc.setObjectName("lineEdit_xemtruoc")
        self.spinBox_doiten = QtWidgets.QSpinBox(self.groupBox_theoso)
        self.spinBox_doiten.setGeometry(QtCore.QRect(120, 40, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.spinBox_doiten.setFont(font)
        self.spinBox_doiten.setWrapping(False)
        self.spinBox_doiten.setFrame(True)
        self.spinBox_doiten.setReadOnly(False)
        self.spinBox_doiten.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_doiten.setKeyboardTracking(False)
        self.spinBox_doiten.setProperty("showGroupSeparator", False)
        self.spinBox_doiten.setMaximum(999999999)
        self.spinBox_doiten.setObjectName("spinBox_doiten")
        self.label_6 = QtWidgets.QLabel(self.groupBox_theoso)
        self.label_6.setGeometry(QtCore.QRect(360, 40, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_doiten_duoi = QtWidgets.QLineEdit(self.groupBox_theoso)
        self.lineEdit_doiten_duoi.setGeometry(QtCore.QRect(470, 40, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_doiten_duoi.setFont(font)
        self.lineEdit_doiten_duoi.setMaxLength(10)
        self.lineEdit_doiten_duoi.setFrame(True)
        self.lineEdit_doiten_duoi.setCursorPosition(0)
        self.lineEdit_doiten_duoi.setClearButtonEnabled(True)
        self.lineEdit_doiten_duoi.setObjectName("lineEdit_doiten_duoi")
        self.line = QtWidgets.QFrame(self.groupBox_theoso)
        self.line.setGeometry(QtCore.QRect(340, 30, 3, 61))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox_theoso)
        self.line_2.setGeometry(QtCore.QRect(0, 90, 731, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit_doiten_ktdt = QtWidgets.QLineEdit(self.groupBox_theoso)
        self.lineEdit_doiten_ktdt.setGeometry(QtCore.QRect(110, 140, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_doiten_ktdt.setFont(font)
        self.lineEdit_doiten_ktdt.setMaxLength(255)
        self.lineEdit_doiten_ktdt.setFrame(True)
        self.lineEdit_doiten_ktdt.setCursorPosition(0)
        self.lineEdit_doiten_ktdt.setClearButtonEnabled(True)
        self.lineEdit_doiten_ktdt.setObjectName("lineEdit_doiten_ktdt")
        self.line_4 = QtWidgets.QFrame(self.groupBox_theoso)
        self.line_4.setGeometry(QtCore.QRect(-10, 240, 741, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton_doiten_xemtruoc = QtWidgets.QPushButton(self.groupBox_theoso)
        self.pushButton_doiten_xemtruoc.setGeometry(QtCore.QRect(280, 260, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_doiten_xemtruoc.setFont(font)
        self.pushButton_doiten_xemtruoc.setObjectName("pushButton_doiten_xemtruoc")
        self.radioButton_coso = QtWidgets.QRadioButton(self.groupBox_theoso)
        self.radioButton_coso.setGeometry(QtCore.QRect(30, 200, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_coso.setFont(font)
        self.radioButton_coso.setChecked(True)
        self.radioButton_coso.setObjectName("radioButton_coso")
        self.radioButton_khongso = QtWidgets.QRadioButton(self.groupBox_theoso)
        self.radioButton_khongso.setGeometry(QtCore.QRect(400, 200, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_khongso.setFont(font)
        self.radioButton_khongso.setObjectName("radioButton_khongso")
        self.line_7 = QtWidgets.QFrame(self.groupBox_theoso)
        self.line_7.setGeometry(QtCore.QRect(720, 230, 741, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.groupBox_theoso)
        self.line_8.setGeometry(QtCore.QRect(-20, 180, 741, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.groupBox_theoso)
        self.line_9.setGeometry(QtCore.QRect(380, 200, 20, 41))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.pushButton_doiten = QtWidgets.QPushButton(self.tab)
        self.pushButton_doiten.setGeometry(QtCore.QRect(280, 390, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_doiten.setFont(font)
        self.pushButton_doiten.setObjectName("pushButton_doiten")
        self.checkBox_doi_gioihan = QtWidgets.QCheckBox(self.tab)
        self.checkBox_doi_gioihan.setGeometry(QtCore.QRect(480, 430, 261, 17))
        self.checkBox_doi_gioihan.setObjectName("checkBox_doi_gioihan")
        self.lineEdit_doi_gioihan = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_doi_gioihan.setEnabled(False)
        self.lineEdit_doi_gioihan.setGeometry(QtCore.QRect(650, 430, 81, 20))
        self.lineEdit_doi_gioihan.setMaxLength(5)
        self.lineEdit_doi_gioihan.setClearButtonEnabled(False)
        self.lineEdit_doi_gioihan.setObjectName("lineEdit_doi_gioihan")
        self.pushButton_doiten_chitiet = QtWidgets.QPushButton(self.tab)
        self.pushButton_doiten_chitiet.setGeometry(QtCore.QRect(20, 420, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_doiten_chitiet.setFont(font)
        self.pushButton_doiten_chitiet.setObjectName("pushButton_doiten_chitiet")
        self.JobTab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_xoa = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_xoa.setGeometry(QtCore.QRect(280, 390, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_xoa.setFont(font)
        self.pushButton_xoa.setObjectName("pushButton_xoa")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 721, 351))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        self.line_5.setGeometry(QtCore.QRect(-30, 120, 771, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(260, 0, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_xoa_xemtruoc = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_xoa_xemtruoc.setGeometry(QtCore.QRect(40, 270, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_xoa_xemtruoc.setFont(font)
        self.lineEdit_xoa_xemtruoc.setText("")
        self.lineEdit_xoa_xemtruoc.setFrame(False)
        self.lineEdit_xoa_xemtruoc.setReadOnly(True)
        self.lineEdit_xoa_xemtruoc.setObjectName("lineEdit_xoa_xemtruoc")
        self.lineEdit_xoa_kitu = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_xoa_kitu.setGeometry(QtCore.QRect(80, 50, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_xoa_kitu.setFont(font)
        self.lineEdit_xoa_kitu.setReadOnly(False)
        self.lineEdit_xoa_kitu.setClearButtonEnabled(True)
        self.lineEdit_xoa_kitu.setObjectName("lineEdit_xoa_kitu")
        self.pushButton_xoa_xemtruoc = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_xoa_xemtruoc.setGeometry(QtCore.QRect(270, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_xoa_xemtruoc.setFont(font)
        self.pushButton_xoa_xemtruoc.setObjectName("pushButton_xoa_xemtruoc")
        self.lineEdit_xoa_gioihan = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_xoa_gioihan.setEnabled(False)
        self.lineEdit_xoa_gioihan.setGeometry(QtCore.QRect(650, 430, 81, 20))
        self.lineEdit_xoa_gioihan.setObjectName("lineEdit_xoa_gioihan")
        self.checkBox_xoa_gioihan = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_xoa_gioihan.setGeometry(QtCore.QRect(480, 430, 261, 17))
        self.checkBox_xoa_gioihan.setObjectName("checkBox_xoa_gioihan")
        self.pushButton_xoa_chitiet = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_xoa_chitiet.setGeometry(QtCore.QRect(20, 420, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_xoa_chitiet.setFont(font)
        self.pushButton_xoa_chitiet.setObjectName("pushButton_xoa_chitiet")
        self.checkBox_xoa_gioihan.raise_()
        self.groupBox.raise_()
        self.pushButton_xoa.raise_()
        self.lineEdit_xoa_gioihan.raise_()
        self.pushButton_xoa_chitiet.raise_()
        self.JobTab.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_them = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_them.setGeometry(QtCore.QRect(280, 390, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_them.setFont(font)
        self.pushButton_them.setObjectName("pushButton_them")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 721, 351))
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_them_kitu = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_them_kitu.setGeometry(QtCore.QRect(80, 50, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_them_kitu.setFont(font)
        self.lineEdit_them_kitu.setMaxLength(255)
        self.lineEdit_them_kitu.setReadOnly(False)
        self.lineEdit_them_kitu.setClearButtonEnabled(True)
        self.lineEdit_them_kitu.setObjectName("lineEdit_them_kitu")
        self.radioButton_them_dau = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_them_dau.setGeometry(QtCore.QRect(160, 130, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_them_dau.setFont(font)
        self.radioButton_them_dau.setChecked(True)
        self.radioButton_them_dau.setAutoRepeatDelay(300)
        self.radioButton_them_dau.setAutoRepeatInterval(100)
        self.radioButton_them_dau.setObjectName("radioButton_them_dau")
        self.radioButton_them_cuoi = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_them_cuoi.setGeometry(QtCore.QRect(250, 130, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_them_cuoi.setFont(font)
        self.radioButton_them_cuoi.setAutoRepeatDelay(300)
        self.radioButton_them_cuoi.setObjectName("radioButton_them_cuoi")
        self.line_6 = QtWidgets.QFrame(self.groupBox_2)
        self.line_6.setGeometry(QtCore.QRect(0, 110, 771, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.lineEdit_them_xemtruoc = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_them_xemtruoc.setGeometry(QtCore.QRect(160, 290, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_them_xemtruoc.setFont(font)
        self.lineEdit_them_xemtruoc.setText("")
        self.lineEdit_them_xemtruoc.setFrame(True)
        self.lineEdit_them_xemtruoc.setReadOnly(True)
        self.lineEdit_them_xemtruoc.setObjectName("lineEdit_them_xemtruoc")
        self.spinBox_them_tuychinh = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_them_tuychinh.setEnabled(False)
        self.spinBox_them_tuychinh.setGeometry(QtCore.QRect(230, 180, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_them_tuychinh.setFont(font)
        self.spinBox_them_tuychinh.setAcceptDrops(False)
        self.spinBox_them_tuychinh.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_them_tuychinh.setObjectName("spinBox_them_tuychinh")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(260, 0, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.radioButton_them_tuychinh = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_them_tuychinh.setGeometry(QtCore.QRect(160, 180, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_them_tuychinh.setFont(font)
        self.radioButton_them_tuychinh.setAutoRepeatDelay(300)
        self.radioButton_them_tuychinh.setObjectName("radioButton_them_tuychinh")
        self.comboBox_them_tuychinh = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_them_tuychinh.setEnabled(False)
        self.comboBox_them_tuychinh.setGeometry(QtCore.QRect(390, 180, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_them_tuychinh.setFont(font)
        self.comboBox_them_tuychinh.setObjectName("comboBox_them_tuychinh")
        self.comboBox_them_tuychinh.addItem("")
        self.comboBox_them_tuychinh.addItem("")
        self.line_12 = QtWidgets.QFrame(self.groupBox_2)
        self.line_12.setGeometry(QtCore.QRect(-10, 260, 771, 16))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.pushButton_them_xemtruoc = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_them_xemtruoc.setGeometry(QtCore.QRect(10, 290, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_them_xemtruoc.setFont(font)
        self.pushButton_them_xemtruoc.setObjectName("pushButton_them_xemtruoc")
        self.radioButton_them_tuychinh.raise_()
        self.label_9.raise_()
        self.lineEdit_them_kitu.raise_()
        self.radioButton_them_dau.raise_()
        self.radioButton_them_cuoi.raise_()
        self.line_6.raise_()
        self.lineEdit_them_xemtruoc.raise_()
        self.spinBox_them_tuychinh.raise_()
        self.label_8.raise_()
        self.comboBox_them_tuychinh.raise_()
        self.line_12.raise_()
        self.pushButton_them_xemtruoc.raise_()
        self.lineEdit_them_gioihan = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_them_gioihan.setEnabled(False)
        self.lineEdit_them_gioihan.setGeometry(QtCore.QRect(650, 430, 81, 20))
        self.lineEdit_them_gioihan.setObjectName("lineEdit_them_gioihan")
        self.checkBox_them_gioihan = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_them_gioihan.setGeometry(QtCore.QRect(480, 430, 261, 17))
        self.checkBox_them_gioihan.setObjectName("checkBox_them_gioihan")
        self.pushButton_them_chitiet = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_them_chitiet.setGeometry(QtCore.QRect(20, 420, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_them_chitiet.setFont(font)
        self.pushButton_them_chitiet.setObjectName("pushButton_them_chitiet")
        self.checkBox_them_gioihan.raise_()
        self.pushButton_them.raise_()
        self.groupBox_2.raise_()
        self.lineEdit_them_gioihan.raise_()
        self.pushButton_them_chitiet.raise_()
        self.JobTab.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 20, 721, 351))
        self.groupBox_4.setAutoFillBackground(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.line_10 = QtWidgets.QFrame(self.groupBox_4)
        self.line_10.setGeometry(QtCore.QRect(-30, 210, 771, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(300, 0, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_thay_xemtruoc = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_thay_xemtruoc.setGeometry(QtCore.QRect(40, 270, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_thay_xemtruoc.setFont(font)
        self.lineEdit_thay_xemtruoc.setText("")
        self.lineEdit_thay_xemtruoc.setFrame(False)
        self.lineEdit_thay_xemtruoc.setReadOnly(True)
        self.lineEdit_thay_xemtruoc.setObjectName("lineEdit_thay_xemtruoc")
        self.lineEdit_thay_thay = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_thay_thay.setGeometry(QtCore.QRect(80, 50, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_thay_thay.setFont(font)
        self.lineEdit_thay_thay.setReadOnly(False)
        self.lineEdit_thay_thay.setClearButtonEnabled(True)
        self.lineEdit_thay_thay.setObjectName("lineEdit_thay_thay")
        self.pushButton_thay_xemtruoc = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_thay_xemtruoc.setGeometry(QtCore.QRect(270, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_thay_xemtruoc.setFont(font)
        self.pushButton_thay_xemtruoc.setObjectName("pushButton_thay_xemtruoc")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(310, 100, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_thay_thanh = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_thay_thanh.setGeometry(QtCore.QRect(80, 160, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_thay_thanh.setFont(font)
        self.lineEdit_thay_thanh.setReadOnly(False)
        self.lineEdit_thay_thanh.setClearButtonEnabled(True)
        self.lineEdit_thay_thanh.setObjectName("lineEdit_thay_thanh")
        self.pushButton_thay = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_thay.setGeometry(QtCore.QRect(280, 390, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_thay.setFont(font)
        self.pushButton_thay.setObjectName("pushButton_thay")
        self.lineEdit_thay_gioihan = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_thay_gioihan.setEnabled(False)
        self.lineEdit_thay_gioihan.setGeometry(QtCore.QRect(650, 430, 81, 20))
        self.lineEdit_thay_gioihan.setObjectName("lineEdit_thay_gioihan")
        self.checkBox_thay_gioihan = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_thay_gioihan.setGeometry(QtCore.QRect(480, 430, 261, 17))
        self.checkBox_thay_gioihan.setObjectName("checkBox_thay_gioihan")
        self.pushButton_thay_chitiet = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_thay_chitiet.setGeometry(QtCore.QRect(20, 420, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_thay_chitiet.setFont(font)
        self.pushButton_thay_chitiet.setObjectName("pushButton_thay_chitiet")
        self.checkBox_thay_gioihan.raise_()
        self.groupBox_4.raise_()
        self.pushButton_thay.raise_()
        self.lineEdit_thay_gioihan.raise_()
        self.pushButton_thay_chitiet.raise_()
        self.JobTab.addTab(self.tab_5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 20, 721, 351))
        self.groupBox_3.setAutoFillBackground(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setGeometry(QtCore.QRect(200, 10, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.lineEdit_doi_doi = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_doi_doi.setGeometry(QtCore.QRect(250, 70, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_doi_doi.setFont(font)
        self.lineEdit_doi_doi.setInputMask("")
        self.lineEdit_doi_doi.setMaxLength(10)
        self.lineEdit_doi_doi.setClearButtonEnabled(True)
        self.lineEdit_doi_doi.setObjectName("lineEdit_doi_doi")
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(180, 140, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.lineEdit_doi_doithanh = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_doi_doithanh.setGeometry(QtCore.QRect(250, 200, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_doi_doithanh.setFont(font)
        self.lineEdit_doi_doithanh.setInputMask("")
        self.lineEdit_doi_doithanh.setMaxLength(10)
        self.lineEdit_doi_doithanh.setClearButtonEnabled(True)
        self.lineEdit_doi_doithanh.setObjectName("lineEdit_doi_doithanh")
        self.lineEdit_doi_xemtruoc = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_doi_xemtruoc.setGeometry(QtCore.QRect(160, 290, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_doi_xemtruoc.setFont(font)
        self.lineEdit_doi_xemtruoc.setText("")
        self.lineEdit_doi_xemtruoc.setFrame(True)
        self.lineEdit_doi_xemtruoc.setReadOnly(True)
        self.lineEdit_doi_xemtruoc.setObjectName("lineEdit_doi_xemtruoc")
        self.line_13 = QtWidgets.QFrame(self.groupBox_3)
        self.line_13.setGeometry(QtCore.QRect(-40, 260, 771, 16))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.pushButton_doi_xemtruoc = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_doi_xemtruoc.setGeometry(QtCore.QRect(10, 290, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_doi_xemtruoc.setFont(font)
        self.pushButton_doi_xemtruoc.setObjectName("pushButton_doi_xemtruoc")
        self.pushButton_doi = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_doi.setGeometry(QtCore.QRect(280, 390, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_doi.setFont(font)
        self.pushButton_doi.setObjectName("pushButton_doi")
        self.pushButton_doi_chitiet = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_doi_chitiet.setGeometry(QtCore.QRect(20, 420, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_doi_chitiet.setFont(font)
        self.pushButton_doi_chitiet.setObjectName("pushButton_doi_chitiet")
        self.JobTab.addTab(self.tab_4, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 90, 501, 71))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 80, 951, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(110, 670, 741, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_lichsu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_lichsu.setGeometry(QtCore.QRect(10, 670, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_lichsu.setFont(font)
        self.pushButton_lichsu.setObjectName("pushButton_lichsu")
        self.pushButton_undo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_undo.setGeometry(QtCore.QRect(860, 670, 75, 23))
        self.pushButton_undo.setObjectName("pushButton_undo")
        self.pushButton_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_file.setGeometry(QtCore.QRect(870, 50, 41, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_file.sizePolicy().hasHeightForWidth())
        self.pushButton_file.setSizePolicy(sizePolicy)
        self.pushButton_file.setObjectName("pushButton_file")
        Venamer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Venamer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Venamer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Venamer)
        self.statusbar.setObjectName("statusbar")
        Venamer.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Venamer)
        self.JobTab.setCurrentIndex(0)
        self.radioButton_them_tuychinh.clicked.connect(self.spinBox_them_tuychinh.update)
        self.radioButton_them_tuychinh.clicked.connect(self.comboBox_them_tuychinh.update)
        self.JobTab.tabBarClicked['int'].connect(self.progressBar.reset)
        QtCore.QMetaObject.connectSlotsByName(Venamer)
        Venamer.setTabOrder(self.duongdan, self.JobTab)
        Venamer.setTabOrder(self.JobTab, self.spinBox_doiten)
        Venamer.setTabOrder(self.spinBox_doiten, self.lineEdit_doiten_duoi)
        Venamer.setTabOrder(self.lineEdit_doiten_duoi, self.lineEdit_doiten_ktdt)
        Venamer.setTabOrder(self.lineEdit_doiten_ktdt, self.radioButton_coso)
        Venamer.setTabOrder(self.radioButton_coso, self.radioButton_khongso)
        Venamer.setTabOrder(self.radioButton_khongso, self.pushButton_doiten_xemtruoc)
        Venamer.setTabOrder(self.pushButton_doiten_xemtruoc, self.pushButton_doiten)
        Venamer.setTabOrder(self.pushButton_doiten, self.pushButton_xoa)
        Venamer.setTabOrder(self.pushButton_xoa, self.lineEdit_xoa_xemtruoc)
        Venamer.setTabOrder(self.lineEdit_xoa_xemtruoc, self.lineEdit_xemtruoc)
        Venamer.setTabOrder(self.lineEdit_xemtruoc, self.lineEdit_xoa_kitu)
        Venamer.setTabOrder(self.lineEdit_xoa_kitu, self.pushButton_xoa_xemtruoc)
        Venamer.setTabOrder(self.pushButton_xoa_xemtruoc, self.pushButton_them)
        Venamer.setTabOrder(self.pushButton_them, self.lineEdit_them_kitu)
        Venamer.setTabOrder(self.lineEdit_them_kitu, self.radioButton_them_dau)
        Venamer.setTabOrder(self.radioButton_them_dau, self.radioButton_them_cuoi)
        Venamer.setTabOrder(self.radioButton_them_cuoi, self.lineEdit_them_xemtruoc)
        Venamer.setTabOrder(self.lineEdit_them_xemtruoc, self.spinBox_them_tuychinh)
        Venamer.setTabOrder(self.spinBox_them_tuychinh, self.radioButton_them_tuychinh)
        Venamer.setTabOrder(self.radioButton_them_tuychinh, self.comboBox_them_tuychinh)
        Venamer.setTabOrder(self.comboBox_them_tuychinh, self.pushButton_them_xemtruoc)
        Venamer.setTabOrder(self.pushButton_them_xemtruoc, self.lineEdit_thay_xemtruoc)
        Venamer.setTabOrder(self.lineEdit_thay_xemtruoc, self.lineEdit_thay_thay)
        Venamer.setTabOrder(self.lineEdit_thay_thay, self.pushButton_thay_xemtruoc)
        Venamer.setTabOrder(self.pushButton_thay_xemtruoc, self.lineEdit_thay_thanh)
        Venamer.setTabOrder(self.lineEdit_thay_thanh, self.pushButton_thay)
        Venamer.setTabOrder(self.pushButton_thay, self.lineEdit_doi_doi)
        Venamer.setTabOrder(self.lineEdit_doi_doi, self.lineEdit_doi_doithanh)
        Venamer.setTabOrder(self.lineEdit_doi_doithanh, self.lineEdit_doi_xemtruoc)
        Venamer.setTabOrder(self.lineEdit_doi_xemtruoc, self.pushButton_doi_xemtruoc)
        Venamer.setTabOrder(self.pushButton_doi_xemtruoc, self.pushButton_doi)


#####################################################################################################################################
        self.pushButton_undo.setEnabled(False)

        self.pushButton_file.clicked.connect(self.run_open_file)

        self.JobTab.tabBarClicked['int'].connect(self.reset_pb)

        self.pushButton_doiten.clicked.connect(self.run_doiten)
        self.pushButton_xoa.clicked.connect(self.run_xoa)
        self.pushButton_them.clicked.connect(self.run_them)
        self.pushButton_doi.clicked.connect(self.run_doiduoi)
        self.pushButton_thay.clicked.connect(self.run_thay)

        self.pushButton_doiten_xemtruoc.clicked.connect(self.run_doiten_xemtruoc)
        self.pushButton_them_xemtruoc.clicked.connect(self.run_them_xemtruoc)
        self.pushButton_xoa_xemtruoc.clicked.connect(self.run_xoa_xemtruoc)
        self.pushButton_doi_xemtruoc.clicked.connect(self.run_doiduoi_xemtruoc)
        self.pushButton_thay_xemtruoc.clicked.connect(self.run_thay_xemtruoc)

        self.pushButton_lichsu.clicked.connect(self.run_lichsu)

        self.pushButton_doiten_chitiet.clicked.connect(self.moCuaSo_doiten)
        self.pushButton_them_chitiet.clicked.connect(self.moCuaSo_them)
        self.pushButton_thay_chitiet.clicked.connect(self.moCuaSo_thay)
        self.pushButton_xoa_chitiet.clicked.connect(self.moCuaSo_xoa)
        self.pushButton_doi_chitiet.clicked.connect(self.moCuaSo_doi)

        self.pushButton_undo.clicked.connect(self.undo)

        self.radioButton_them_dau.clicked.connect(self.them_dau)
        self.radioButton_them_cuoi.clicked.connect(self.them_cuoi)
        self.radioButton_them_tuychinh.clicked.connect(self.them_tuychinh)

        self.checkBox_doi_gioihan.clicked.connect(self.run_doi_gioihan)
        self.checkBox_thay_gioihan.clicked.connect(self.run_thay_gioihan)
        self.checkBox_xoa_gioihan.clicked.connect(self.run_xoa_gioihan)
        self.checkBox_them_gioihan.clicked.connect(self.run_them_gioihan)

        self.radioButton_coso.clicked.connect(self.run_doi_coso)
        self.radioButton_khongso.clicked.connect(self.run_doi_khongso)

        




    def moCuaSo_doiten(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_doiten()
        self.ui.setupUi(self.window)
        startFrom = int(self.spinBox_doiten.text())
        duoiFile = self.lineEdit_doiten_duoi.text()
        specialName = self.lineEdit_doiten_ktdt.text()
        gioihan = self.lineEdit_doi_gioihan.text()
        path = self.duongdan.text()
        
        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác!')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            Ui_Form_doiten().loaddata(self.window, files, doi_coso, doi_gioihan, specialName, duoiFile, startFrom, gioihan)
            self.window.show()

    def moCuaSo_them(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_them()
        self.ui.setupUi(self.window)
        path = self.duongdan.text()
        kituthem = self.lineEdit_them_kitu.text()
        count = 1
        gioihan = self.lineEdit_them_gioihan.text()
        try:
            cach_n = self.spinBox_them_tuychinh.text()
            tinh_tu = self.comboBox_them_tuychinh.currentText()
        except Exception():
            cach_n = '0'
            tinh_tu = ''


        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác!')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            Ui_Form_them().loaddata(self.window, files, kituthem, gioihan, count, vitriType, cach_n, tinh_tu, them_gioihan)
            self.window.show()

    def moCuaSo_thay(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_thay()
        self.ui.setupUi(self.window)
        gioihan = self.lineEdit_thay_gioihan.text()
        thay = self.lineEdit_thay_thay.text()
        thay_thanh = self.lineEdit_thay_thanh.text()
        path = self.duongdan.text()
        count = 1


        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác!')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            Ui_Form_thay().loaddata(self.window, files, gioihan, thay, thay_thanh, count, thay_gioihan)
            self.window.show()

    def moCuaSo_xoa(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_xoa()
        self.ui.setupUi(self.window)
        kitucanxoa = self.lineEdit_xoa_kitu.text()
        path = self.duongdan.text()
        count = 1
        gioihan = self.lineEdit_xoa_gioihan.text()


        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác!')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            Ui_Form_xoa().loaddata(self.window, files, kitucanxoa, gioihan, count, xoa_gioihan)
            self.window.show()

    def moCuaSo_doi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_doi()
        self.ui.setupUi(self.window)
        path = self.duongdan.text()
        doi = kituthem = self.lineEdit_doi_doi.text()
        doithanh = self.lineEdit_doi_doithanh.text()
        count=1


        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác!')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            Ui_Form_doi().loaddata(self.window, files, doi, kituthem, doithanh, count)
            self.window.show()




    def run_open_file(self):
        path = str(QFileDialog.getExistingDirectory(None, "Chọn Đường Dẫn"))
        self.duongdan.setText(path)

    def run_lichsu(self):
        try:
            os.startfile('logs.txt')
        except Exception:
            with io.open('logs.txt','a+', encoding='utf-8') as f:
                pass
            f.close()
            os.startfile('logs.txt')
            
    def undo(self):
        
        path = self.duongdan.text()
        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp muốn hoàn tác không chính xác!')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            self.pushButton_undo.setEnabled(False)
            try:
                count = 1
                with io.open('before.txt','r', encoding='utf-8') as f:
                    before_list = f.readlines()
                f.close()
                with io.open('after.txt','r', encoding='utf-8') as f:
                    after_list = f.readlines()
                f.close()
                for i in range(len(before_list)):
                    self.progressBar.setProperty("value", round(count*100/len(before_list)))
                    QApplication.processEvents()
                    count = count + 1
                    before_list[i] = before_list[i][0:len(before_list[i])-1]
                    after_list[i] = after_list[i][0:len(after_list[i])-1]
                    for file in files:
                        if file == after_list[i]:
                            os.rename(path+'\\'+file,path+'\\'+before_list[i])
                            with io.open('logs.txt','a+', encoding='utf-8') as f:
                                f.(f'{datetime.now()}: Hoàn Tác [{file}] -> ['+before_list[i]+']\n')
                            f.close()
                            break
                done = QMessageBox()
                done.setWindowTitle('Hoàn Tất')
                done.setText(f'Đã hoàn tác thành công {len(files)} tệp')
                done.setIcon(QMessageBox.Information)
                x = done.exec_()

            except Exception:
                msg = QMessageBox()
                msg.setWindowTitle('Lỗi')
                msg.setText('Không tìm thấy dữ liệu để hoàn tác!')
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()

                



    def run_doi_gioihan(self):
        global doi_gioihan
        if doi_gioihan == False:
            self.lineEdit_doi_gioihan.setEnabled(True)
            doi_gioihan = True
        else:
            self.lineEdit_doi_gioihan.setEnabled(False)
            doi_gioihan = False

    def run_xoa_gioihan(self):
        global xoa_gioihan
        if xoa_gioihan == False:
            self.lineEdit_xoa_gioihan.setEnabled(True)
            xoa_gioihan = True
        else:
            self.lineEdit_xoa_gioihan.setEnabled(False)
            xoa_gioihan = False

    def run_them_gioihan(self):
        global them_gioihan
        if them_gioihan == False:
            self.lineEdit_them_gioihan.setEnabled(True)
            them_gioihan = True
        else:
            self.lineEdit_them_gioihan.setEnabled(False)
            them_gioihan = False

    def run_thay_gioihan(self):
        global thay_gioihan
        if thay_gioihan == False:
            self.lineEdit_thay_gioihan.setEnabled(True)
            thay_gioihan = True
        else:
            self.lineEdit_thay_gioihan.setEnabled(False)
            thay_gioihan = False





    def reset_pb(self):
        self.progressBar.setProperty("value", 0)

    def run_doi_coso(self):
        global doi_coso
        doi_coso = True 


    def run_doi_khongso(self):
        global doi_coso
        doi_coso = False



        

    def them_dau(self):
        global vitriType
        vitriType = 'dau'
        self.spinBox_them_tuychinh.setEnabled(False)
        self.comboBox_them_tuychinh.setEnabled(False)
    def them_cuoi(self):
        global vitriType
        vitriType = 'cuoi'
        self.spinBox_them_tuychinh.setEnabled(False)
        self.comboBox_them_tuychinh.setEnabled(False)
    def them_tuychinh(self):
        global vitriType
        vitriType = 'tuychinh'
        self.spinBox_them_tuychinh.setEnabled(True)
        self.comboBox_them_tuychinh.setEnabled(True)


    def run_doiten(self):
        self.pushButton_undo.setEnabled(True)
        path = self.duongdan.text()
        startFrom = int(self.spinBox_doiten.text())
        duoiFile = self.lineEdit_doiten_duoi.text()
        specialName = self.lineEdit_doiten_ktdt.text()
        gioihan = self.lineEdit_doi_gioihan.text()
        with io.open('before.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        with io.open('after.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        i = startFrom
        count = 1
        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác!')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:


            if doi_coso == True:
                try:
                    for file in files:
                        
                        file = str(file)
                        if doi_gioihan == True:
                            if file[len(file)-len(gioihan):len(file)] == str(gioihan):
                                if specialName != '':
                                    with io.open('logs.txt','a+', encoding='utf-8') as f:
                                        f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(specialName)+str(i)+'.'+duoiFile+']\n')
                                    with io.open('before.txt','a+', encoding='utf-8') as f:
                                        f.write(file+'\n')
                                    with io.open('after.txt','a+', encoding='utf-8') as f:
                                        f.write(str(specialName)+str(i)+'.'+duoiFile+'\n')
                                    f.close()
                                    os.rename(path+'\\'+file,path+'\\'+str(specialName)+str(i)+'.'+duoiFile)
                                else:
                                    with io.open('logs.txt','a+', encoding='utf-8') as f:
                                        f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(i)+'.'+duoiFile+']\n')
                                    with io.open('before.txt','a+', encoding='utf-8') as f:
                                        f.write(file+'\n')
                                    with io.open('after.txt','a+', encoding='utf-8') as f:
                                        f.write(str(i)+'.'+duoiFile+'\n')
                                    f.close()
                                    os.rename(path+'\\'+file,path+'\\'+str(i)+'.'+duoiFile)

                        else:
                            if specialName != '':
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(specialName)+str(i)+'.'+duoiFile+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(str(specialName)+str(i)+'.'+duoiFile+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+str(specialName)+str(i)+'.'+duoiFile)
                            else:
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(i)+'.'+duoiFile+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(str(i)+'.'+duoiFile+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+str(i)+'.'+duoiFile)
                        i = i + 1
                        self.progressBar.setProperty("value", round(count*100/len(files)))
                        QApplication.processEvents()
                        count = count + 1
                        
                    f.close()

                    done = QMessageBox()
                    done.setWindowTitle('Hoàn Tất')
                    done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                    done.setIcon(QMessageBox.Information)
                    x = done.exec_()

                    if len(files) == 0:
                        msg = QMessageBox()
                        msg.setWindowTitle('Lỗi')
                        msg.setText('Có lỗi xảy ra, thư mục rỗng')
                        msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                        msg.setIcon(QMessageBox.Warning)
                        x = msg.exec_()
                        self.progressBar.setProperty("value", 0)


                except PermissionError:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra, không có quyền truy cập vào thư mục')
                    msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)

                except Exception:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra, tên các file trước khi đổi và sau khi đổi không được trùng nhau và không được có kí tự đặc biệt!')
                    msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)

            else:
                try:
                    mang_file = ''
                    mang_so = ['0','1','2','3','4','5','6','7','8','9']


                    for file in files:
                        
                        file = str(file)
                        mang_file = ''
                        for i in range(len(file)):
                            if file[i] in mang_so:
                                mang_file = mang_file + str(file[i])

                        if doi_gioihan == True:
                            if file[len(file)-len(gioihan):len(file)] == str(gioihan):

                                if specialName != '':
                                    with io.open('logs.txt','a+', encoding='utf-8') as f:
                                        f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(specialName)+mang_file+'.'+duoiFile+']\n')
                                    with io.open('before.txt','a+', encoding='utf-8') as f:
                                        f.write(file+'\n')
                                    with io.open('after.txt','a+', encoding='utf-8') as f:
                                        f.write(str(specialName)+mang_file+'.'+duoiFile+'\n')
                                    f.close()
                                    os.rename(path+'\\'+file,path+'\\'+str(specialName)+mang_file+'.'+duoiFile)
                                else:
                                    with io.open('logs.txt','a+', encoding='utf-8') as f:
                                        f.write(f'{datetime.now()}: Đổi [{file}] -> ['+mang_file+'.'+duoiFile+']\n')
                                    with io.open('before.txt','a+', encoding='utf-8') as f:
                                        f.write(file+'\n')
                                    with io.open('after.txt','a+', encoding='utf-8') as f:
                                        f.write(mang_file+'.'+duoiFile+'\n')
                                    f.close()
                                    os.rename(path+'\\'+file,path+'\\'+mang_file+'.'+duoiFile)

                        else:
                            if specialName != '':
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(specialName)+mang_file+'.'+duoiFile+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(str(specialName)+mang_file+'.'+duoiFile+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+str(specialName)+mang_file+'.'+duoiFile)
                            else:
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+mang_file+'.'+duoiFile+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(mang_file+'.'+duoiFile+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+mang_file+'.'+duoiFile)

                        self.progressBar.setProperty("value", round(count*100/len(files)))
                        QApplication.processEvents()
                        count = count + 1

                        

                    f.close()
                    done = QMessageBox()
                    done.setWindowTitle('Hoàn Tất')
                    done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                    done.setIcon(QMessageBox.Information)
                    x = done.exec_()                    
                    if len(files) == 0:
                        msg = QMessageBox()
                        msg.setWindowTitle('Lỗi')
                        msg.setText('Có lỗi xảy ra, thư mục rỗng')
                        msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                        msg.setIcon(QMessageBox.Warning)
                        x = msg.exec_()
                        self.progressBar.setProperty("value", 0)

                except Exception:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra liên quan đến tên được đổi, vui lòng thử lại')
                    msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)

    
       
    def run_xoa(self):
        self.pushButton_undo.setEnabled(True)
        with io.open('before.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        with io.open('after.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        kitucanxoa = self.lineEdit_xoa_kitu.text()
        path = self.duongdan.text()
        count = 1
        gioihan = self.lineEdit_xoa_gioihan.text()
        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            try:
                for file in files:
                    file = str(file)
                    
                    if xoa_gioihan == True:
                        if file[len(file)-len(gioihan):len(file)] == str(gioihan):
                            if file.find(str(kitucanxoa)) != -1:
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file.replace(str(kitucanxoa),'')+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(file.replace(str(kitucanxoa),'')+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+file.replace(str(kitucanxoa),''))
                    else:
                        if file.find(str(kitucanxoa)) != -1:
                            with io.open('logs.txt','a+', encoding='utf-8') as f:
                                f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file.replace(str(kitucanxoa),'')+']\n')
                            with io.open('before.txt','a+', encoding='utf-8') as f:
                                f.write(file+'\n')
                            with io.open('after.txt','a+', encoding='utf-8') as f:
                                f.write(file.replace(str(kitucanxoa),'')+'\n')
                            f.close()
                            os.rename(path+'\\'+file,path+'\\'+file.replace(str(kitucanxoa),''))

                    self.progressBar.setProperty("value", round(count*100/len(files)))
                    QApplication.processEvents()
                    count = count + 1

                f.close()
                done = QMessageBox()
                done.setWindowTitle('Hoàn Tất')
                done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                done.setIcon(QMessageBox.Information)
                x = done.exec_() 
                if len(files) == 0:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra, thư mục rỗng')
                    msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)
            except Exception:
                msg = QMessageBox()
                msg.setWindowTitle('Lỗi')
                msg.setText('Có lỗi liên quan đến tên tệp sau khi xóa, vui lòng thử lại')
                msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()
                self.progressBar.setProperty("value", 0)



    def run_them(self):
        self.pushButton_undo.setEnabled(True)
        with io.open('before.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        with io.open('after.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        path = self.duongdan.text()
        kituthem = self.lineEdit_them_kitu.text()
        count = 1
        gioihan = self.lineEdit_them_gioihan.text()

        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

        else:
            if vitriType == 'dau':

                try:
                    for file in files:
                        file = str(file)
                        
                        if them_gioihan == True:
                            if file[len(file)-len(gioihan):len(file)] == str(gioihan):
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(kituthem)+file+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(str(kituthem)+file+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+str(kituthem)+file)
                        else:
                            with io.open('logs.txt','a+', encoding='utf-8') as f:
                                f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(kituthem)+file+']\n')
                            with io.open('before.txt','a+', encoding='utf-8',) as f:
                                f.write(file+'\n')
                            with io.open('after.txt','a+', encoding='utf-8') as f:
                                f.write(str(kituthem)+file+'\n')
                            f.close()
                            os.rename(path+'\\'+file,path+'\\'+str(kituthem)+file)

                        self.progressBar.setProperty("value", round(count*100/len(files)))
                        QApplication.processEvents()
                        count = count + 1

                    f.close()
                    done = QMessageBox()
                    done.setWindowTitle('Hoàn Tất')
                    done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                    done.setIcon(QMessageBox.Information)
                    x = done.exec_() 
                    if len(files) == 0:
                        msg = QMessageBox()
                        msg.setWindowTitle('Lỗi')
                        msg.setText('Có lỗi xảy ra, thư mục rỗng')
                        msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                        msg.setIcon(QMessageBox.Warning)
                        x = msg.exec_()
                        self.progressBar.setProperty("value", 0)
                except Exception:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra liên quan đến kí tự được thêm hoặc lỗi không xác định liên quan đến vị trí thêm đầu, vui lòng thử lại')
                    msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)

            elif vitriType == 'cuoi':
                try:
                    for file in files:
                        file = str(file)
                        
                        if them_gioihan == True:
                            if file[len(file)-len(gioihan):len(file)] == str(gioihan):
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file+str(kituthem)+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(file+str(kituthem)+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+file+str(kituthem))
                        else:
                            with io.open('logs.txt','a+', encoding='utf-8') as f:
                                f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file+str(kituthem)+']\n')
                            with io.open('before.txt','a+', encoding='utf-8') as f:
                                f.write(file+'\n')
                            with io.open('after.txt','a+', encoding='utf-8') as f:
                                f.write(file+str(kituthem)+'\n')
                            f.close()
                            os.rename(path+'\\'+file,path+'\\'+file+str(kituthem))

                        self.progressBar.setProperty("value", round(count*100/len(files)))
                        QApplication.processEvents()
                        count = count + 1

                    f.close()
                    done = QMessageBox()
                    done.setWindowTitle('Hoàn Tất')
                    done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                    done.setIcon(QMessageBox.Information)
                    x = done.exec_() 
                    if len(files) == 0:
                        msg = QMessageBox()
                        msg.setWindowTitle('Lỗi')
                        msg.setText('Có lỗi xảy ra, thư mục rỗng')
                        msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                        msg.setIcon(QMessageBox.Warning)
                        x = msg.exec_()
                        self.progressBar.setProperty("value", 0)
                except Exception:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra liên quan đến kí tự được thêm hoặc lỗi không xác định liên quan đến vị trí thêm cuối, vui lòng thử lại')
                    msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)

            else:
                try:
                    cach_n = self.spinBox_them_tuychinh.text()
                    tinh_tu = self.comboBox_them_tuychinh.currentText()
                    if tinh_tu == 'vị trí đầu':
                        for file in files:
                            file = str(file)
                            
                            if them_gioihan == True:
                                if file[len(file)-len(gioihan):len(file)] == str(gioihan):
                                    with io.open('logs.txt','a+', encoding='utf-8') as f:
                                        f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file[0:int(cach_n)]+str(kituthem)+file[int(cach_n):len(file)]+']\n')
                                    with io.open('before.txt','a+', encoding='utf-8') as f:
                                        f.write(file+'\n')
                                    with io.open('after.txt','a+', encoding='utf-8') as f:
                                        f.write(file[0:int(cach_n)]+str(kituthem)+file[int(cach_n):len(file)]+'\n')
                                    f.close()
                                    os.rename(path+'\\'+file,path+'\\'+file[0:int(cach_n)]+str(kituthem)+file[int(cach_n):len(file)])
                            else:
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file[0:int(cach_n)]+str(kituthem)+file[int(cach_n):len(file)]+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(file[0:int(cach_n)]+str(kituthem)+file[int(cach_n):len(file)]+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+file[0:int(cach_n)]+str(kituthem)+file[int(cach_n):len(file)])

                            self.progressBar.setProperty("value", round(count*100/len(files)))
                            QApplication.processEvents()
                            count = count + 1
                        done = QMessageBox()
                        done.setWindowTitle('Hoàn Tất')
                        done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                        done.setIcon(QMessageBox.Information)
                        x = done.exec_() 
                        if len(files) == 0:
                            msg = QMessageBox()
                            msg.setWindowTitle('Lỗi')
                            msg.setText('Có lỗi xảy ra, thư mục rỗng')
                            msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                            msg.setIcon(QMessageBox.Warning)
                            x = msg.exec_()
                            self.progressBar.setProperty("value", 0)
                    else:
                        for file in files:
                            file = str(file)
                            
                            if them_gioihan == True:
                                if file[len(file)-len(gioihan):len(file)] == str(gioihan):
                                    with io.open('logs.txt','a+', encoding='utf-8') as f:
                                        f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file[0:int(len(file))-int(cach_n)]+str(kituthem)+file[int(len(file))-int(cach_n):len(file)]+']\n')
                                    with io.open('before.txt','a+', encoding='utf-8') as f:
                                        f.write(file+'\n')
                                    with io.open('after.txt','a+', encoding='utf-8') as f:
                                        f.write(file[0:int(len(file))-int(cach_n)]+str(kituthem)+file[int(len(file))-int(cach_n):len(file)]+'\n')
                                    f.close()
                                    os.rename(path+'\\'+file,path+'\\'+file[0:int(len(file))-int(cach_n)]+str(kituthem)+file[int(len(file))-int(cach_n):len(file)])
                            else:
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file[0:int(len(file))-int(cach_n)]+str(kituthem)+file[int(len(file))-int(cach_n):len(file)]+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(file[0:int(len(file))-int(cach_n)]+str(kituthem)+file[int(len(file))-int(cach_n):len(file)]+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+file[0:int(len(file))-int(cach_n)]+str(kituthem)+file[int(len(file))-int(cach_n):len(file)])
                            self.progressBar.setProperty("value", round(count*100/len(files)))
                            QApplication.processEvents()
                            count = count + 1
                        f.close()
                        done = QMessageBox()
                        done.setWindowTitle('Hoàn Tất')
                        done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                        done.setIcon(QMessageBox.Information)
                        x = done.exec_() 
                        if len(files) == 0:
                            msg = QMessageBox()
                            msg.setWindowTitle('Lỗi')
                            msg.setText('Có lỗi xảy ra, thư mục rỗng')
                            msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                            msg.setIcon(QMessageBox.Warning)
                            x = msg.exec_()
                            self.progressBar.setProperty("value", 0)
                except Exception:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra liên quan đến kí tự được thêm hoặc lỗi không xác định liên quan đến vị trí thêm tùy chỉnh, vui lòng thử lại')
                    msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)


        

    def run_doiduoi(self):
        self.pushButton_undo.setEnabled(True)
        with io.open('before.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        with io.open('after.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        path = self.duongdan.text()
        doi = kituthem = self.lineEdit_doi_doi.text()
        doithanh = self.lineEdit_doi_doithanh.text()
        count=1

        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

        else:
            if doi == '' and doithanh == '':

                msg = QMessageBox()
                msg.setWindowTitle('Lỗi')
                msg.setText('Không thể để trống cả 2 ô!')
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
            else:

                try:

                    for file in files:
                        
                        file = str(file)
                        if file[len(file)-len(doi):len(file)] == str(doi):
                            
                            if doi != '':
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file[0:int(len(file))-int(len(doi))]+doithanh+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(file[0:int(len(file))-int(len(doi))]+doithanh+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+file[0:int(len(file))-int(len(doi))]+doithanh)
                            else:
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file[0:int(len(file))-int(len(doi))]+'.'+doithanh+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(file[0:int(len(file))-int(len(doi))]+'.'+doithanh+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+file[0:int(len(file))-int(len(doi))]+'.'+doithanh)
                        self.progressBar.setProperty("value", round(count*100/len(files)))
                        QApplication.processEvents()
                        count = count + 1
                    f.close()
                    done = QMessageBox()
                    done.setWindowTitle('Hoàn Tất')
                    done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                    done.setIcon(QMessageBox.Information)
                    x = done.exec_() 
                    if len(files) == 0:
                        msg = QMessageBox()
                        msg.setWindowTitle('Lỗi')
                        msg.setText('Có lỗi xảy ra, thư mục rỗng')
                        msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                        msg.setIcon(QMessageBox.Warning)
                        x = msg.exec_()
                        self.progressBar.setProperty("value", 0)
                except Exception:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra liên quan đến cách đặt phần mở rộng, vui lòng thử lại')
                    msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)

    def run_thay(self):
        self.pushButton_undo.setEnabled(True)
        with io.open('before.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        with io.open('after.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        gioihan = self.lineEdit_thay_gioihan.text()
        thay = self.lineEdit_thay_thay.text()
        thay_thanh = self.lineEdit_thay_thanh.text()
        path = self.duongdan.text()
        count = 1

        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

        else:

            if thay != '':

                try:
                    for file in files:
                        file = str(file)
                        if thay_gioihan == True:
                            if file[len(file)-len(gioihan):len(file)] == str(gioihan):
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file.replace(str(thay),str(thay_thanh))+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(file.replace(str(thay),str(thay_thanh))+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+file.replace(str(thay),str(thay_thanh)))
                        else:
                            with io.open('logs.txt','a+', encoding='utf-8') as f:
                                f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file.replace(str(thay),str(thay_thanh))+']\n')
                            with io.open('before.txt','a+', encoding='utf-8') as f:
                                f.write(file+'\n')
                            with io.open('after.txt','a+', encoding='utf-8') as f:
                                f.write(file.replace(str(thay),str(thay_thanh))+'\n')
                            f.close()
                            os.rename(path+'\\'+file,path+'\\'+file.replace(str(thay),str(thay_thanh)))
                        self.progressBar.setProperty("value", round(count*100/len(files)))
                        QApplication.processEvents()
                        count = count + 1
                    done = QMessageBox()
                    done.setWindowTitle('Hoàn Tất')
                    done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                    done.setIcon(QMessageBox.Information)
                    x = done.exec_() 
                    if len(files) == 0:
                        msg = QMessageBox()
                        msg.setWindowTitle('Lỗi')
                        msg.setText('Có lỗi xảy ra, thư mục rỗng')
                        msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                        msg.setIcon(QMessageBox.Warning)
                        x = msg.exec_()
                        self.progressBar.setProperty("value", 0)

                except Exception:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra liên quan đến cách đặt tên thay thế, vui lòng thử lại')
                    msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)
            else:
                msg = QMessageBox()
                msg.setWindowTitle('Lỗi')
                msg.setText('Tên thay thế không được để trống!')
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()


    def run_doiten_xemtruoc(self):
        specialName = self.lineEdit_doiten_ktdt.text()
        startFrom = int(self.spinBox_doiten.text())
        duoiFile = self.lineEdit_doiten_duoi.text()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Venamer", "Venamer"))
        if duoiFile == '':
            self.lineEdit_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: " + str(specialName) + str(startFrom) + str(duoiFile)+ ", " + str(specialName) + str(startFrom+1) + str(duoiFile) +", ..."))
        else:
            self.lineEdit_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: " + str(specialName) + str(startFrom)+"." + str(duoiFile)+ ", " + str(specialName) + str(startFrom+1) + "."+ str(duoiFile) +", ..."))


    def run_xoa_xemtruoc(self):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Venamer", "Venamer"))
        kitucanxoa = self.lineEdit_xoa_kitu.text()
        self.lineEdit_xoa_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: "+str(kitucanxoa)+"abcdef.xyz ---> abcdef.xyz"))
       

    def run_them_xemtruoc(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Venamer", "Venamer"))
        kituthem = self.lineEdit_them_kitu.text()
        if vitriType == 'dau':
            self.lineEdit_them_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: abcdef.xyz ---> "+str(kituthem)+"abcdef.xyz"))
        elif vitriType == 'cuoi':
           self.lineEdit_them_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: abcdef.xyz ---> abcdef.xyz"+str(kituthem))) 
        else:
            self.lineEdit_them_xemtruoc.setPlaceholderText(_translate("Venamer", "Không có bản xem trước")) 

        

    def run_doiduoi_xemtruoc(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Venamer", "Venamer"))
        doi = kituthem = self.lineEdit_doi_doi.text()
        doithanh = self.lineEdit_doi_doithanh.text()
        if doi != '' and doithanh != '':
            self.lineEdit_doi_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: abcdef."+str(doi)+" ---> abcdef."+str(doithanh)))
        elif doi != '' and doithanh == '':
            self.lineEdit_doi_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: abcdef."+str(doi)+" ---> abcdef"))
        elif doi == '' and doithanh != '':
            self.lineEdit_doi_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: abcdef ---> abcdef."+str(doithanh)))
    def run_thay_xemtruoc(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Venamer", "Venamer"))
        thay = self.lineEdit_thay_thay.text()
        thay_thanh = self.lineEdit_thay_thanh.text()
        self.lineEdit_thay_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: "+str(thay)+"abcdef.xyz ---> "+str(thay_thanh)+"abcdef.xyz"))


###########################################################################################################################################


    def retranslateUi(self, Venamer):
        _translate = QtCore.QCoreApplication.translate
        Venamer.setWindowTitle(_translate("Venamer", "Venamer"))
        self.Link.setText(_translate("Venamer", "Đường Dẫn"))
        self.duongdan.setPlaceholderText(_translate("Venamer", "C:\\..."))
        self.groupBox_theoso.setTitle(_translate("Venamer", "Đổi tên theo thứ tự số"))
        self.label_4.setText(_translate("Venamer", "Bắt đầu từ"))
        self.label_5.setText(_translate("Venamer", "Kí tự đặc trưng"))
        self.lineEdit_xemtruoc.setPlaceholderText(_translate("Venamer", "Tệp sẽ có dạng: kitudactrung0.xyz, kitudactrung1.xyz,..."))
        self.label_6.setText(_translate("Venamer", "Đuôi tệp"))
        self.lineEdit_doiten_duoi.setPlaceholderText(_translate("Venamer", "mp3, mp4, png,..."))
        self.lineEdit_doiten_ktdt.setPlaceholderText(_translate("Venamer", "Các kí tự riêng biệt cho các bộ xếp (có thể bỏ qua)"))
        self.pushButton_doiten_xemtruoc.setText(_translate("Venamer", "Xem trước"))
        self.radioButton_coso.setText(_translate("Venamer", "Các file không có sẵn số thứ tự"))
        self.radioButton_khongso.setText(_translate("Venamer", "Các file đã có sẵn số thứ tự"))
        self.pushButton_doiten.setText(_translate("Venamer", "Bắt Đầu"))
        self.checkBox_doi_gioihan.setText(_translate("Venamer", "Chỉ giới hạn những tệp có đuôi"))
        self.pushButton_doiten_chitiet.setText(_translate("Venamer", "Xem Chi Tiết"))
        self.JobTab.setTabText(self.JobTab.indexOf(self.tab), _translate("Venamer", "Đổi tên tệp theo thứ tự"))
        self.pushButton_xoa.setText(_translate("Venamer", "Bắt Đầu"))
        self.groupBox.setTitle(_translate("Venamer", "Xóa kí tự"))
        self.label_2.setText(_translate("Venamer", "Kí tự muốn xóa"))
        self.lineEdit_xoa_xemtruoc.setPlaceholderText(_translate("Venamer", "Tệp sẽ có dạng: OOOabcdef.xyz ---> abcdef.xyz"))
        self.lineEdit_xoa_kitu.setPlaceholderText(_translate("Venamer", "Nhập những kí tự cần xóa trong tên tệp"))
        self.pushButton_xoa_xemtruoc.setText(_translate("Venamer", "Xem trước"))
        self.checkBox_xoa_gioihan.setText(_translate("Venamer", "Chỉ giới hạn những tệp có đuôi"))
        self.pushButton_xoa_chitiet.setText(_translate("Venamer", "Xem Chi Tiết"))
        self.JobTab.setTabText(self.JobTab.indexOf(self.tab_2), _translate("Venamer", "Xóa kí tự đặc trưng của tệp"))
        self.pushButton_them.setText(_translate("Venamer", "Bắt Đầu"))
        self.groupBox_2.setTitle(_translate("Venamer", "Thêm kí tự"))
        self.label_9.setText(_translate("Venamer", "Vị Trí Thêm"))
        self.lineEdit_them_kitu.setPlaceholderText(_translate("Venamer", "Nhập những kí tự cần thêm trong tên tệp"))
        self.radioButton_them_dau.setText(_translate("Venamer", "Đầu"))
        self.radioButton_them_cuoi.setText(_translate("Venamer", "Cuối"))
        self.lineEdit_them_xemtruoc.setPlaceholderText(_translate("Venamer", "Tệp sẽ có dạng: abcdef.xyz ---> OOOabcdef.xyz"))
        self.label_8.setText(_translate("Venamer", "Kí tự muốn thêm"))
        self.radioButton_them_tuychinh.setText(_translate("Venamer", "Cách       kí tự tính từ"))
        self.comboBox_them_tuychinh.setItemText(0, _translate("Venamer", "vị trí đầu"))
        self.comboBox_them_tuychinh.setItemText(1, _translate("Venamer", "vị trí cuối"))
        self.pushButton_them_xemtruoc.setText(_translate("Venamer", "Xem trước"))
        self.checkBox_them_gioihan.setText(_translate("Venamer", "Chỉ giới hạn những tệp có đuôi"))
        self.pushButton_them_chitiet.setText(_translate("Venamer", "Xem Chi Tiết"))
        self.JobTab.setTabText(self.JobTab.indexOf(self.tab_3), _translate("Venamer", "Thêm kí tự đặc trưng cho tệp"))
        self.groupBox_4.setTitle(_translate("Venamer", "Thay thế kí tự"))
        self.label_3.setText(_translate("Venamer", "Thay thế"))
        self.lineEdit_thay_xemtruoc.setPlaceholderText(_translate("Venamer", "Tệp sẽ có dạng: OOOabcdef.xyz ---> XXXabcdef.xyz"))
        self.lineEdit_thay_thay.setPlaceholderText(_translate("Venamer", "Nhập những kí tự cần thay trong tên tệp"))
        self.pushButton_thay_xemtruoc.setText(_translate("Venamer", "Xem trước"))
        self.label_7.setText(_translate("Venamer", "Thành"))
        self.lineEdit_thay_thanh.setPlaceholderText(_translate("Venamer", "Nhập những kí tự muốn thay thành trong tên tệp"))
        self.pushButton_thay.setText(_translate("Venamer", "Bắt Đầu"))
        self.checkBox_thay_gioihan.setText(_translate("Venamer", "Chỉ giới hạn những tệp có đuôi"))
        self.pushButton_thay_chitiet.setText(_translate("Venamer", "Xem Chi Tiết"))
        self.JobTab.setTabText(self.JobTab.indexOf(self.tab_5), _translate("Venamer", "Thay thế kí tự đặc trưng của tệp"))
        self.groupBox_3.setTitle(_translate("Venamer", "Đổi đuôi tệp"))
        self.label_19.setText(_translate("Venamer", "Đổi những tệp có đuôi"))
        self.lineEdit_doi_doi.setPlaceholderText(_translate("Venamer", "mp3, mp4, png,..."))
        self.label_20.setText(_translate("Venamer", "Thành những tệp có đuôi"))
        self.lineEdit_doi_doithanh.setPlaceholderText(_translate("Venamer", "mp3, mp4, png,..."))
        self.lineEdit_doi_xemtruoc.setPlaceholderText(_translate("Venamer", "Tệp sẽ có dạng: abcdef.xyz ---> abcdef.XYZ"))
        self.pushButton_doi_xemtruoc.setText(_translate("Venamer", "Xem trước"))
        self.pushButton_doi.setText(_translate("Venamer", "Bắt Đầu"))
        self.pushButton_doi_chitiet.setText(_translate("Venamer", "Xem Chi Tiết"))
        self.JobTab.setTabText(self.JobTab.indexOf(self.tab_4), _translate("Venamer", "Đổi phần mở rộng"))
        self.label.setText(_translate("Venamer", "Làm việc với tên tệp"))
        self.pushButton_lichsu.setText(_translate("Venamer", "Lịch sử thay đổi"))
        self.pushButton_undo.setText(_translate("Venamer", "Hoàn tác"))
        self.pushButton_file.setText(_translate("Venamer", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Venamer()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())