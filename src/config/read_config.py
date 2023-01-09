from configparser import ConfigParser

def ReadMySQLConfig(filename='src/config/config.ini', selection='mysql'):
    parser = ConfigParser()
    parser.read(filename)
    
    db = {}
    if parser.has_section(selection):
        items = parser.items(selection)
        for item in items:
            db[item[0]] = item[1]    
    else:
        raise Exception('{0} not found in the {1} file'.format(selection, filename))
    return db