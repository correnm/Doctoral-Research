# Python libraries
import collections
import csv
import logging
import MySQLdb
import os
import os.path

# my libraries
import manageMySQLDB


def author():
  """
  cmccoy@cs.odu.edu (Corren McCoy) @2015
  """
  
def help():
  """
  Load nicknames from csv file compiled by Carlton Northern
  http://code.google.com/p/nickname-and-diminutive-names-lookup/
  """
  print help.__doc__
  
def load(filename=None):
    manageMySQLDB.openConnection()
    cursor = manageMySQLDB.conn.cursor()
    logging.info('entered nicknames.load')

    # Delete any old records in the database tables (master - detail)
    query = "delete from given_names"
    # execute the query
    cursor.execute(query)

    query = "delete from nicknames"
    cursor.execute(query)
    # accept the change
    manageMySQLDB.conn.commit()

 
    filename = filename or 'names1.2.csv'
    # when a modole is loaded __file__ is set to its name
    filename = os.path.join(os.path.dirname('__file__'), filename)
    lookup = collections.defaultdict(list)
    with open(filename) as f:
        try:
            # Initialize the primary key value
            name_pk = 0
            # Read rows from the csv file
            reader = csv.reader(f)
            # read a row as column 1: value 1, column2 :value 2
            for line in f.readlines():
                array = line.split(',')
                keyword = array[0]
                # Primary key is a sequence number
                name_pk = name_pk + 1
                # add each given name to the table in lower case for consistency
                query="insert ignore into given_names (name_pk, first_name) values (%s, %s)"
                cursor.execute(query,(name_pk, keyword.lower(),))
                manageMySQLDB.conn.commit()
            
                for value in array[1:]:
                    nickname = value.strip()
                    lookup[keyword.lower()].append(nickname.lower())
                    # add the associated nicknames in lower case for consistency
                    try:
                      query="insert ignore into nicknames (name_pk, nickname) values (%s, %s)"
                      cursor.execute(query,(name_pk, nickname.lower(),))
                      manageMySQLDB.conn.commit()
                    except MySQLdb.IntegrityError as err:
                      print "Error when inserting nicknames: {}".format(err)
                      logging.error ("Error when inserting nicknames: {}".format(err))
                      raise
            print "Number of records imported: ", name_pk
            logging.info("Number of records imported: %s", name_pk)
        except Exception as e:
            print "Error: %s " % e
            logging.error(e)
            raise

    cursor.close()
    if manageMySQLDB.conn.open :
      manageMySQLDB.closeConnection()

    logging.info('Exit nicknames.load')
