from PyQt5 import QtWidgets

from pyqt.view.client_reg_view import Ui_Form

class ClientRegCommand(QtWidgets.QWidget):
    def __init__(self):
        self.width = 220
        self.height = 260
        super(ClientRegCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.width, self.height)
        self.move(300, 300)