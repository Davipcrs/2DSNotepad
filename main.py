from PySide6.QtWidgets import QApplication
from view.mainwindow import MainWindow
from controller.main_func import mkdir
import sys

def main():
    app = QApplication(sys.argv)

    mkdir()

    window = MainWindow()
    window.show()

    try:
        with open("style/dark/darktheme.qss", "r") as f:
            _style = f.read()
            app.setStyleSheet(_style)

    except:
        with open("themes/darktheme.qss", "r") as f:
            _style = f.read()
            app.setStyleSheet(_style)  


    app.exec()


if __name__ == "__main__":
    main()


##using pyinstaller in windows to generate a .exe file.
##pyinstaller --windowed .\gui\main.py --paths C:\Users\davip\Documents\Projetos\2DpsNotes --add-data 'C:\Users\davip\Documents\Projetos\2DpsNotes\style\dark\darktheme.qss;themes' --add-data 'C:\Users\davip\Documents\Projetos\2DpsNotes\LICENSE;license' --name 2DSNotepad