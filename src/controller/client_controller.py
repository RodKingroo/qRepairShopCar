from database.connection import Connection
from model.client_model import Client

class ClientController():
    def __init__(self):
        self.client = Client(Connection())
        
    def InsertClient(self, id, name, passport, address, phone):
        self.client.InsertClient(id, name, passport, address, phone)
        print('complete')
        
    def GetClient_name(self, id, name, passport, address, phone):
        self.client.GetClient_name(id, name, passport, address, phone)
        print('complete')
        
    def GetAllClient(self, combobox):
        self.client.GetAllClient(combobox)
        print('complete')
        
    def UpdateClient(self, id, name, address, phone):
        self.client.UpdateClient(id, name, address, phone)
        print('complete')
        
    def CountClient(self):
        self.client.CountClient()
        print('complete')
    
    def DelWithClient_ID(self, id):
        self.client.DelWithClient_ID(id)
        print('complete')