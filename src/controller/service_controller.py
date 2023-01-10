from model.service_model import Service
from database.connection import Connection

class ServiceController():
    def __init__(self):
        self.service = Service(Connection())
        
    def InsertService(self, id, problem, price, car, client):
        self.service.InsertService(id, problem, price, car, client)
        print('insertClient complete!')
            
    def GetService_ID(self, problem, price, car, client):
        self.service.GetService_ID(problem, price, car, client)
        print('getService_ID complete!')
            
    def GetAllService(self):
        self.service.GetAllService()
        print('getAllService complete!')
        
    def UpdateService(self, id, problem, price, car, client):
        self.service.UpdateService(id, problem, price, car, client)
        print('updateService complete!')
            
    def CountService(self):
        self.service.CountService()
        print('countService complete!')
        
    def DelWithService_ID(self, id):
        self.service.DelWithService_ID(id)
        print('delWithService_ID complete!')