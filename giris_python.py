# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/masaüstü/yazılımileilgilihersey/onluk/droncuadam/kodabasla/giris.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 439)
        MainWindow.setStyleSheet("selection-color: rgb(170, 170, 255);\n"
"background-color: rgb(167, 167, 167);\n"
"alternate-background-color: rgb(85, 0, 0);\n"
"selection-background-color: rgb(85, 255, 127);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 641, 441))
        self.scrollArea.setStyleSheet("color: rgb(107, 102, 248);\n"
"selection-color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 639, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.logo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.logo.setGeometry(QtCore.QRect(200, 10, 200, 200))
        self.logo.setMinimumSize(QtCore.QSize(200, 200))
        self.logo.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logo.setFont(font)
        self.logo.setObjectName("logo")
        self.email = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.email.setGeometry(QtCore.QRect(140, 240, 350, 41))
        self.email.setMinimumSize(QtCore.QSize(350, 41))
        self.email.setMaximumSize(QtCore.QSize(350, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setOverwriteMode(False)
        self.email.setObjectName("email")
        self.sifre = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.sifre.setGeometry(QtCore.QRect(140, 300, 350, 41))
        self.sifre.setMinimumSize(QtCore.QSize(350, 41))
        self.sifre.setMaximumSize(QtCore.QSize(350, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sifre.setFont(font)
        self.sifre.setOverwriteMode(False)
        self.sifre.setObjectName("sifre")
        self.girisbuton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.girisbuton.setGeometry(QtCore.QRect(350, 360, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.girisbuton.setFont(font)
        self.girisbuton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(107, 102, 248);")
        self.girisbuton.setObjectName("girisbuton")
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setGeometry(QtCore.QRect(150, 370, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionGiri = QtWidgets.QAction(MainWindow)
        self.actionGiri.setObjectName("actionGiri")
        self.actionHesaplar_Ekle = QtWidgets.QAction(MainWindow)
        self.actionHesaplar_Ekle.setObjectName("actionHesaplar_Ekle")
        self.actionBot_Ba_lar = QtWidgets.QAction(MainWindow)
        self.actionBot_Ba_lar.setObjectName("actionBot_Ba_lar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo.setText(_translate("MainWindow", "LOGO"))
        self.email.setPlaceholderText(_translate("MainWindow", "E-Mail or Username"))
        self.sifre.setPlaceholderText(_translate("MainWindow", "Password"))
        self.girisbuton.setText(_translate("MainWindow", "Login"))
        self.checkBox.setText(_translate("MainWindow", "Remember Me"))
        self.actionGiri.setText(_translate("MainWindow", "Giriş"))
        self.actionHesaplar_Ekle.setText(_translate("MainWindow", "Hesapları Ekle"))
        self.actionBot_Ba_lar.setText(_translate("MainWindow", "Bot Başlat"))

