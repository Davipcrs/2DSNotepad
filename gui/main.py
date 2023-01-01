from PySide6.QtWidgets import QApplication
import sys
from mainwindow import MainWindow

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    with open("style\dark\darktheme.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    


    app.exec()


if __name__ == "__main__":
    main()


