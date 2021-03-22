# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserManager.ui'
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
        Dialog.resize(395, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.tableUser = QTableView(Dialog)
        self.tableUser.setObjectName(u"tableUser")
        self.tableUser.setGeometry(QRect(0, 0, 401, 311))
        sizePolicy.setHeightForWidth(self.tableUser.sizePolicy().hasHeightForWidth())
        self.tableUser.setSizePolicy(sizePolicy)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u7528\u6237\u7ba1\u7406", None))
    # retranslateUi

