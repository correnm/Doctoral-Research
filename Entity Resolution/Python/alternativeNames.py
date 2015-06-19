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
  Query the nicknames table in the mySQL database.
  Find alternative names for the indicate person.
  """
  print help.__doc__
  
def load(param_dataset_pk=None):
    logging.info('Enter alternativeNames.load')
    # We will indicate whether the name is the (O)riginal entry or an (A)lternative
    name_type_orig  = 'O'
    name_type_alias = 'A'
    
    manageMySQLDB.openConnection()
    cursor = manageMySQLDB.conn.cursor()

    # Remove any old data
    dataset.clear()
    try:
        # Query for the list of people we want to find in the (T)raining set
        # Middle name can be null in the table. Convert to the empty string
        cursor.execute('''SELECT dataset_pk, first_name, IFNULL(middle_name,''), last_name  
        FROM people where record_type= 'T' and dataset_pk = %s ''', param_dataset_pk)
        all_rows = cursor.fetchall()
        for row in all_rows:
            # row[0] returns the first column in the query (name), row[1] returns second column.
            dataset[row[0]].append(( row[1].lower(), row[2].lower(), row[3].lower() ))
            dataset_pk  = row[0]
            first_name  = row[1].lower()
            middle_name = row[2].lower()
            last_name   = row[3].lower()

            #print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

            try:
                # Delete any old records associated with this record in the dataset
                query = "delete from people_alt_names where dataset_pk = %s"
                # execute the query
                cursor.execute(query, (dataset_pk,))
                print "Rows deleted:", cursor.rowcount

                # (1) Insert the new name for the original records
                query = "insert into people_alt_names (dataset_pk, first_name, middle_name, last_Name, name_type) values (%s, %s, %s, %s, %s)"
                # execute the query
                cursor.execute(query, (dataset_pk,first_name, middle_name, last_name, name_type_orig,))

                # (2) first, middle initial, last
                if middle_name and len(middle_name) >= 1:
                  middle_init = middle_name[0]
                  query = "insert into people_alt_names (dataset_pk, first_name, middle_name, last_Name, name_type) values (%s, %s, %s, %s, %s)"
                  # execute the query
                  cursor.execute(query, (dataset_pk, first_name, middle_init, last_name, name_type_alias,))
                  
                # (3) first initial, middle name, last
                if first_name and middle_name and len(middle_name) >= 1:
                  first_init = first_name[0]
                  query = "insert into people_alt_names (dataset_pk, first_name, middle_name, last_Name, name_type) values (%s, %s, %s, %s, %s)"
                  # execute the query
                  cursor.execute(query, (dataset_pk, first_init, middle_name, last_name, name_type_alias,))
                
                # accept the change
                manageMySQLDB.conn.commit()
            # Catch the database exception
            except Exception as e:
                print "Database exception", e
                logging.error ("alternativeNames: Database exception %s", e)
                raise

            # Add any nicknames (e.g., Joseph --> Joe)
            cursor.execute('''SELECT nickname from nicknames n,
            given_names g  where g.name_pk = n.name_pk and lower(first_name) = %s
            ''', (first_name, ))
            
            nickname_rows = cursor.fetchall()
            for n_row in nickname_rows:
              # concat the nickname with original last name (e.g., Joe Smith, Joseph Smith)
              dataset[row[0]].append((n_row[0], row[2].lower()))
              nickname = n_row[0].lower()
              
              # Insert the new name for the original records
              query = "insert into people_alt_names (dataset_pk, first_name, last_Name, name_type) values (%s, %s, %s, %s)"
              # execute the query
              cursor.execute(query, (dataset_pk, nickname, last_name, name_type_alias,))
              alt_name_pk = cursor.lastrowid
              # accept the change
              manageMySQLDB.conn.commit()
 
        # DEBUG: see contents from database table
        for keys, values in dataset.items():
          print keys, values
          print
    # Catch the exception
    except Exception as e:
        print e
        logging.error(e)
        # Re-raise the last exception
        raise
    finally:
        # Close the db connection
        cursor.close()
        if manageMySQLDB.conn.open :
          manageMySQLDB.closeConnection()
        logging.info('Exit alternativeNames.load')
