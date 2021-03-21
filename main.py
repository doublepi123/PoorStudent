import sys
import os
import hashlib
from functools import partial
from PySide2.QtSql import *
from PySide2.QtWidgets import *
from PySide2.QtCore import QObject, SIGNAL

import Login
from PySide2.QtWidgets import (QApplication, QMainWindow, QDialog, QAction)

db = QSqlDatabase.addDatabase('QSQLITE')
login_dialog = Login.Ui_Dialog()


def loginSystem():
    global login_dialog
    connectdb()
    username = login_dialog.textUsername.text()
    password = login_dialog.textPassword.text()
    h = hashlib.sha256()
    h.update(bytes(password, encoding='utf-8'))
    pwd = h.hexdigest()
    model = QSqlQueryModel()
    print(type(model.setQuery('SELECT * FROM USER WHERE USERNAME = ' + username)))


# 连接数据库
def connectdb():
    global db
    db.setDatabaseName('student.db')
    db.open()


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

    view = QSqlQueryModel()

    app.exec_()


if __name__ == '__main__':
    main()
