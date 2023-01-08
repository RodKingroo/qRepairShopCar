from PyQt5 import QtWidgets

from pyqt.view.car_reg_view import Ui_Form

class CarRegCommand(QtWidgets.QWidget):
    def __init__(self):
        self.width = 220
        self.height = 320
        super(CarRegCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.width, self.height)
        self.move(600, 250)