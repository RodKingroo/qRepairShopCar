from PyQt5 import QtWidgets

from pyqt.view.service_reg_view import Ui_Form

class ServiceRegCommand(QtWidgets.QWidget):
    def __init__(self):
        self.width = 210
        self.height = 260
        super(ServiceRegCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.width, self.height)
        self.move(900, 300)