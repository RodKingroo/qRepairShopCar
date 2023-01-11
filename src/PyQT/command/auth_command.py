from PyQt5 import QtWidgets

from PyQT.view.auth_view import Ui_Form
from database._connection import Connection

class AuthCommand(QtWidgets.QMainWindow):
    def __init__(self):
        self.width = 220
        self.height = 200
        super().__init__()
       
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.AuthorizationCommand()
        
    def AuthorizationCommand(self):
        self.ui.enterButton.clicked.connect(lambda: Connection(self.ui.lineEdit_hostname.text(),
                                                               self.ui.lineEdit_user.text(),
                                                               self.ui.lineEdit_password.text(),
                                                               self))