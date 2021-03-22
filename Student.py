# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Student.ui'
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
        Dialog.resize(305, 301)
        self.labelUsername = QLabel(Dialog)
        self.labelUsername.setObjectName(u"labelUsername")
        self.labelUsername.setGeometry(QRect(10, 10, 151, 16))
        self.buttonEdit = QPushButton(Dialog)
        self.buttonEdit.setObjectName(u"buttonEdit")
        self.buttonEdit.setGeometry(QRect(60, 60, 141, 28))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 200, 141, 28))
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(60, 130, 141, 28))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5b66\u751f\u754c\u9762", None))
        self.labelUsername.setText(QCoreApplication.translate("Dialog", u"Username\uff0c\u4f60\u597d\uff01", None))
        self.buttonEdit.setText(QCoreApplication.translate("Dialog", u"\u586b\u5199\u4e2a\u4eba\u4fe1\u606f", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u67e5\u8be2\u5ba1\u6279\u7ed3\u679c", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u67e5\u770b\u5206\u6790\u6570\u636e", None))
    # retranslateUi

