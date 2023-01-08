from PyQt5 import QtWidgets

from pyqt.view.register_view import Ui_Form

class RegisterCommand(QtWidgets.QWidget):
    def __init__(self):
        self.width = 520
        self.height = 360
        super(RegisterCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)