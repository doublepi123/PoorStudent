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
windows = ''


def encodePWD(password):
    h = hashlib.sha256()
    h.update(bytes(password, encoding='utf-8'))
    return h.hexdigest()


def loginAUser():
    global login_dialog
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
    print(username)
    print("SELECT * FROM USER WHERE USERNAME = '" + username + "'")
    print(model.rowCount())
    if model.rowCount() == 0:
        pwd = encodePWD(password)
        model.setQuery("INSERT INTO USER VALUES (" + "'" + username + "'," + "'" + pwd + "'," + "1)")
        regist_dialog.labelError.setText("注册成功")
    else:
        regist_dialog.labelError.setText("用户名已存在")


def registSystem():
    global regist_dialog
    global window
    window = QDialog()
    regist_dialog.setupUi(window)
    window.show()
    regist_dialog.buttonSubmit.clicked.connect(registAUser)


def loginSystem():
    global window
    global login_dialog
    window = QDialog()
    login_dialog.setupUi(window)
    window.show()
    # 执行登入操作
    login_dialog.buttonLogin.clicked.connect(loginAUser)
    login_dialog.textPassword.setEchoMode(QLineEdit.Password)
    login_dialog.buttonRegist.clicked.connect(registSystem)


def main():
    # MACOS BIGSUR兼容
    os.environ['QT_MAC_WANTS_LAYER'] = '1'
    # QT环境初始化
    connectdb()
    app = QApplication()
    loginSystem()
    app.exec_()


if __name__ == '__main__':
    main()
