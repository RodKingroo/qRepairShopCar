from PyQt5 import QtWidgets

from PyQT.view.client_insert_view import Ui_Form
from controller.client_controller import ClientController

class ClientInsertCommand(QtWidgets.QWidget):
    def __init__(self):
        self.clientController = ClientController()
        self.width = 220
        self.height = 230
        super(ClientInsertCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.width, self.height) 
        self.InsertClient()
        
    def InsertClient(self):
        self.ui.add_button.clicked.connect(lambda: self.clientController.InsertClient(self.ui.client_id_line_edit.text(),
                                                                                      self.ui.client_name_line_edit.text(),
                                                                                      self.ui.client_passport_line_edit.text(), 
                                                                                      self.ui.client_address_line_edit.text(), 
                                                                                      self.ui.client_phone_line_edit.text()))