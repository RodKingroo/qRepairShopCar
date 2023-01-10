from PyQt5 import QtWidgets

from PyQT.view.car_insert_view import Ui_Form
from controller.car_controller import CarController
from controller.client_controller import ClientController

class CarInsertCommand(QtWidgets.QWidget):
    def __init__(self):
        self.carController = CarController()
        self.clientController = ClientController()
        self.width = 220
        self.height = 290
        super(CarInsertCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.width, self.height) 
        self.InsertCar()
        
    def InsertCar(self):
        self.clientController.GetAllClient(self.ui.car_owner_combo_box)
        self.ui.add_button_2.clicked.connect(lambda: self.carController.InsertCar(self.ui.cars_id_line_edit.text(),
                                                                                  self.ui.cars_brand_line_edit.text(),
                                                                                  self.ui.cars_place_line_edit.text(),
                                                                                  self.ui.cars_year_line_edit.text(),
                                                                                  self.ui.cars_model_line_edit.text(),
                                                                                  self.ui.cars_km_line_edit.text(),
                                                                                  self.ui.car_owner_combo_box.currentData()))