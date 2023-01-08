from PyQt5 import QtWidgets

from pyqt.view.index_view import Ui_Form

from pyqt.command.register_command import RegisterCommand
from pyqt.command.search_command import SearchCommand

class IndexCommand(QtWidgets.QWidget):
    def __init__(self):
        self.register = RegisterCommand()
        self.search = SearchCommand()
        self.width = 220
        self.height = 70
        super(IndexCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.SelectRegister()
        self.SelectSearch()
        
    def SelectRegister(self):
        self.ui.regestration_button.clicked.connect(lambda: self.register.show())
    
    def SelectSearch(self):
        self.ui.search_button.clicked.connect(lambda: self.search.show())