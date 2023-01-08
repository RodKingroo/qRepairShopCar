from src.model.car_model import Car
from src.sql.connection import Connect

class CarController():
    def __init__(self):
        self.car = Car(Connect())
    
    def insertCar(self, id, brand, place, year, model, km, owner):
        if id and brand and place and year and model and km and owner:
            self.car.InsertCar(id, brand, place, year, model, km, owner)
            
    def getCar_ID(self, brand, place, year, model, km, owner):
        if brand and place and year and model and km and owner:
            self.car.GetCar_ID(brand, place, year, model, km, owner)
            
    def GetAllCar(self):
        self.car.GetAllCar()
    
    def updateCar(self, id, brand, place, year, model, km, owner):
        if id and brand and place and year and model and km and owner:
            self.car.UpdateCar(id, brand, place, year, model, km, owner)
            
    def countCar(self):
        self.car.CountCars()
        
    def delWidthCar_id(self, id):
        if id:
            self.car.DelWithCar_ID(id)