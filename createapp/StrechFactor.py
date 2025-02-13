from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Button")
        self.layout = QHBoxLayout(self)
        button1 = QPushButton("1")
        button2 = QPushButton("2")
        button3 = QPushButton("3")

        self.layout.addWidget(button1)
        self.layout.addWidget(button2)
        self.layout.addWidget(button3)

        self.layout.setStretch(0, 5)
        self.layout.setStretch(1, 1)
        self.layout.setStretch(2, 10)

        self.setFocus()


app = QApplication()
wind = MainWindow()
wind.show()
app.exec()
