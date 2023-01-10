from PyQt5 import QtWidgets

from PyQT.view.selected_view import Ui_Form
from PyQT.command.insert_client_command import ClientInsertCommand
from PyQT.command.update_command import ClientUpdateCommand

class SelectedCommand(QtWidgets.QWidget):
    def __init__(self):
        self.clientInsert = ClientInsertCommand()
        self.clientUpdate = ClientUpdateCommand()
        self.width = 380
        self.height = 190
        super(SelectedCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.width, self.height)
        self.ClientCommand()
        
    def ClientCommand(self):
        self.ui.InsertClientButton.clicked.connect(lambda: self.clientInsert.show())
        self.ui.UpdateClientButton.clicked.connect(lambda: self.clientUpdate.show())