from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyNotes")
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.modify_widgets()
        self.add_widgets_to_layout()
        self.setup_connections()

    def create_widgets(self):
        self.btn_createNotes = QtWidgets.QPushButton("Create a note")
        self.lw_notes = QtWidgets.QListWidget()
        self.te_content = QtWidgets.QTextEdit()

    def modify_widgets(self):
        pass

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)

    def add_widgets_to_layout(self):
        self.main_layout.addWidget(self.btn_createNotes, 0, 0, 1, 1)
        self.main_layout.addWidget(self.lw_notes, 1, 0, 1, 1)
        self.main_layout.addWidget(self.te_content, 0, 1, 2, 1)

    def setup_connections(self):
        pass

    def create_note(self):
        print("Create a note new")

    def delete_selected_note(self):
        print("delete of a note")

    def populate_notes(self):
        print("Loading notes from disk ")

    def populate_note_content(self):
        print("Loading content of the note")

    def save_note(self):
        print("Backup content of the note")



app = QApplication()
win = MainWindow()
win.show()
app.exec()
