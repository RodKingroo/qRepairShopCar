from database.connection import Connection
from model.client_model import Client

class ClientController():
    def __init__(self):
        self.client = Client(Connection())
        
    def InsertClient(self, id, name, passport, address, phone):
        self.client.InsertClient(id, name, passport, address, phone)
        print('complete')
        
    def GetClient_name(self, id):
        self.client.GetClient_name(id)
        
    def GetClient_name_(self, id):
        self.client.GetClient_name_(id)
        
    def GetAllClient(self, combobox):
        self.client.GetAllClient(combobox)
        
    def UpdateClient(self, id, name, address, phone):
        self.client.UpdateClient(id, name, address, phone)
        
    def CountClient(self):
        self.client.CountClient()
    
    def DelWithClient_ID(self, id):
        self.client.DelWithClient_ID(id)