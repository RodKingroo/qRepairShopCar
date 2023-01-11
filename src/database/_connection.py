from mysql.connector import MySQLConnection
from config.read_config import ReadMySQLConfig
from PyQT.command.selected_command import SelectedCommand

def Connection(host, user, password, form):
    selected = SelectedCommand()
    connect = MySQLConnection(host=host,
                              user=user,
                              password=password)
    if connect.is_connected():
        with connect.cursor() as cursor:
            request='''CREATE DATABASE IF NOT EXISTS RepairShop'''
            cursor.execute(request)
            print('Database Added')
        connect.commit()
        selected.show()
        with open('config/main_config.ini', 'w+') as file:
                    file.write(f'[mysql]\nhost={host}\nuser={user}\npassword={password}\ndatabase=RepairShop')
                    file.close()
        form.close()
        print('Connect!')
    return connect