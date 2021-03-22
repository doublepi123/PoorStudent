import hashlib
from PySide2.QtSql import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ChangeAnyPwd
import Login
import Regist
import StuInformation
import Student
import SubmitStudentInformation
import Teacher
import UserManager
import os

db = QSqlDatabase.addDatabase('QSQLITE')
# 登入界面
login_dialog = Login.Ui_Dialog()
# 注册界面
regist_dialog = Regist.Ui_Dialog()
# 学生主界面
student_dialog = Student.Ui_Dialog()
# 学生信息修改界面
stuinfor = StuInformation.Ui_Dialog()
# 教师主界面
teacher_dialog = Teacher.Ui_Dialog()
# 修改密码
changeAnyPwd_dialog = ChangeAnyPwd.Ui_Dialog()

stuinforModel = QSqlTableModel()
# 窗口
window = ''
# 当前用户名
USER = ''


# 用于编码密码，便于将密码以sha256的方式存在数据库中
def encodePWD(password):
    h = hashlib.sha256()
    h.update(bytes(password, encoding='utf-8'))
    return h.hexdigest()


# 将学生信息储存，并退出返回至学生主界面
def stuinfoSaveAndExit():
    global stuinfor
    global USER
    sql = "INSERT INTO STUDENT VALUES ('temp','" + stuinfor.textName.text() + "','" + stuinfor.textID.text() + "','" + stuinfor.textPeople.text() + "','" + stuinfor.textIncome.text() + "','" + stuinfor.textCostForFood.text() + "','" + stuinfor.textCostForOther.text() + "')"
    model = QSqlQueryModel()
    model.setQuery("DELETE FROM STUDENT WHERE USERNAME = 'temp'")
    model.setQuery(sql)
    if model.lastError().isValid():
        stuinfor.labelError.setText(
            '<html><head/><body><p><span style=" color:#ff0000;">您输入的信息有误</span></p></body></html>')
        return
    else:
        model.setQuery("DELETE FROM STUDENT WHERE USERNAME = '" + USER + "'")
        model.setQuery(
            "INSERT INTO STUDENT VALUES ('" + USER + "','" + stuinfor.textName.text() + "','" + stuinfor.textID.text() + "','" + stuinfor.textPeople.text() + "','" + stuinfor.textIncome.text() + "','" + stuinfor.textCostForFood.text() + "','" + stuinfor.textCostForOther.text() + "')")
    StudentSystem()


def submitYes():
    global USER
    submit(USER)
    

def submitStudentInformation():
    global window
    window = QDialog()
    sub = SubmitStudentInformation.Ui_Dialog()
    sub.setupUi(window)
    window.show()
    sub.buttonYes.clicked.connect(submitYes)


# 学生信息编辑
def StuInforEdit():
    global USER
    global window
    global stuinfor
    window = QDialog()
    stuinfor.setupUi(window)
    window.show()
    # 将保存按钮和保存并退出的槽函数绑定
    stuinfor.buttonSave.clicked.connect(stuinfoSaveAndExit)
    query = QSqlQueryModel()
    query.setQuery("SELECT * FROM STUDENT WHERE USERNAME = '" + USER + "'")
    # 将数据库中的学生信息导入至学生信息表
    if query.columnCount() > 0:
        stuinfor.textID.setText(query.data(query.index(0, 2)))
        stuinfor.textName.setText(query.data(query.index(0, 1)))
        stuinfor.textPeople.setText(str(query.data(query.index(0, 3))))
        stuinfor.textIncome.setText(str(query.data(query.index(0, 4))))
        stuinfor.textCostForFood.setText(str(query.data(query.index(0, 5))))
        stuinfor.textCostForOther.setText(str(query.data(query.index(0, 6))))


# 启动学生信息系统
def StudentSystem():
    global student_dialog
    global USER
    global window
    window = QDialog()
    student_dialog.setupUi(window)
    window.show()
    # 显示欢迎词
    student_dialog.labelUsername.setText(USER + ",您好！")
    # 将信号和槽函数绑定
    student_dialog.buttonEdit.clicked.connect(StuInforEdit)
    student_dialog.buttonSubmit.clicked.connect(submitStudentInformation)


# 用户管理系统
def usermanager():
    global window
    window = QDialog()
    userMgr = UserManager.Ui_Dialog()
    userMgr.setupUi(window)
    view = userMgr.tableUser
    model = QSqlTableModel()
    view.setModel(model)
    model.setTable('USER')
    model.select()
    model.setHeaderData(0, Qt.Horizontal, '用户名')
    model.setHeaderData(1, Qt.Horizontal, '密码')
    model.setHeaderData(2, Qt.Horizontal, '用户权限')
    window.show()


# 启动教师信息系统
def teacherSystem():
    global teacher_dialog
    global window
    window = QDialog()
    teacher_dialog.setupUi(window)
    window.show()
    teacher_dialog.buttonUserManager.clicked.connect(usermanager)
    teacher_dialog.changpwd.clicked.connect(changeAnyPwd)


def changeapwd():
    global changeAnyPwd_dialog
    username = changeAnyPwd_dialog.textUsername.text()
    password = changeAnyPwd_dialog.textPassword.text()
    model = QSqlQueryModel()
    model.setQuery("SELECT * FROM USER WHERE USERNAME = '" + username + "'")
    # print("SELECT * FROM USER WHERE USERNAME = '" + username + "'")
    if model.rowCount() > 0:
        pwd = encodePWD(password)
        model.setQuery('UPDATE USER SET PASSWORD = "' + pwd + '" WHERE USERNAME = "' + username + '"')
        # print('UPDATE USER SET PASSWORD = "' + pwd + '" WHERE USERNAME = "' + username + '"')
        changeAnyPwd_dialog.labelError.setText('密码修改成功')
    else:
        print("here")
        changeAnyPwd_dialog.labelError.setText('用户名不存在')


def changeAnyPwd():
    global window
    global changeAnyPwd_dialog
    window = QDialog()
    changeAnyPwd_dialog.setupUi(window)
    window.show()
    changeAnyPwd_dialog.buttonChange.clicked.connect(changeapwd)
    changeAnyPwd_dialog.buttonBack.clicked.connect(teacherSystem)


# 尝试登入账户
def loginAUser():
    global login_dialog
    global USER
    # 获取用户名及密码
    username = login_dialog.textUsername.text()
    password = login_dialog.textPassword.text()
    # 计算密码的hash
    pwd = encodePWD(password)
    model = QSqlQueryModel()
    # 获取数据库中的密码并进行比对
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
                teacherSystem()

        else:
            login_dialog.lableError.setText("用户名或密码错误")


# 连接数据库
def connectdb():
    global db
    db.setDatabaseName('student.db')
    # 打开连接
    db.open()


# 尝试注册账户
def registAUser():
    model = QSqlQueryModel()
    username = regist_dialog.testUsername.text()
    password = regist_dialog.testPassword.text()
    password1 = regist_dialog.textPassword1.text()
    # 比较两次输入的密码是否一致
    if password1 != password:
        regist_dialog.labelError.setText("两次输入密码不一致！")
        return
    # 查询数据库中是否存在同名用户
    model.setQuery("SELECT * FROM USER WHERE USERNAME = '" + username + "'")
    # debug
    # print(username)
    # print("SELECT * FROM USER WHERE USERNAME = '" + username + "'")
    # print(model.rowCount())
    if model.rowCount() == 0:
        pwd = encodePWD(password)
        model.setQuery("INSERT INTO USER VALUES (" + "'" + username + "'," + "'" + pwd + "'," + "1)")
        regist_dialog.labelError.setText("注册成功")
    else:
        regist_dialog.labelError.setText("用户名已存在")


# 启动注册系统
def registSystem():
    global regist_dialog
    global window
    window = QDialog()
    regist_dialog.setupUi(window)
    window.show()
    regist_dialog.buttonSubmit.clicked.connect(registAUser)


# 启动登入系统
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


# main函数
def main():
    # MACOS BIGSUR兼容
    os.environ['QT_MAC_WANTS_LAYER'] = '1'
    # QT环境初始化
    connectdb()
    app = QApplication()
    loginSystem()
    app.exec_()


# 程序入口
if __name__ == '__main__':
    main()
