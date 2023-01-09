from model.car_model import Car
from sql.connection import Connect

class CarController():
    def __init__(self):
        self.car = Car(Connect())
    
    def insertCar(self, id, brand, place, year, model, km, owner):
        self.car.InsertCar(id, brand, place, year, model, km, owner)
        print('insertCar complete!')
            
    def getCar_ID(self, brand, place, year, model, km, owner):
        self.car.GetCar_ID(brand, place, year, model, km, owner)
        print('getCar_ID complete!')
            
    def GetAllCar(self):
        self.car.GetAllCar()
        print('GetAllCar complete!')
    
    def updateCar(self, id, brand, place, year, model, km, owner):
        self.car.UpdateCar(id, brand, place, year, model, km, owner)
        print('updateCar complete!')
            
    def countCar(self):
        self.car.CountCars()
        print('countCar complete!')
        
    def delWidthCar_id(self, id):
        self.car.DelWithCar_ID(id)
        print('delWidthCar_id complete!')