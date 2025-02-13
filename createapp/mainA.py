from PySide6.QtWidgets import QMainWindow
from PySide6 import QtCore
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QSizePolicy
from fbs_runtime.application_context.PySide2 import ApplicationContext

import sys

from createapp.main_window import MainWindow

if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = MainWindow()
    window.resize(250, 150)
    window.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
