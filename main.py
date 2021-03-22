import sys
import os
import hashlib
from functools import partial
from PySide2.QtSql import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import Login
import Regist
import StuInformation
import Student
from PySide2.QtWidgets import (QApplication, QMainWindow, QDialog, QAction)

db = QSqlDatabase.addDatabase('QSQLITE')
login_dialog = Login.Ui_Dialog()
regist_dialog = Regist.Ui_Dialog()
student_dialog = Student.Ui_Dialog()
window = ''
USER = ''


def encodePWD(password):
    h = hashlib.sha256()
    h.update(bytes(password, encoding='utf-8'))
    return h.hexdigest()


def StuInforEdit():
    global USER
    global window
    window = QDialog()
    stuinfor = StuInformation.Ui_Dialog()
    stuinfor.setupUi(window)
    window.show()
    model = QSqlTableModel()
    view = stuinfor.tableView
    view.setModel(model)
    model.setQuery(QSqlQuery('SELECT STUID,NAME,BIRTHDAY,PEOPLE FROM STUDENT WHERE USERNAME = "' + USER + '"'))
    model.setHeaderData(0, Qt.Horizontal, '学号')
    model.setHeaderData(1, Qt.Horizontal, '姓名')
    model.setHeaderData(2, Qt.Horizontal, '出生日期')
    model.setHeaderData(3, Qt.Horizontal, '家庭人口')

    view.show()


def StudentSystem():
    global student_dialog
    global USER
    global window
    window = QDialog()
    student_dialog.setupUi(window)
    window.show()
    student_dialog.labelUsername.setText(USER + ",您好！")
    student_dialog.buttonEdit.clicked.connect(StuInforEdit)


def loginAUser():
    global login_dialog
    global USER
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
            mod = model.data(model.index(0, 2))
            USER = username
            if mod == 1:
                StudentSystem()
            elif mod == 2:
                pass

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
