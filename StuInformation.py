# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StuInformation.ui'
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
        Dialog.resize(1065, 312)
        self.tableView = QTableView(Dialog)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 70, 1031, 171))
        self.saveAndExit = QPushButton(Dialog)
        self.saveAndExit.setObjectName(u"saveAndExit")
        self.saveAndExit.setGeometry(QRect(940, 260, 93, 28))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.saveAndExit.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u5e76\u9000\u51fa", None))
    # retranslateUi

