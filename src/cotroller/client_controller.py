from model.client_model import Client
from sql.connection import Connect

class UserController():
    def __init__(self):
        self.client = Client(Connect())
    
    def insertClient(self, id, name, passport, address, phone):
        if id and name and passport and address and phone:
            self.client.InsertClient(id, name, passport, address, phone)
    
    def getClient_ID(self, name, passport, address, phone):
        if name and passport and address and phone:
            self.client.GetClient_ID(name, passport, address, phone)
    
    def getAllClient(self):
        self.client.GetAllClient()
        
    def updateClient(self, id, name, address, phone):
        if id and name and address and phone:
            self.client.UpdateClient(id, name, address, phone)
            
    def countClient(self):
        self.client.CountClient()
        
    def delWithClient_ID(self, id):
        if id:
            self.client.DelWithClient_ID(id)
