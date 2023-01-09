from PyQt5 import QtWidgets

from pyqt.view.car_reg_view import Ui_Form
from cotroller.car_controller import CarController
from cotroller.client_controller import ClientController

class CarRegCommand(QtWidgets.QWidget):
    def __init__(self):
        self.carController = CarController()
        self.clientController = ClientController()
        self.width = 220
        self.height = 320
        super(CarRegCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.width, self.height)
        self.move(600, 250)
        self.CountCars()
        self.InsertCars()
        
    def CountCars(self): 
        self.ui.count_car_line.setText(self.carController.countCar())
        
    def InsertCars(self):
        self.ui.add_button_2.clicked.connect(self.carController.insertCar(self.ui.cars_id_line_edit.text(),
                                                                          self.ui.cars_brand_line_edit.text(),
                                                                          self.ui.cars_place_line_edit.text(),
                                                                          self.ui.cars_year_line_edit.text(),
                                                                          self.ui.cars_model_line_edit.text(),
                                                                          self.ui.cars_km_line_edit.text(),
                                                                          self.clientController.getClient_ID(self.ui.car_owner_combo_box)))