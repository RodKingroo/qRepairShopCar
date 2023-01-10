class Client():
    def __init__(self, connect):
        self.connect = connect
        with self.connect.cursor() as cursor:
            request = '''CREATE TABLE IF NOT EXISTS client
                        (client_id INT PRIMARY KEY UNIQUE,
                         client_name VARCHAR(256) NOT NULL,
                         client_passport CHAR(11) NOT NULL,
                         client_address VARCHAR(256) NOT NULL,
                         client_phone CHAR(11) NOT NULL)'''
            cursor.execute(request)
        self.connect.commit()

    # insert client
    def InsertClient(self, id, name, passport, address, phone):
        with self.connect.cursor() as cursor:
            request = '''INSERT INTO client (client_id, client_name, 
                                             client_passport, client_address, client_phone)
                         VALUES (%s, %s, %s, %s, %s)'''
            cursor.execute(request, (id, name, passport, address, phone))
            print(f'({(id, name, passport, address, phone)} recorded in the console)')
            self.connect.commit()
            
    # get client_name
    def GetClient_name(self, id):
        with self.connect.cursor() as cursor:
            request = """SELECT client_name, client_passport, create_address, create_phone 
                             FROM client WHERE client_id = %s"""
            cursor.execute(request, (id))
            result = cursor.fetchall()
            if result:
                return result
            
    def GetClient_name_(self, id):
        with self.connect.cursor() as cursor:
            request = """SELECT client_name FROM client WHERE client_id = %s"""
            cursor.execute(request, (id))
            result = cursor.fetchall()
            if result:
                return result
            
    # get all client
    def GetAllClient(self, combobox):
        with self.connect.cursor() as cursor:
            request = '''SELECT * FROM client'''
            cursor.execute(request)
            result = cursor.fetchall()
            for result in result:
                combobox.addItem(str(result[1]), int(result[0]))
            
    # update client
    def UpdateClient(self, id, name, address, phone):
        with self.connect.cursor() as cursor:
            request = '''UPDATE client SET client_name = %s, 
                                        client_address = %s, 
                                        client_phone = %s
                                  WHERE client_id = %s'''
            cursor.execute(request, (id, name, address, phone))
            self.connect.commit()
            
    # count client
    def CountClient(self):
        with self.connect.cursor() as cursor:
            request = '''SELECT COUNT(*) FROM client'''
            cursor.execute(request)
            result = cursor.fetchall()
            return result
        
    # del with client_id
    def DelWithClient_ID(self, id):
        with self.conn.cursor() as cursor:
            request = """DELETE FROM client WHERE client_id = %s"""
            cursor.execute(request, id)
            self.conn.commit() 