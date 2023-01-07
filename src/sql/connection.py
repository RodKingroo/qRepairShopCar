from mysql.connector import MySQLConnection

def connect():
    connect = MySQLConnection(host='localhost',
                              user='root',
                              password='chanmeme',
                              database='cars')
    
    return connect