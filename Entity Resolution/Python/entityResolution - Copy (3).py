'''
@Author Corren McCoy, 2014
@Purpose Entity Resolution of known community with online social network
'''

__author__ = 'cmccoy@cs.odu.edu (Corren McCoy)'

from xgoogle.search import GoogleSearch, SearchError
from apiclient.discovery import build
from BeautifulSoup import BeautifulSoup
from collections import defaultdict

import collections
import csv
import json
import os
import pprint
import random
import re
import sys
import time
import urllib2
import urllib
import MySQLdb
import requests
import mechanize
import xmltodict

def description():
  """
  Full explanation for the processing in the entityResolution module

  """
  print description.__doc__

# Configuration parameters

# mySQL connection string
sqlHost    = "localhost"
sqlUser    = "corren"
sqlPasswd  = "c0ree3n"
sqlDb      = "corren"

# blank space
blank=" "
lang="en"
wildcard="*"
termsep="+"
conjunction="+"
# define the empty dictionary
dataset = defaultdict(list)
# default affiliation
affiliation='Regent University'
site='site:www.linkedin.com/in'
results=[] # used to store results from Google Custom Search Element API
linkedinURLs=[]

# Define tuples for constant data which cannot be changed
AFFILIATION = (
    'Regent University'
    )
SITE =  (
    # LinkedIn public profiles can be associated with these URLs
    'www.linkedin.com/in',
    'www.linkedin.com/pub'
    )
BROWSERS = (
    # Most popular browsers as of December 8, 2014.
    # Retrieved from http://techblog.willshouse.com/2012/01/03/most-common-user-agents/
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36'
)

def stripHtmlTags (self, htmlTxt):
    if HtmlTxt is None:
        return None
    else:
        return ''.join(BeautifulSoup(htmlTxt).findAll(text=True))
      
def openConnection():
    global conn 
    global cursor

    try:
        conn = MySQLdb.connect(host=sqlHost,
                               user=sqlUser,
                               passwd=sqlPasswd,
                               db=sqlDb)
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
        cursor.execute('''SELECT dataset_pk, first_name, last_name FROM dataset where record_type= 'T' and dataset_pk like '8' ''')
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
        if conn.open :
          closeConnection()

def randomWait():
    # get a random number in this range (seconds)
    wait = random.uniform(2,5)
    time.sleep(wait)


# Search using the Google custom search engine
def searchGoogleCSE():
    openConnection()
    cursor = conn.cursor()
    searchEngine="Google"
    
    # search for each person's public profile on LinkedIn
    for pk in dataset.keys():
        print
        # query parameters for search engine
        first = None
        last = None
        fullname = None
        
        for elements in dataset[pk]:
            first = elements[0]
            last = elements[1]
            fullname = termsep.join([first, last])
            
        # format search parameters
        searchString = "allintitle:"+fullname
        print "Google Custom Search for: ", searchString

        try:
            # try to space our calls so we look like a human user
            randomWait()
            # Browser
            br = mechanize.Browser()

            # Browser options
            br.set_handle_equiv(True)
            br.set_handle_gzip(True)
            br.set_handle_redirect(True)
            br.set_handle_referer(True)
            br.set_handle_robots(False)

            # User-Agent (this is cheating, ok?)
            randomUserAgent=random.choice(BROWSERS)
            br.addheaders = [('User-agent', randomUserAgent)]

            # Open the Google custom search URL
            # Use my CSE ID for the cx parameter
            url = "http://www.google.com/cse/api/013993674550209950690/cse/ptr-mn8l7h0&hl=%(lang)s&q=allintitle:%(query)s"
            #url = "http://www.google.com/search?start=0&num=20&filter=1&hl=%(lang)s&q=allintitle:%(query)s&client=google-csbe&output=xml_no_dtd&cx=013993674550209950690:ptr-mn8l7h0&nojs=1"

            #CSEurl = [url % { 'query': searchString, 'lang': lang }]
            #CSEurl= "".join(CSEurl)
            #print CSEurl
            
            #r = br.open(CSEurl)

            # Build a service object for interacting with the API. Visit
            # the Google APIs Console <http://code.google.com/apis/console>
            # to get an API key for your own application.
            service = build("customsearch", "v1",
            developerKey="AIzaSyDyvnRIwlTLNA_HNKqHmpvpitSaDNfFJbU")

            # Return only a partial list of fields from the response
            response = service.cse().list(
            q=searchString,
            fields="items(link, htmlTitle, pagemap(hcard(fn), person(location))), queries(request(startIndex,totalResults))",
            cx="013993674550209950690:ptr-mn8l7h0",
            ).execute()
            
            #pprint.pprint(response)
            results.append(response)
            totalResults = response.get('queries').get('request')[0].get('totalResults',0)
            print "TotalResults", totalResults
                                                                         
            try:
                # Delete any old records associated with this record in the dataset
                query = "delete from linkedin where dataset_pk = %s"
                
                # execute the query
                cursor.execute(query, (pk,))
                print "Rows deleted:", cursor.rowcount
                
                # accept the change
                conn.commit()
                
                for res in response.get('items',[]):
                    title = res.get('htmlTitle')
                    print "Title", title
                    resultFullname = res.get('pagemap',{}).get('hcard')[0].get('fn')
                    print "Full name", resultFullname
                    url = res.get('link')
                    print "URL", url
                    location = res.get('pagemap',{}).get('person')[0].get('location')
                    print "Location", location
                    
                    # add each result to the table
                    query="insert into linkedin (dataset_pk, title, location, url, search_name, full_name, search_engine) values (%s, %s, %s, %s, %s, %s ,%s)"
                    cursor.execute(query,(pk, title, location, url, fullname, resultFullname, searchEngine))
                    conn.commit()
                
            # Catch the database exception
            except Exception as e:
                print "Database exception", e
        # Catch the Google exception
        except Exception, e:
            print "Google Custom Search failed: %s" % e
    # Close the mySQL connection normally
    if conn.open:
        closeConnection()

  
# Search Google using the Mechanize browser emulater
def searchGoogleM():
    openConnection()
    cursor = conn.cursor()
    
    # search for each person's public profile on LinkedIn
    for pk in dataset.keys():
        print
        # query parameters for search engine
        first = None
        last = None
        fullname = None
        
        for elements in dataset[pk]:
            first = elements[0]
            last = elements[1]
            fullname = blank.join([first, last])
            
        # @TODO need to loop over the public URLs
        linkedIN = SITE[1]
        # format search parameters
        fullname = '"' + fullname + '"'
        searchString = fullname
        print "Searching Google for: ", searchString, linkedIN

        try:
            # try to space our calls so we look like a human user
            #randomWait()
            gs = GoogleSearch(searchString, random_agent=True, sitesearch=linkedIN)
            # don't grab too many results at one time
            gs.results_per_page = 10 # 10 25 50 100
            results=[]
            # prime the loop
            tmp=gs.get_results()
            x=0
            while tmp:
                x=x+1
                print x
                results.extend(tmp)
                #randomWait()
                tmp = gs.get_results()
                if not tmp: # no more results were found
                    break
            print "Results", len(results)

            try:
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
                    print title, url
                    
                    # add each result to the table
                    query="insert into linkedin (dataset_pk, title, description, url, search_name) values (%s, %s, %s, %s, %s)"
                    cursor.execute(query,(pk, title, desc, url, fullname,))
                    conn.commit()
            # Catch the database exception
            except Exception as e:
                print e
            finally:
                # Close the db connection
                closeConnection()
        # Catch the Google exception
        except Exception, e:
            print "Google Search failed: %s" % e
    # Close the mySQL connection normally
    if conn.open:
        closeConnection()



# Perform a Google search on the target social network
def searchGoogleX():
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
        
        #searchString is "full name" site:https://www.linkedin.com/in
        searchString = conjunction.join([fullnameS, site])
        print "Searching LinkedIn for: " + fullname + " using search string " + searchString
        try:
            # try to space our calls so we look like a human user
            gs = GoogleSearch(searchString, random_agent=True)
            # don't grab too many results at one time
            gs.results_per_page = 10 # 10 25 50 100
            results=[]
            while True:
                randomWait()
                tmp = gs.get_results()
                if not tmp: # no more results were found
                    break
                results.extend(tmp)
                print "Results (loop)", len(results)
            print "Results", len(results)

            try:
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
            # Catch the database exception
            except Exception as e:
                print e
            finally:
                # Close the db connection
                closeConnection()
        # Catch the Google exception
        except Exception, e:
            print "Search failed: %s" % e
    # Close the mySQL connection normally
    if conn.open:
        closeConnection()
        

# Perform a Yahoo search on the target social network
def searchYahoo():
    openConnection()
    cursor = conn.cursor()
    

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
          # try to space our calls so we look like a human user
          randomWait()  
          gs = GoogleSearch(searchString, random_agent=True)
          gs.results_per_page = 100 # 10 25 50 100
          results=[]
          while True:
            tmp = gs.get_results()
            if not tmp: # no more results were found
                break
            results.extend(tmp)
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

# Load nicknames from csv file compiled by Carlton Northern
# http://code.google.com/p/nickname-and-diminutive-names-lookup/
def loadNickNames(filename=None):
    openConnection()
    cursor = conn.cursor()

    # Delete any old records in the database tables (master - detail)
    query = "delete from given_names"
    # execute the query
    cursor.execute(query)

    query = "delete from nicknames"
    cursor.execute(query)
    # accept the change
    conn.commit()

  
    filename = filename or 'names1.2.csv'
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
                query="insert into given_names (name_pk, first_name) values (%s, %s)"
                cursor.execute(query,(name_pk, keyword.lower(),))
                conn.commit()
            
                for value in array[1:]:
                    nickname = value.strip()
                    lookup[keyword.lower()].append(nickname.lower())
                    # add the associated nicknames in lower case for consistency
                    try:
                      query="insert into nicknames (name_pk, nickname) values (%s, %s)"
                      cursor.execute(query,(name_pk, nickname.lower(),))
                      conn.commit()
                    except MySQLdb.IntegrityError as err:
                      print "Error when inserting nicknames: {}".format(err)
            print "Number of records imported: ", name_pk
        except Exception as e:
            print "Error: %s " % e

    cursor.close()
    closeConnection()

   
############################################################################             
#  This is main procedure in this package
############################################################################
def main(load=False):

#1. Load the nicknames into the database
    if load:
      loadNickNames()
#2. Read the database file with training data set
    readSeedDB()

#3. Google Search for public profiles on LinkedIn
    searchGoogleCSE()

#4. Yahoo Search for undiscovered public profiles on LinkedIn
    searchYahoo();
    
#5. Traverse all the query results from web searches to 
#    linkedInPublicProfiles()


if __name__ == '__main__':
    main()
