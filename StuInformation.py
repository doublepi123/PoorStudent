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
        Dialog.resize(428, 452)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.saveAndExit = QPushButton(Dialog)
        self.saveAndExit.setObjectName(u"saveAndExit")
        self.saveAndExit.setGeometry(QRect(940, 260, 93, 28))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 90, 431, 361))
        self.textName = QLineEdit(self.groupBox)
        self.textName.setObjectName(u"textName")
        self.textName.setGeometry(QRect(70, 30, 113, 21))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 60, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 60, 16))
        self.textID = QLineEdit(self.groupBox)
        self.textID.setObjectName(u"textID")
        self.textID.setGeometry(QRect(70, 70, 113, 21))
        self.textPeople = QLineEdit(self.groupBox)
        self.textPeople.setObjectName(u"textPeople")
        self.textPeople.setGeometry(QRect(70, 110, 113, 21))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 110, 60, 16))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 150, 60, 16))
        self.textIncome = QLineEdit(self.groupBox)
        self.textIncome.setObjectName(u"textIncome")
        self.textIncome.setGeometry(QRect(70, 150, 113, 21))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 190, 60, 16))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 230, 60, 16))
        self.textCostForFood = QLineEdit(self.groupBox)
        self.textCostForFood.setObjectName(u"textCostForFood")
        self.textCostForFood.setGeometry(QRect(70, 190, 113, 21))
        self.textCostForOther = QLineEdit(self.groupBox)
        self.textCostForOther.setObjectName(u"textCostForOther")
        self.textCostForOther.setGeometry(QRect(70, 230, 113, 21))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 270, 60, 16))
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 310, 60, 16))
        self.buttonSave = QPushButton(self.groupBox)
        self.buttonSave.setObjectName(u"buttonSave")
        self.buttonSave.setGeometry(QRect(300, 280, 111, 51))
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(90, 20, 241, 71))
        self.labelError = QLabel(Dialog)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setGeometry(QRect(240, 330, 171, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5b66\u751f\u4fe1\u606f\u4e0a\u4f20", None))
        self.saveAndExit.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u5e76\u9000\u51fa", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u59d3\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5b66\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5bb6\u5ead\u4eba\u6570", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5bb6\u5ead\u6536\u5165", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u996e\u98df\u6d88\u8d39", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u5176\u4ed6\u6d88\u8d39", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u7279\u6b8a\u60c5\u51b5", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u7a81\u53d1\u4e8b\u4ef6", None))
        self.buttonSave.setText(QCoreApplication.translate("Dialog", u"\u63d0\u4ea4\u5e76\u8fd4\u56de", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:36pt;\">\u5b66\u751f\u4fe1\u606f\u4e0a\u4f20</span></p></body></html>", None))
        self.labelError.setText("")
    # retranslateUi

