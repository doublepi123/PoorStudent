# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Regist.ui'
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
        self.groupBox.setGeometry(QRect(50, 50, 311, 211))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 72, 15))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 72, 15))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 72, 15))
        self.testUsername = QLineEdit(self.groupBox)
        self.testUsername.setObjectName(u"testUsername")
        self.testUsername.setGeometry(QRect(120, 0, 151, 21))
        self.testPassword = QLineEdit(self.groupBox)
        self.testPassword.setObjectName(u"testPassword")
        self.testPassword.setGeometry(QRect(120, 40, 151, 21))
        self.testPassword.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.textPassword1 = QLineEdit(self.groupBox)
        self.textPassword1.setObjectName(u"textPassword1")
        self.textPassword1.setGeometry(QRect(120, 90, 151, 21))
        self.textPassword1.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.buttonSubmit = QPushButton(self.groupBox)
        self.buttonSubmit.setObjectName(u"buttonSubmit")
        self.buttonSubmit.setGeometry(QRect(190, 160, 93, 28))
        self.labelError = QLabel(self.groupBox)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setGeometry(QRect(90, 130, 171, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6ce8\u518c", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4\u5bc6\u7801", None))
        self.buttonSubmit.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u518c", None))
        self.labelError.setText("")
    # retranslateUi

