from mysql.connector import MySQLConnection

def Connect():
    connect = MySQLConnection(host='localhost',
                              user='root',
                              password='chanmeme',
                              database='cars')
    
    return connect