from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton, QApplication, QSizePolicy


class CustomLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()

    def sizeHint(self):
        return QSize(20, 20)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Button")
        self.layout = QHBoxLayout(self)
        line_edit = CustomLineEdit()
        #line_edit = QLineEdit(self)
        button = QPushButton("Login")

        line_edit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.layout.addWidget(line_edit)
        self.layout.addWidget(button)

        self.setFocus()


app = QApplication()
win = MainWindow()
win.show()
app.exec()
