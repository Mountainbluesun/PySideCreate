
from PySide6 import QtCore
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QSizePolicy
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QListWidget, QVBoxLayout, \
    QHBoxLayout, QGridLayout
from functools import partial


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My application great")

        self.main_layout = QVBoxLayout(self)
        self.lw_todos = QListWidget()
        self.lw_task_title = QLineEdit()
        self.lw_task_title.setPlaceholderText("Task to be done")
        self.btn_clear = QPushButton("All delete")

        self.main_layout.addWidget(self.lw_todos)
        self.main_layout.addWidget(self.lw_task_title)
        self.main_layout.addWidget(self.btn_clear)

        self.lw_task_title.returnPressed.connect(self.add_todo)
        self.btn_clear.clicked.connect(self.lw_todos.clear)
        self.lw_todos.itemDoubleClicked.connect(self.delete_todo)

    def add_todo(self):
        self.lw_todos.addItem(self.lw_task_title.text())
        self.lw_task_title.clear()

    def delete_todo(self, item):
        self.lw_todos.takeItem(self.lw_todos.row(item))


app = QApplication()
win = MainWindow()
win.show()
app.exec()
