from model.client_model import Client
from sql.connection import Connect

class ClientController():
    def __init__(self):
        self.client = Client(Connect()) 
    
    def insertClient(self, id, name, passport, address, phone):
        self.client.InsertClient(id, name, passport, address, phone)
        print('insertClient complete!')
    
    def getClient_ID(self, name, passport, address, phone):
        self.client.GetClient_ID(name, passport, address, phone)
        print('getClient_ID complete!')
    
    def getClient_ID(self, combobox):
        self.client.GetClient_ID(combobox)
        print('getClient_Name_ID complete!')
    
    def getAllClient(self):
        self.client.GetAllClient()
        print('getAllClient complete!')
        
    def updateClient(self, id, name, address, phone):
        self.client.UpdateClient(id, name, address, phone)
        print('updateClient complete!')
            
    def countClient(self):
        self.client.CountClient()
        print('countClient complete!')
        
    def delWithClient_ID(self, id):
        self.client.DelWithClient_ID(id)
        print('delWithClient_ID complete!')
