import sys
import os
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)

from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
from app.main_func import mkdir

def main():
    app = QApplication(sys.argv)

    mkdir()

    window = MainWindow()
    window.show()

    with open("style/dark/darktheme.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    


    app.exec()


if __name__ == "__main__":
    main()


