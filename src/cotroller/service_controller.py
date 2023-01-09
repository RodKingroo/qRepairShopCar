from model.service_model import Service
from sql.connection import Connect

class ServiceController():
    def __init__(self):
        self.service = Service(Connect())
        
    def insertService(self, id, problem, price, car, client):
        self.service.InsertService(id, problem, price, car, client)
        print('insertClient complete!')
            
    def getService_ID(self, problem, price, car, client):
        self.service.GetService_ID(problem, price, car, client)
        print('getService_ID complete!')
            
    def getAllService(self):
        self.service.GetAllService()
        print('getAllService complete!')
        
    def updateService(self, id, problem, price, car, client):
        self.service.UpdateService(id, problem, price, car, client)
        print('updateService complete!')
            
    def countService(self):
        self.service.CountService()
        print('countService complete!')
        
    def delWithService_ID(self, id):
        self.service.DelWithService_ID(id)
        print('delWithService_ID complete!')