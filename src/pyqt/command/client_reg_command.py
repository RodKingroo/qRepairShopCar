from PyQt5 import QtWidgets

from pyqt.view.client_reg_view import Ui_Form
from cotroller.client_controller import ClientController

class ClientRegCommand(QtWidgets.QWidget):
    def __init__(self):
        self.clientController = ClientController()
        self.width = 220
        self.height = 260
        super(ClientRegCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.width, self.height)
        self.move(300, 300)
        self.CountClient()
        self.InsertClient()
        
    def CountClient(self):
        self.ui.count_client_line.setText(self.clientController.countClient())
        
    def InsertClient(self):
        self.ui.add_button.clicked.connect(lambda: self.clientController.insertClient(self.ui.client_id_line_edit.text(),
                                                                                      self.ui.client_name_line_edit.text(),
                                                                                      self.ui.client_passport_line_edit.text(), 
                                                                                      self.ui.client_address_line_edit.text(), 
                                                                                      self.ui.client_phone_line_edit.text()))