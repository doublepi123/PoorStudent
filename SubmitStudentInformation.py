# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SubmitStudentInformation.ui'
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
        Dialog.resize(443, 217)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 150, 391, 51))
        self.buttonCancel = QPushButton(self.groupBox)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setGeometry(QRect(0, 10, 113, 32))
        self.buttonYes = QPushButton(self.groupBox)
        self.buttonYes.setObjectName(u"buttonYes")
        self.buttonYes.setGeometry(QRect(270, 10, 113, 32))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 441, 101))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 120, 61, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u63d0\u4ea4\u786e\u8ba4", None))
        self.groupBox.setTitle("")
        self.buttonCancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        self.buttonYes.setText(QCoreApplication.translate("Dialog", u"\u63d0\u4ea4", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">\u4fe1\u606f\u63d0\u4ea4\u540e\u5c06\u7b49\u5f85\u8001\u5e08\u5ba1\u6838\uff0c</span></p><p><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">\u4e2d\u9014\u4e0d\u53ef\u4fee\u6539\uff0c\u4f60\u786e\u5b9a\u8981\u63d0\u4ea4\u5417\uff1f</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" color:#ff00ff;\">\u63d0\u4ea4\u6210\u529f</span></p></body></html>", None))
    # retranslateUi

