from PyQt5 import QtWidgets

from PyQT.view.selected_view import Ui_Form
from PyQT.command.insert_client_command import ClientInsertCommand
from PyQT.command.insert_car_command import CarInsertCommand
from PyQT.command.insert_service_command import ServiceInsertCommand
from PyQT.command.update_client_command import ClientUpdateCommand

class SelectedCommand(QtWidgets.QWidget):
    def __init__(self):
        self.clientInsert = ClientInsertCommand()
        self.carInsert = CarInsertCommand()
        self.serviceInsert = ServiceInsertCommand()
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
        self.ui.InsertCarButton.clicked.connect(lambda: self.carInsert.show())
        self.ui.InsertServiceButton.clicked.connect(lambda: self.serviceInsert.show())
        self.ui.UpdateClientButton.clicked.connect(lambda: self.clientUpdate.show())