class DataBaseModel():
    def __init__(self, connect):
        self.connect = connect
        with self.connect.cursor() as cursor:
            request='''CREATE DATABASE IF NOT EXISTS RepairShop'''
            cursor.execute(request)
            print('Database Added')
        self.connect.commit()