import sys
import os
import hashlib
from functools import partial
from PySide2.QtSql import *
from PySide2.QtWidgets import *
from PySide2.QtCore import QObject, SIGNAL

import Login
import Regist
from PySide2.QtWidgets import (QApplication, QMainWindow, QDialog, QAction)

db = QSqlDatabase.addDatabase('QSQLITE')
login_dialog = Login.Ui_Dialog()
regist_dialog = Regist.Ui_Dialog()


def encodePWD(password):
    h = hashlib.sha256()
    h.update(bytes(password, encoding='utf-8'))
    return h.hexdigest()


def loginSystem():
    global login_dialog
    connectdb()
    username = login_dialog.textUsername.text()
    password = login_dialog.textPassword.text()
    pwd = encodePWD(password)
    model = QSqlQueryModel()
    model.setQuery("SELECT * FROM USER WHERE USERNAME = '" + username + "'")
    if model.lastError().isValid():
        login_dialog.lableError.setText("用户名不存在")
    else:
        realPwd = model.data(model.index(0, 1))
        if realPwd == pwd:
            print(pwd, realPwd)
        else:
            login_dialog.lableError.setText("用户名或密码错误")


# 连接数据库
def connectdb():
    global db
    db.setDatabaseName('student.db')
    db.open()


def registAUser():
    model = QSqlQueryModel()
    username = regist_dialog.testUsername.text()
    password = regist_dialog.testPassword.text()
    password1 = regist_dialog.textPassword1.text()
    if password1 != password:
        regist_dialog.labelError.setText("两次输入密码不一致！")
        return
    model.setQuery("SELECT * FROM USER WHERE USERNAME = '" + username + "'")
    if model.lastError().isValid():
        pwd = encodePWD(password)
        model.setQuery("INSERT INTO USER VALUES ("+"'"+username+"',"+"'"+pwd+"',"+"1)")
        regist_dialog.labelError.setText("注册成功")



def registSystem():
    global regist_dialog
    app = QApplication()
    main = Regist.QDialog()
    regist_dialog.setupUi(main)
    main.show()
    regist_dialog.buttonSubmit.clicked.connect(registAUser)
    app.exec_()


def main():
    # MACOS BIGSUR兼容
    os.environ['QT_MAC_WANTS_LAYER'] = '1'

    # QT环境初始化
    app = QApplication()
    main = QDialog()

    login_dialog.setupUi(main)
    main.show()
    # 执行登入操作
    login_dialog.buttonLogin.clicked.connect(loginSystem)
    login_dialog.textPassword.setEchoMode(QLineEdit.Password)
    login_dialog.buttonRegist.clicked.connect(registSystem)
    view = QSqlQueryModel()

    app.exec_()


if __name__ == '__main__':
    main()
