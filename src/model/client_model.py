class Client():
    #  create table: client
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
            request = '''INSERT INTO client (client_id, client_name, client_passport, client_address, client_phone)
                         VALUES (%s, %s, %s, %s, %s)'''
            cursor.execute(request, (id, name, passport, address, phone))
            self.connect.commit()
            
    # get client_id
    def GetClient_ID(self, name, passport, address, phone):
        with self.connect.cursor() as cursor:
            request = """SELECT client_id FROM client WHERE client_name = %s
                                                        and client_passport = %s
                                                        and client_address = %s
                                                        and client_phone = %s"""
            cursor.execute(request, (name, passport, address, phone))
            result = cursor.fetchone()
            if result:
                return result
         
    # get client_id
    def GetClient_ID(self, combobox):
        with self.connect.cursor() as cursor:
            request = '''SELECT client_id FROM client'''
            cursor.execute(request)
            result = cursor.fetchall()
            while result:
                combobox.addItem(str(result))
            
    # get all client
    def GetAllClient(self):
        with self.connect.cursor() as cursor:
            request = '''SELECT * FROM client'''
            cursor.execute(request)
            result = cursor.fetchall()
            if result:
                return result
    
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