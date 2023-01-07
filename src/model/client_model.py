class Client():
    #  create table: client
    def __init__(self, connect):
        self.connect = connect
        with self.connect.cursor as cursor:
            request = '''CREATE TABLE IF NOT EXISTS client
                        (client_id INT PRIMARY KEY UNIQUE,
                         client_name VARCHAR(256) NOT NULL,
                         client_cpf CHAR(11) NOT NULL,
                         client_adress VARCHAR(256) NOT NULL
                         client_phone CHAR(11) NOT NULL)'''
            cursor.execute(request)
            self.connect.commit()
    
    # insert client
    def InsertClient(self, name, cpf, address, phone):
        with self.connect.cursor as cursor:
            request = '''INSERT INTO client (client_name, client_cpf, client_address, client_phone)
                         VALUES (%s, %s, %s, %s)'''
            cursor.execute(request, (name, cpf, address, phone))
            self.connect.commit()
            
    # get client_id
    def GetClient_ID(self, name, cpf, address, phone):
        with self.connect.cursor() as cursor:
            request = """SELECT client_id FROM client WHERE client_name = %s
                                                        and client_cpf = %s
                                                        and client_address = %s
                                                        and client_phone = %s"""
            cursor.execute(request, (name, cpf, address, phone))
            result = cursor.fetchone()
            if result:
                return result
            
    # get all client
    def GetAllClient(self):
        with self.connect.cursor() as cursor:
            request = '''SELECT * FROM client'''
            cursor.execute(request)
            result = cursor.fetchall()
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