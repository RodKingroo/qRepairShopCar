from src.model.service_model import Service
from src.sql.connection import Connect

class ServiceController():
    def __init__(self):
        self.service = Service(Connect())
        
    def insertService(self, id, problem, price, car, client):
        if id and problem and price and car and client:
            self.service.InsertService(id, problem, price, car, client)
            
    def getService_ID(self, problem, price, car, client):
        if problem and price and car and client:
            self.service.GetService_ID(problem, price, car, client)
            
    def getAllService(self):
        self.service.GetAllService()
        
    def updateService(self, id, problem, price, car, client):
        if id and problem and price and car and client:
            self.service.UpdateService(id, problem, price, car, client)
            
    def countService(self):
        self.service.CountService()
        
    def delWithService_ID(self, id):
        if id:
            self.service.DelWithService_ID(id)