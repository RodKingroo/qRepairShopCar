from PyQt5 import QtWidgets

from PyQT.view.update_view import Ui_Form
from controller.client_controller import ClientController

class ClientUpdateCommand(QtWidgets.QWidget):
    def __init__(self):
        self.clientController = ClientController()
        self.width = 220
        self.height = 230
        super(ClientUpdateCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.width, self.height)
        self.UpdateClient()
   
    def UpdateClient(self):
        self.clientController.GetAllClient(self.ui.comboBox)
        # self.ui.searchButton.clicked.connect(
        #     self.clientController.GetClient_name(
        #         self.ui.comboBox.currentData(), 
        #         self.ui.client_name_line_edit,
        #         self.ui.client_passport_line_edit,
        #         self.ui.client_address_line_edit,
        #         self.ui.client_phone_line_edit))
        