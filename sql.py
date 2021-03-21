import os
from PySide2.QtCore import *
from PySide2.QtSql import *
from PySide2.QtWidgets import *

os.environ['QT_MAC_WANTS_LAYER'] = '1'
app = QApplication()
db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('student.db')
db.open()
view = QTableView()
model = QSqlTableModel()
view.setModel(model)
model.setTable('STUDENT')
model.select()
view.show()
app.exec_()