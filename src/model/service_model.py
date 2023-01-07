class Service():
    #  create table: services
    def __init__(self, connect):
        self.connect = connect
        with self.connect.cursor as cursor:
            request = '''CREATE TABLE IF NOT EXISTS service
                        (service_id INT PRIMARY KEY UNIQUE,
                         service_problem VARCHAR(256) NOT NULL,
                         service_price FLOAT NOT NULL,
                         service_car INT NOT NULL
                         service_client INT NOT NULL,
                         FOREIGN KEY(service_car) REFERENCES car(car_id),
                         FOREIGN KEY(service_client) REFERENCES client(client_id))'''
            cursor.execute(request)
            self.connect.commit()
    
    # insert service
    def InsertService(self, problem, price, car, client):
        with self.connect.cursor as cursor:
            request = '''INSERT INTO service (service_problem, service_price, service_car, service_client)
                         VALUES (%s, %s, %s, %s)'''
            cursor.execute(request, (problem, price, car, client))
            self.connect.commit()
            
    # get service_id
    def GetService_ID(self, problem, price, car, client):
        with self.connect.cursor() as cursor:
            request = """SELECT service_id FROM service WHERE service_problem = %s
                                                          and service_price = %s
                                                          and service_car = %s
                                                          and servoce_client = %s"""
            cursor.execute(request, (problem, price, car, client))
            result = cursor.fetchone()
            if result:
                return result
            
    # get all services
    def GetAllServoce(self):
        with self.connect.cursor() as cursor:
            request = '''SELECT * FROM service'''
            cursor.execute(request)
            result = cursor.fetchall()
            return result
    
    # update service
    def UpdateService(self, id, problem, price, car, client):
        with self.connect.cursor() as cursor:
            request = '''UPDATE service SET service_problem = %s, 
                                            service_price = %s, 
                                            service_car = %s,
                                            service_car = %s
                                      WHERE service_id = %s'''
            cursor.execute(request, (id, problem, price, car, client))
            self.connect.commit()
            
    # count service
    def CountService(self):
        with self.connect.cursor() as cursor:
            request = '''SELECT COUNT(*) FROM service'''
            cursor.execute(request)
            result = cursor.fetchall()
            return result
        
    # del with service_id
    def DelWithService_ID(self, id):
        with self.conn.cursor() as cursor:
            request = """DELETE FROM service WHERE service_id = %s"""
            cursor.execute(request, id)
            self.conn.commit() 