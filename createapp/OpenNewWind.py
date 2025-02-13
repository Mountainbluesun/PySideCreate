from random import randrange
from PySide6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget


class RandomButton(QPushButton):
    def __init__(self, size=48, flat=False):
        super().__init__()
        self.setText(str(randrange(999)))
        self.setMaximumSize(size, size)
        self.setFlat(flat)
        self.setCheckable(True)
        self.setStyleSheet(f"color: rgb({randrange(255)}, {randrange(255)}, {randrange(255)});")
        self.clicked.connect(self.random_color)

    def random_color(self):
        self.setStyleSheet(f"color: rgb({randrange(255)}, {randrange(255)}, {randrange(255)});")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Button")
        self.layout = QHBoxLayout(self)
        for _ in range(10):
            btn_random = RandomButton(size=randrange(10, 80), flat=True)
            self.layout.addWidget(btn_random)

        #self.layout.addWidget(btn_random)

        self.setFocus()


app = QApplication()
win = MainWindow()
win.show()
app.exec()
