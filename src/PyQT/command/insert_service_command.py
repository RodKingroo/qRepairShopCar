from PyQt5 import QtWidgets

from PyQT.view.service_insert_view import Ui_Form
from controller.car_controller import CarController
from controller.client_controller import ClientController
from controller.service_controller import ServiceController

class ServiceInsertCommand(QtWidgets.QWidget):
    def __init__(self):
        self.carController = CarController()
        self.clientController = ClientController()
        self.serviceController = ServiceController()
        self.width = 210
        self.height = 230
        super(ServiceInsertCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.width, self.height) 
        self.InsertService()
        
    def InsertService(self):
        self.clientController.GetAllClient(self.ui.service_owner_combo_box)
        self.carController.GetAllCar(self.ui.service_car_combo_box)
        self.ui.add_button_3.clicked.connect(lambda: self.serviceController.InsertService(self.ui.service_id_line_edit.text(),
                                                                                          self.ui.service_problem_line_edit.text(),
                                                                                          self.ui.service_price_line_edit.text(),
                                                                                          self.ui.service_car_combo_box.currentData(),
                                                                                          self.ui.service_owner_combo_box.currentData()))