from mysql.connector import MySQLConnection
from config.read_config import ReadMySQLConfig

def Connection():
    db = ReadMySQLConfig()
    connect = MySQLConnection(**db.ReadConfig('main'))
    if connect.is_connected():
        print('Connect!')
    return connect

