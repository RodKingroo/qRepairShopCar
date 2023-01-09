from PyQt5 import QtWidgets

from pyqt.view.index_view import Ui_Form

from pyqt.command.client_reg_command import ClientRegCommand
from pyqt.command.car_reg_command import CarRegCommand
from pyqt.command.service_reg_command import ServiceRegCommand
from pyqt.command.search_command import SearchCommand

class IndexCommand(QtWidgets.QWidget):
    def __init__(self):
        self.client_reg = ClientRegCommand()
        self.car_reg = CarRegCommand()
        self.service_reg = ServiceRegCommand()
        self.search = SearchCommand()
        self.width = 220
        self.height = 70
        super(IndexCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.width, self.height)
        self.SelectRegister()
        self.SelectSearch()
        
    def SelectRegister(self):
        self.ui.regestration_button.clicked.connect(lambda: self.ShowRegWindows())
    
    def ShowRegWindows(self):
        self.client_reg.show()
        self.car_reg.show() 
        self.service_reg.show()
    
    def SelectSearch(self):
        self.ui.search_button.clicked.connect(lambda: self.search.show())