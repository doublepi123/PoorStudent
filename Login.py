# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QSize(400, 300))
        Dialog.setMaximumSize(QSize(400, 300))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(60, 110, 281, 151))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 60, 16))
        self.textUsername = QLineEdit(self.groupBox)
        self.textUsername.setObjectName(u"textUsername")
        self.textUsername.setGeometry(QRect(100, 40, 113, 21))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 60, 16))
        self.textPassword = QLineEdit(self.groupBox)
        self.textPassword.setObjectName(u"textPassword")
        self.textPassword.setGeometry(QRect(100, 70, 113, 21))
        self.buttonLogin = QPushButton(self.groupBox)
        self.buttonLogin.setObjectName(u"buttonLogin")
        self.buttonLogin.setGeometry(QRect(160, 110, 113, 32))
        self.buttonRegist = QPushButton(self.groupBox)
        self.buttonRegist.setObjectName(u"buttonRegist")
        self.buttonRegist.setGeometry(QRect(10, 110, 113, 32))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 40, 151, 51))
        font = QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.lableError = QLabel(Dialog)
        self.lableError.setObjectName(u"lableError")
        self.lableError.setGeometry(QRect(211, 270, 131, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u767b\u5165", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801", None))
        self.buttonLogin.setText(QCoreApplication.translate("Dialog", u"\u767b\u5165", None))
        self.buttonRegist.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u518c", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u8d2b\u56f0\u751f\u7ba1\u7406\u7cfb\u7edf", None))
        self.lableError.setText("")
    # retranslateUi

