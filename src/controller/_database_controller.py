from database._connection import Connection
from model._database_model import DataBaseModel

class DatabaseController():
    def __init__(self):
        self.database = DataBaseModel(Connection())