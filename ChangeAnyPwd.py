# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChangeAnyPwd.ui'
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
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 90, 361, 201))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 60, 16))
        self.textUsername = QLineEdit(self.groupBox)
        self.textUsername.setObjectName(u"textUsername")
        self.textUsername.setGeometry(QRect(60, 10, 113, 21))
        self.textPassword = QLineEdit(self.groupBox)
        self.textPassword.setObjectName(u"textPassword")
        self.textPassword.setGeometry(QRect(60, 60, 113, 21))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 60, 60, 16))
        self.buttonChange = QPushButton(self.groupBox)
        self.buttonChange.setObjectName(u"buttonChange")
        self.buttonChange.setGeometry(QRect(210, 90, 113, 32))
        self.buttonBack = QPushButton(self.groupBox)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setGeometry(QRect(210, 140, 113, 32))
        self.labelError = QLabel(self.groupBox)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setGeometry(QRect(40, 100, 121, 20))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 20, 191, 51))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u4fee\u6539\u5bc6\u7801", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801", None))
        self.buttonChange.setText(QCoreApplication.translate("Dialog", u"\u4fee\u6539", None))
        self.buttonBack.setText(QCoreApplication.translate("Dialog", u"\u8fd4\u56de", None))
        self.labelError.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:48pt;\">\u4fee\u6539\u5bc6\u7801</span></p></body></html>", None))
    # retranslateUi

