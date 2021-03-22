# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Teacher.ui'
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
        self.buttonUserManager = QPushButton(Dialog)
        self.buttonUserManager.setObjectName(u"buttonUserManager")
        self.buttonUserManager.setGeometry(QRect(40, 40, 113, 32))
        self.buttonCheck = QPushButton(Dialog)
        self.buttonCheck.setObjectName(u"buttonCheck")
        self.buttonCheck.setGeometry(QRect(40, 90, 113, 32))
        self.buttonAnalyze = QPushButton(Dialog)
        self.buttonAnalyze.setObjectName(u"buttonAnalyze")
        self.buttonAnalyze.setGeometry(QRect(40, 140, 141, 32))
        self.changpwd = QPushButton(Dialog)
        self.changpwd.setObjectName(u"changpwd")
        self.changpwd.setGeometry(QRect(220, 40, 113, 32))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6559\u5e08\u7aef", None))
        self.buttonUserManager.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u7ba1\u7406", None))
        self.buttonCheck.setText(QCoreApplication.translate("Dialog", u"\u5ba1\u6838\u5b66\u751f\u6570\u636e", None))
        self.buttonAnalyze.setText(QCoreApplication.translate("Dialog", u"\u67e5\u770b\u603b\u4f53\u6570\u636e\u60c5\u51b5", None))
        self.changpwd.setText(QCoreApplication.translate("Dialog", u"\u4fee\u6539\u5bc6\u7801", None))
    # retranslateUi

