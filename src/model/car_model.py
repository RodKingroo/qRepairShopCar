class Car():
    #  create table: car
    def __init__(self, connect):
        self.connect = connect
        with self.connect.cursor as cursor:
            request = '''CREATE TABLE IF NOT EXISTS car
                        (car_id INT PRIMARY KEY UNIQUE,
                         car_brand VARCHAR(128) NOT NULL,
                         car_plate CHAR(7) NOT NULL,
                         car_year INT NOT NULL
                         car_model VARCHAR(128) NOT NULL,
                         car_km INT NOT NULL,
                         car_owner INTEGER NOT NULL,
                         FOREIGN KEY(car_owner) REFERENCES client(client_id))'''
            cursor.execute(request)
            self.connect.commit()
    
    # insert car
    def InsertCar(self, id, brand, place, year, model, km, owner):
        with self.connect.cursor as cursor:
            request = '''INSERT INTO car (car_id, car_brand, car_plate, car_year, car_model, car_km, car_owner)
                         VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(request, (id, brand, place, year, model, km, owner))
            self.connect.commit()
            
    # get car_id
    def GetCar_ID(self, brand, plate, year, model, km, owner):
        with self.connect.cursor() as cursor:
            request = """SELECT car_id FROM car WHERE car_brand = %s
                                              and car_place = %s
                                              and car_year = %s
                                              and car_model = %s
                                              and car_km = %s
                                              and car_owner = %s"""
            cursor.execute(request, (brand, plate, year, model, km, owner))
            result = cursor.fetchone()
            if result:
                return result
            
    # get all car
    def GetAllCar(self):
        with self.connect.cursor() as cursor:
            request = '''SELECT * FROM car'''
            cursor.execute(request)
            result = cursor.fetchall()
            return result
    
    # update car
    def UpdateCar(self, id, brand, place, year, model, km, owner):
        with self.connect.cursor() as cursor:
            request = '''UPDATE car SET car_brand = %s, 
                                        car_plate = %s, 
                                        car_year = %s, 
                                        car_model = %s,
                                        car_km = %s,
                                        car_owner = %s
                                  WHERE car_id = %s'''
            cursor.execute(request, (id, brand, place, year, model, km, owner))
            self.connect.commit()
            
    # count cars
    def CountCars(self):
        with self.connect.cursor() as cursor:
            request = '''SELECT COUNT(*) FROM car'''
            cursor.execute(request)
            result = cursor.fetchall()
            return result
        
    # del with car_id
    def DelWithCar_ID(self, id):
        with self.conn.cursor() as cursor:
            request = """DELETE FROM car WHERE car_id = %s"""
            cursor.execute(request, id)
            self.conn.commit() 