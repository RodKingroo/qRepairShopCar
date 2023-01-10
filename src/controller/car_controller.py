from model.car_model import Car
from database.connection import Connection

class CarController():
    def __init__(self):
        self.car = Car(Connection())
    
    def InsertCar(self, id, brand, place, year, model, km, owner):
        self.car.InsertCar(id, brand, place, year, model, km, owner)
        print('insertCar complete!')
            
    def GetCar_ID(self, brand, place, year, model, km, owner):
        self.car.GetCar_ID(brand, place, year, model, km, owner)
        print('getCar_ID complete!')
            
    def GetAllCar(self, combobox):
        self.car.GetAllCar(combobox)
        print('GetAllCar complete!')
    
    def UpdateCar(self, id, brand, place, year, model, km, owner):
        self.car.UpdateCar(id, brand, place, year, model, km, owner)
        print('updateCar complete!')
            
    def CountCar(self):
        self.car.CountCars()
        print('countCar complete!')
        
    def DelWidthCar_id(self, id):
        self.car.DelWithCar_ID(id)
        print('delWidthCar_id complete!')