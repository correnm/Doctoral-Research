# Python libraries
import collections
from collections import defaultdict
import csv
import logging
import MySQLdb
import os
import os.path

# my libraries
import manageMySQLDB


# define the empty dictionary
dataset = defaultdict(list)

def author():
  """
  cmccoy@cs.odu.edu (Corren McCoy) @2015
  """
  
def help():
  """
  Query the person table in the mySQL database.
  Allow user to select one name from the training set to process
  """
  print help.__doc__
  
def showPeople():
    choice = None
    logging.info('started selectPerson')
    manageMySQLDB.openConnection()
    cursor = manageMySQLDB.conn.cursor()

    try:
        # Query for the list of people we want to find in the (T)raining set
        cursor.execute('''SELECT dataset_pk, first_name, IFNULL(middle_name,''), last_name FROM people where record_type= 'T'
        ''', )
        all_rows = cursor.fetchall()
        os.system('cls') # for windows    
        print "==========================\n"
        print "Select a record to process"

        for row in all_rows:
            # row[0] returns the first column in the query (name), row[1] returns second column.
            dataset[row[0]].append((row[1].lower(), row[2].lower()))
            dataset_pk = row[0]
            first_name = row[1].lower()
            middle_name  = row[2].lower()
            last_name = row[3].lower()
            print dataset_pk, first_name, middle_name, last_name
        choice = raw_input(" Enter a number>>  ")

        logging.info('Selected dataset key %s ', choice)

    # Catch the exception
    except Exception as e:
        print e
        logging.error(e)
        # Re-raise the last exception
        raise
      
    cursor.close()
    manageMySQLDB.closeConnection()  
    # Return menu selection to the main program
    return choice

