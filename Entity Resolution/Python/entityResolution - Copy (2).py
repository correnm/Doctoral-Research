
from xgoogle.search import GoogleSearch, SearchError
from BeautifulSoup import BeautifulSoup
from collections import defaultdict

import os
import sys
import time
import urllib2
import urllib
import MySQLdb
import requests
import mechanize

'''
@Author Corren McCoy, 2014
@Purpose
Entity Resolution of known community with online social network
'''

# blank space
blank=" "
wildcard="*"
termsep="+"
conjunction=" AND "
# define the empty dictionary
dataset = defaultdict(list)
# default affiliation
affiliation='Regent University'
site='site:www.linkedin.com/in'


def openConnection():
    global conn 
    global cursor

    try:
        conn = MySQLdb.connect(host="localhost",
                               user="corren",
                               passwd="c0ree3n",
                               db="corren")
    # Catch the exception
    except Exception as e:
        print e
        
def closeConnection():
    # Close the db connection
    try:
        conn.close()
    except Exception as e:
        print e
        
def readSeedDB():
#    conn = MySQLdb.connect("localhost","corren","c0ree3n","corren") 
#    cursor = conn.cursor()

    openConnection()
    cursor = conn.cursor()

    try:
        # Query for the list of people we want to find in the (T)raining set
        cursor.execute('''SELECT dataset_pk, first_name, last_name FROM dataset where record_type= 'T' and dataset_pk like '1' ''')
        all_rows = cursor.fetchall()
        for row in all_rows:
            # row[0] returns the first column in the query (name), row[1] returns second column.
            dataset[row[0]].append((row[1], row[2]))
            #print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
        # DEBUG: see contents from database table
        # print dict(dataset)
    # Catch the exception
    except Exception as e:
        print e
    finally:
        # Close the db connection
        closeConnection()

def linkedInPublicProfiles():
    openConnection()
    cursor = conn.cursor()
    
    # search for each person's public profile on LinkedIn
    for pk in dataset.keys():
        print
        # query parameters for search engine
        first = None
        last = None
        fullname = None
        # data extracted from the result page
        linkedin_fullname=None
        
        for elements in dataset[pk]:
            first = elements[0]
            last = elements[1]
            fullname = blank.join([first, last])

        # format search parameters
        fullnameS = '"' + fullname + '"'
        
        #searchString is "full name" AND site:www.linkedin.com
        searchString = conjunction.join([fullnameS, site])
        print "Searching LinkedIn for: " + fullname + " using search string " + searchString
        try:
          gs = GoogleSearch(searchString)
          gs.results_per_page = 25 # 10 25 50 100 are valid values
          results = []
          while True:
              tmp = gs.get_results()
              if not tmp: # no more results were found
                  break
              results.extend(tmp)
          print "Results", len(results)
                          
          # process the results
          for res in results:
              title = res.title.encode('utf8')
              desc = res.desc.encode('utf8')
              url = res.url.encode('utf8')
              print title, url
              print
              
        except SearchError, e:
            print "Google search failed: %s" % e
    
def origlinkedInPublicProfiles():
    openConnection()
    cursor = conn.cursor()
    
    # search for each person's public profile on LinkedIn
    for pk in dataset.keys():
        print
        # query parameters for search engine
        first = None
        last = None
        fullname = None
        # data extracted from the result page
        linkedin_fullname=None
        
        for elements in dataset[pk]:
            first = elements[0]
            last = elements[1]
            fullname = blank.join([first, last])

        # format search parameters
        fullnameS = '"' + fullname + '"'
        
        #searchString is "full name" AND site:www.linkedin.com
        searchString = conjunction.join([fullnameS, site])
        print "Searching LinkedIn for: " + fullname + " using search string " + searchString
        try:
          gs = GoogleSearch(searchString)
          gs.results_per_page = 100 # 10 25 50 100
          results = gs.get_results()
          print "Results", len(results)
          # DEBUG
          #print "Search returned: " + str(gs.num_results)

          # Delete any old records associated with this record in the dataset
          query = "delete from linkedin where dataset_pk = %s"

          # execute the query
          cursor.execute(query, (pk,))
          # accept the change
          conn.commit()

          for res in results:
            title = res.title.encode('utf8')
            desc = res.desc.encode('utf8')
            url = res.url.encode('utf8')
            
            # add each result to the table
            query="insert into linkedin (dataset_pk, title, description, url, search_name) values (%s, %s, %s, %s, %s)"
            cursor.execute(query,(pk, title, desc, url, fullname,))
            conn.commit()
            
            #package the request
            url=res.url.encode('utf8')
            request=urllib2.Request(url)
            # Understanding the user agent string (http://msdn.microsoft.com/en-us/library/ms537503(VS.85).aspx)
            request.add_header('User-agent',' Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0)')
            response=urllib2.urlopen(request)
            if response.code == 200 and title.find(fullname) != -1:
                html=response.read()
                # decode byte stream to unicode
                html = html.decode("utf-8")
                # encode to ASCII byte stream, removing characters with codes >127
                html = html.encode("ascii", "ignore") 
                soup = BeautifulSoup(html)
                #DEBUG: show the html of the retrieved page
                #print soup

                try:
                    linkedin_fullname = soup.html.body.find('span',{'class' : 'full-name'}).string.strip()
                # Catch the exception
                except Exception as e:
                    print e
           
                # Update the name of the matching record in the table
                query="update linkedin set full_name = %s where dataset_pk = %s"
                cursor.execute(query,(linkedin_fullname,pk,))
                conn.commit()

                if linkedin_fullname:
                    print "LinkedIn Full Name: " + linkedin_fullname
                else:
                    print "LinkedIn Full Name not in profile page"
                    
                #index for education records
                index=0
                educationRec={}
                for schoolName in soup.html.body.findAll('tr',{'id' : 'overview-summary-education'}):
                    #print schoolName
                    #second anchor is the name of university
                    temp=schoolName.find('a',{'title':'More details for this school'})
                    #print temp
                    if temp:
                        universityName=temp.text.strip()
                        educationRec[index]=universityName
                        print res.title.encode('utf8')
                        print res.desc.encode('utf8')
                        print res.url.encode('utf8')
 
                        if universityName.find(affiliation) != -1:
                            print "Education: " + universityName
                            print
                        else:
                            print "Not an affiliate of " + affiliation
                            print
                    index=index+1
            response.close()
 
        except SearchError, e:
            print "Search failed: %s" % e

    closeConnection()

############################################################################             
#  This is main procedure in this package
############################################################################
def main():
#1. Read the database file with training data set
    readSeedDB()
    #DEBUG
    #print dataset
#2. Google Search for public profiles on LinkedIn
    linkedInPublicProfiles()


if __name__ == '__main__':
    main()
