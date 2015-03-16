from ConfigParser import SafeConfigParser
import MySQLdb


def read_db_config(filename='config.ini', section='mysqlWindows'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return a dictionary of database parameters
    """

    # create parser and read ini configuration file
    parser = SafeConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception ('{0} not found in the {1} file'.format(section,filename))
    return db

def openConnection():
    """ Connect to MySQL database """
    global conn
    global cursor

    db_config = read_db_config()
    try:
        print 'Connecting to MySQL database. . . '
        conn = MySQLdb.connect(**db_config)

        if conn.open:
            print('Connection established.')
        else:
            print('Connection failed.')

    # Catch the exception
    except Exception as e:
        print e
      
def closeConnection():
    # Close the db connection
    try:
        conn.close()
    except Exception as e:
        print e

if __name__ == '__main__':
    openConnection()