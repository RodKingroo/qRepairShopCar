from mysql.connector import MySQLConnection
from config.read_config import ReadMySQLConfig

def Connect():
    db_config = ReadMySQLConfig()
    connect = MySQLConnection(**db_config)
    
    return connect