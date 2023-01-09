from PyQt5 import QtWidgets

from pyqt.view.service_reg_view import Ui_Form
from cotroller.service_controller import ServiceController

class ServiceRegCommand(QtWidgets.QWidget):
    def __init__(self):
        self.serviceController = ServiceController()
        self.width = 210
        self.height = 260
        super(ServiceRegCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.width, self.height)
        self.move(900, 300)
        self.CountService()
        
    def CountService(self):
        self.ui.count_service_line.setText(self.serviceController.countService())
        