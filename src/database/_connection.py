from mysql.connector import MySQLConnection
from config.read_config import ReadMySQLConfig

def Connection():
    db = ReadMySQLConfig()
    connect = MySQLConnection(**db.ReadConfig('first'))
    if connect.is_connected():
        with open('config/main_config.ini', 'w+') as file:
                    file.write(f'[mysql]\nhost=localhost\nuser=root\npassword=chanmeme\ndatabase=RepairShop')
                    file.close()
        print('Connect!')
    return connect