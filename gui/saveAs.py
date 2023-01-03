from ui.ui_saveAsDialog import Ui_SaveAsDialog
from PySide6.QtWidgets import QDialog

class SaveAsDialog(QDialog):
    def __init__(self):
        super(SaveAsDialog, self).__init__()
        self.ui = Ui_SaveAsDialog()
        self.ui.setupUi(self)