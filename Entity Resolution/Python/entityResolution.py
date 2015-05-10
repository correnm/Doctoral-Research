'''
@Author Corren McCoy, 2015
@Purpose Entity Resolution of known community with online social network
'''

__author__ = 'cmccoy@cs.odu.edu (Corren McCoy)'

from xgoogle.search import GoogleSearch, SearchError
from apiclient.discovery import build
from BeautifulSoup import BeautifulSoup
from ConfigParser import SafeConfigParser
from collections import defaultdict
from TwitterCredentials import credentials
import mainMenu


import codecs
import collections
import datetime
import csv
import json
import logging
import nltk
import os
import pprint
from py2neo import Graph
import random
import re
import sys
import time
import urllib2
import urllib
import matplotlib.pyplot as plt
import MySQLdb
import networkx as nx
import requests
import mechanize
import time
import tweepy
import urllib
import urllib2
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()
import xmltodict



def description():
  """
  Full explanation for the processing in the entityResolution module

  """
  print description.__doc__


# blank space
blank=" "
lang="en"
wildcard="*"
termsep="+"
conjunction="+"
SPECIAL_CHARACTERS="1234567890!@#$%^&*()_+-={}[];':\"<>?,./ "

# define the empty dictionary
dataset = defaultdict(list)
linkedin_affiliation = defaultdict(list)
linkedin_pav = defaultdict(list)

#### TWITTER
# variables used to manage the API rate limit
FIFTEEN_MIN=900 # seconds
FIVE_MIN=300
ITEM_LIMIT=1000

def saveWebPage(name, network, url):
  
  logging.info("saveWebPage %s %s %s", name, network, url)
  
  archiveDir = "./archive/"
  now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
  filename = archiveDir + ''.join(name.split()) + "_" + ''.join(network.split()) + "_" + now + '.html'
  headerfilename = archiveDir + ''.join(name.split()) + "_" + ''.join(network.split()) + "_header_" + now + '.txt'

  #package the request
  url=url.encode('utf8')
  #request=requests.Request(url)
  # Understanding the user agent string (http://msdn.microsoft.com/en-us/library/ms537503(VS.85).aspx)
  randomUserAgent=random.choice(BROWSERS)
  headers=dict()
  headers['User-Agent'] = randomUserAgent
  
  #print headers
  response=requests.get(url, headers=headers)
  if response.status_code == 200:
      html=response.text
      # encode to ASCII byte stream, removing characters with codes >127
      html = html.encode("ascii", "ignore") 
      archiveFile = open (filename, 'wb')
      # save the server's response
      archiveFile.write(html)
      headerFile = open(headerfilename, 'wb')
      h=json.dumps(dict(response.headers))
      headerFile.write(h)
  
  
def loginTwitter():
    logging.info('loginTwitter')
    
    # Initialize the oAuth authentication settings
    # Documentation: https://dev.twitter.com/docs/auth/oauth
    CONSUMER_KEY    = credentials['CONSUMER_KEY']       ## "LrA1DdH1QJ5cfS8gGaWp0A"
    CONSUMER_SECRET = credentials['CONSUMER_SECRET']    ## "9AX14EQBLjRjJM4ZHt2kNf0I4G77sKsYX1bEXQCW8"
    OAUTH_TOKEN     = credentials['OAUTH_TOKEN']        ## "1862092890-FrKbhD7ngeJtTZFZwf2SMjOPwgsCToq2A451iWi"
    OAUTH_SECRET    = credentials['OAUTH_SECRET']       ## "AdMQmyfaxollI596G82FBipfSMhagv6hjlNKoLYjeg8"

    api = None
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
        #create an instance of a tweepy StreamListener to handle the incoming data
        api = tweepy.API(auth, api_root='/1.1')
    except tweepy.error.TweepError as e:
        remaining_hits = api.rate_limit_status('application')['resources']['application']['/application/rate_limit_status']['remaining']
        print '\n'
        print 'You have', remaining_hits, 'API calls remaining in this window.', time.ctime()
        logging.error('Tweepy Error from loginTwitter %s', e.reason)
        logging.info('You have %s %s %s', remaining_hits, 'API calls remaining in this window.', time.ctime())
        time.sleep(FIFTEEN_MIN)
        # Re-raise the last exception
        raise
    return api

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


def read_db_config(filename='config.ini', section='mysqlWindows'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return a dictionary of database parameters
    """

    logging.info('read_db_config')
    
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
  
    logging.info('openConnection')
    
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
        logging.error(e)
        print e
        # Re-raise the last exception
        raise
      
def closeConnection():
    logging.info('closeConnection')
      
    # Close the db connection
    try:
        conn.close()
    except Exception as e:
        logging.error(e)
        print e
        # re-raise the last exception
        raise

def stripHtmlTags (htmlTxt):
    if htmlTxt is None:
        return None
    else:
        return ''.join(BeautifulSoup(htmlTxt).findAll(text=True))
      
        
def readSeedDB(param_dataset_pk=None):
    logging.info('readSeedDB')
    name_type_orig ='O'
    name_type_alias = 'A'
    
#    openConnection()
#    cursor = conn.cursor()

    # Remove any old data
    dataset.clear()
    try:
        # Query for the list of people we want to find in the (T)raining set
        cursor.execute('''SELECT dataset_pk, first_name, last_name
        FROM people where record_type= 'T' and dataset_pk = %s ''', param_dataset_pk)
        all_rows = cursor.fetchall()
        for row in all_rows:
            # row[0] returns the first column in the query (name), row[1] returns second column.
            dataset[row[0]].append((row[1].lower(), row[2].lower()))
            dataset_pk = row[0]
            first_name = row[1].lower()
            last_name  = row[2].lower()
            #print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

            try:
                # Delete any old records associated with this record in the dataset
                query = "delete from people_alt_names where dataset_pk = %s"
                # execute the query
                cursor.execute(query, (dataset_pk,))
                print "Rows deleted:", cursor.rowcount

                # Insert the new name for the original records
                query = "insert into people_alt_names (dataset_pk, first_name, last_Name, name_type) values (%s, %s, %s, %s)"
                # execute the query
                cursor.execute(query, (dataset_pk,first_name, last_name, name_type_orig,))
                
                # accept the change
                conn.commit()
            # Catch the database exception
            except Exception as e:
                print "Database exception", e
                logging.error ("READSEEBDB: Database exception %s", e)

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
              conn.commit()
 
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
  #  finally:
        # Close the db connection
  #      if conn.open :
  #        closeConnection()

def randomWait():
    # get a random number in this range (seconds)
    wait = random.uniform(2,5)
    time.sleep(wait)


# Search using the Google custom search engine
def searchGoogleCSE(dataset_pk, delete=True, startPage=1):
#    openConnection()
#    cursor = conn.cursor()
    logging.info('searchGoogleCSE')
    searchEngine="Google"
    numResults=20
    totalResults=0 # CSE limit
    maxResults=100
    
    # search for each person's public profile on LinkedIn using primary key
    # Query for the list of people we want to find in the (T)raining set
    cursor.execute('''SELECT dataset_pk, first_name, last_name, alt_name_pk FROM people_alt_names where dataset_pk = %s ''', dataset_pk)
    all_rows = cursor.fetchall()
    for row in all_rows:
        # initialize query parameters for search engine
        pk = row[0]
        first = None
        last = None
        fullname = None
        alt_name_pk = None

        try:
            if delete:
              # Delete any old records associated with this record in the dataset
              query = "delete from linkedin_candidates where dataset_pk = %s"
              # execute the query
              cursor.execute(query, (pk,))
              print "Rows deleted:", cursor.rowcount
              delete=False

              # accept the change
              conn.commit()
        # Catch the database exception
        except Exception as e:
            print "Database exception", e
            logging.error("SearchGoogleCSE: Database exception %s", e)

        first = row[1]
        last = row[2]
        fullname = blank.join([first, last])
        searchName = termsep.join([first, last])
        alt_name_pk =  row[3]        
        # format search parameters
        searchString = "allintitle:"+searchName
        print
        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        print "Google Custom Search for: ", searchString

        try:
              # try to space our calls so we look like a human user
              randomWait()
              # Browser
              '''
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
              '''
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
              # to get an API key for your own application. This is the one for LinkedIn
              service = build("customsearch", "v1",
              developerKey="AIzaSyDyvnRIwlTLNA_HNKqHmpvpitSaDNfFJbU")

              # Return only a partial list of fields from the response
              try:
                response = service.cse().list(
                q=searchString,
                cx="013993674550209950690:ptr-mn8l7h0",
                start=startPage
                ).execute()

                position = 0
                while (response != None): 
                  totalResults = response.get('queries').get('request')[0].get('totalResults',0)
                  print "About", totalResults, "Results"

                  for res in response.get('items',[]):
                      # relative position in search results
                      position = position + 1

                      title = res.get('title')
                      # Remove the html tags from the title
                      #title = stripHtmlTags(title)
                      print "Title", title
                      resultFullname = res.get('pagemap',{}).get('hcard')[0].get('fn')
                      print "Full name", resultFullname
                      url = res.get('link')
                      print "original URL", url
                      #Is the URL an alias or redirect to another page?
                      final_url=finalURL(url)
                      print "resolved URL", final_url
                      location = res.get('pagemap',{}).get('person')[0].get('location')
                      print "Location", location
                      
                      # does this profile already exist in the table?
                      query="select linkedin_pk from linkedin where url_pub = %s"
                      cursor.execute(query,(final_url))
                      row = cursor.fetchone()
                      if row is not None:
                          linkedin_pk =row[0]
                      else:
                          # Existing record not found. So we create a new one
                          # add each result to the table
                          query="insert into linkedin (title, location, url_pub, full_name, search_engine, alt_name_pk) values (%s, %s, %s, %s, %s, %s)"
                          cursor.execute(query,(title, location, final_url, resultFullname, searchEngine, alt_name_pk))
                          linkedin_pk = cursor.lastrowid
                          conn.commit()
                      print "linkedin_pk %s " % linkedin_pk 
                      print "pk %s" % pk 
                      print "position %s" % position
                      query="insert ignore into linkedin_candidates (dataset_pk, linkedin_pk, position_no) values (%s, %s, %s)"
                      print query
                      
                      # archive the html for the web page
                      saveWebPage(resultFullname.replace(" ","_"), 'linkedin', final_url)
                      try:
                        cursor.execute(query,(pk, linkedin_pk, position))
                        conn.commit()
                      except MySQLdb.Error, e:
                        print "MySQL Error %s" %e
                        logging.error(e)
                        
                  nextPage=response.get('queries').get('nextPage')[0].get('startIndex')
                  startPage = nextPage
                  if nextPage:
                      print "\n next", nextPage
              
                  response = service.cse().list(
                  q=searchString,
                  cx="013993674550209950690:ptr-mn8l7h0",
                  start=startPage
                  ).execute()
                      
                  if (response == None):
                     break

              # Catch the Google exception
              except SearchError, e:
                 print "(1) Search failed: %s" % e              
              except Exception, e:
                 print "(1) Google Custom Search failed: %s" % e
        except SearchError, e:
            print "(2) Search failed: %s" % e              
        except Exception, e:
            print "(2) Google Custom Search failed: %s" % e
            logging.error(e)

    # Close the mySQL connection normally
    #if conn.open:
    #  closeConnection()

        
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
            alt_name_pk = elements[2]
            
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
                print "Rows deleted:", cursor.rowcount

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
    

def linkedInAffiliation(dataset_pk=None):
    logging.info('linkedInAffiliation')
    try:
        # Query for the list of candidate LinkedIn public profiles
        query ='''SELECT l.linkedin_pk, url_pub FROM linkedin_candidates c,  linkedin l 
        where c.dataset_pk= %s and c.linkedin_pk = l.linkedin_pk'''

        cursor.execute(query,(dataset_pk,))
        all_rows = cursor.fetchall()
        # clear the list each time
        linkedin_affiliation.clear()
        for row in all_rows:
            # row[0] returns the first column in the query (name), row[1] returns second column.
            linkedin_affiliation[row[0]].append(row[1].lower())
    
        # search for each person's public profile on LinkedIn
        for pk, value in linkedin_affiliation.items():
          url = str(value).strip('[]')
          url = url.strip('\'"')
          url = url.encode("utf-8")
          print pk, url 
          try:
            # Delete any old records associated with this record in the dataset
            query = "delete from linkedin_affiliation where linkedin_pk = %s"

            # execute the query
            cursor.execute(query, (pk,))
            print "Rows deleted from linkedin_affiliation table:", cursor.rowcount
            # accept the change
            conn.commit()
            
            #package the request
            #url=url.encode('utf8')
            request=urllib2.Request(url)
            # Understanding the user agent string (http://msdn.microsoft.com/en-us/library/ms537503(VS.85).aspx)
            randomUserAgent=random.choice(BROWSERS)
            #print randomUserAgent
            request.add_header('User-agent', randomUserAgent)
            response=urllib2.urlopen(request)
            #print "response" , response.code
            if response.code == 200:
                html=response.read()
                # decode byte stream to unicode
                html = html.decode("utf-8")
                # encode to ASCII byte stream, removing characters with codes >127
                html = html.encode("ascii", "ignore") 
                soup = BeautifulSoup(html)
                #DEBUG: show the html of the retrieved page
                #print soup
                schoolsAttended= soup.html.body.find('div',{'id' : 'background-education-container'})
                if schoolsAttended:
                    for temp in schoolsAttended.findAll('h4',{'class':'summary fn org'}):
                      education = temp.find('a',{'title':'More details for this school'})
                      if education:
                        universityName = education.string
                        if universityName:
                          print "insert university", universityName
                          try:
                            # is this a known affiliation? if so, get the PK
                            query ='''SELECT affiliation_pk 
                            FROM research.affiliations 
                            where lower(affiliation_name) = lower(%s) 
                            UNION
                            select n.affiliation_pk
                            from affiliations a, 
                            affiliation_alt_names n 
                            where a.affiliation_pk = n.affiliation_pk 
                            and lower(n.affiliation_name) = lower(%s)'''

                            # reset the PK
                            affiliation_pk = None
                            cursor.execute(query,(universityName, universityName,))
                            aff_row =cursor.fetchone()
                            if aff_row:
                                affiliation_pk = aff_row[0]

                            query='''insert into linkedin_affiliation (linkedin_pk, affiliation_name, affiliation_pk) 
                            values (%s, %s, %s)'''
                            cursor.execute(query,(pk, universityName, affiliation_pk,))
                            conn.commit()
                          except Exception as e:
                            print "Error while inserting linkedin affiliation", e
            print              
            response.close()
          except Exception as e:
            print e
            logging.error(e)
    # Catch the database exception
    except Exception as e:
      print e
      logging.error(e)
      # Re-raise the last exception
      raise

def finalURL (url=None, verbose=None):
    logging.info('finalURL')
                 
    finalurl= url
    if not url:
        pass
        #url='https://www.linkedin.com/in/bohdan'
        #url='http://www.linkedin.com/pub/bohdan-smaha-mba/4/a01/a2'
    else:
        request=urllib2.Request(url)
        # Understanding the user agent string (http://msdn.microsoft.com/en-us/library/ms537503(VS.85).aspx)
        randomUserAgent=random.choice(BROWSERS)
        #print randomUserAgent
        request.add_header('User-agent', randomUserAgent)
        response=urllib2.urlopen(request)
        if response == 200:
            finalurl=response.geturl()
        else:
            finalurl=url
        if verbose:
            print "RESPONSE" , response.code
            print "START-URL", url
            print "FINAL-URL",finalurl

            headers=response.info()
            print "DATE:", headers['date']
            print "HEADERS"
            print " -------------"
            print headers

    return finalurl

def peopleAlsoViewed(dataset_pk, degree):
    logging.info('peopleAlsoViewed')
    logging.info("--->degree %s %s %s",degree, "dataset_pk", dataset_pk)
    print "--->degree","PK", degree, dataset_pk

    
    try:
        # For first degree, get the "people also viewed" from the original profile page
        if degree == 1:
            cursor.execute('''SELECT l.linkedin_pk, l.url_pub, 0 
            FROM linkedin l,
            linkedin_candidates d
            where l.linkedin_pk = d.linkedin_pk
            and d.dataset_pk = %s ''' , (dataset_pk,))
        elif degree == 2:
            cursor.execute('''SELECT p.linkedin_pk, l.url_pub, p.pav_pk 
            FROM linkedin_pav p, 
            linkedin l 
            where p.pav_pk = l.linkedin_pk 
            and degree = 1
            and p.linkedin_pk in
            (
            select l.linkedin_pk
            from linkedin l,
            linkedin_candidates c
            where c.linkedin_pk = l.linkedin_pk
            and c.dataset_pk=%s
            )
             ''', (dataset_pk,))
        elif degree == 3:
            cursor.execute('''SELECT p.linkedin_pk, l.url_pub, p.pav_pk 
            FROM linkedin_pav p, 
            linkedin l 
            where p.pav_pk = l.linkedin_pk 
            and degree = 2
            and p.linkedin_pk in
            (
            select l.linkedin_pk
            from linkedin l,
            linkedin_candidates c
            where c.linkedin_pk = l.linkedin_pk
            and c.dataset_pk=%s
            )
             ''', (dataset_pk,))
        else:
            raise ValueError('Degree can only be set to 1, 2, or 3')
        
        all_rows = cursor.fetchall()
        print "Rows retrieved", cursor.rowcount

        # Clear the list each time so we don't keep appending the list (i.e., infinite loop)
        linkedin_pav.clear()
        deleteOld = True
        for row in all_rows:
          # row[0] returns the first column in the query (name), row[1] returns second column.
          linkedin_pav[row[0]].append(row[1].lower())
          pk = row[0]
          value = row[1].lower()
          parent_pav_pk = row[2]
          # search for each person's public profile on LinkedIn
          #for pk, value in linkedin_pav.items():
          url = str(value).strip('[]')
          url = url.strip('\'"')
          url = url.encode("utf-8")
          print pk, url, parent_pav_pk 
          try:
            if deleteOld:
              # Delete any old records associated with this record in the dataset
              query = "delete from linkedin_pav where linkedin_pk = %s and degree = %s"

              # execute the query
              cursor.execute(query, (pk, degree,))
              print "Rows deleted from linkedin_pav table:", cursor.rowcount
              # accept the change
              conn.commit()
              deleteOld = False
            
            #package the request
            url=url.encode('utf8')
            #request=requests.Request(url)
            # Understanding the user agent string (http://msdn.microsoft.com/en-us/library/ms537503(VS.85).aspx)
            randomUserAgent=random.choice(BROWSERS)
            #print randomUserAgent
            #request.add_header('User-agent', randomUserAgent)
            headers=dict()
            headers['User-Agent'] = randomUserAgent
            #print headers
            response=requests.get(url, headers=headers)
            print "response" , response.status_code
            if response.status_code == 200:
                #html=response.read()
                html=response.text
                # decode byte stream to unicode
                html = html.decode("utf-8","ignore")
                # encode to ASCII byte stream, removing characters with codes >127
                html = html.encode("ascii", "ignore") 
                soup = BeautifulSoup(html)
                #DEBUG: show the html of the retrieved page
                #print soup
                peopleAlsoViewed= soup.html.body.find('div',{'class' : 'insights-browse-map'})
                #print peopleAlsoViewed
                if peopleAlsoViewed:
                    position = 0
                    for temp in peopleAlsoViewed.findAll('li'):
                      position = position + 1
                      photo = temp.find('img', {'class' : ''})['src']
                      print "Photo: ", photo
                      h4 = temp.find('h4')
                      temp_url = h4.find('a')
                      #print "temp:", temp_url
                      url = temp_url['href'].strip('?trk=pub-pbmap')
                      final_url=finalURL(url)
                      print "URL: ", url, final_url
                      fullname =temp_url.contents[0]
                      print "Full name", fullname
                      profileTitle = temp.find('p',{'class': 'browse-map-title'}).string
                      print "Title", profileTitle
                      try:
                        # Have we already seen this profile?
                        query='''select linkedin_pk from linkedin where url_pub = %s'''
                        cursor.execute(query, (final_url))
                        row = cursor.fetchone()
                        if row is not None:
                            pav_pk = row[0]
                        else:
                            # New one. Add to table. Save the key
                            query="insert into linkedin (url_pub, full_name, title, profile_image_url) values (%s, %s, %s, %s)"
                            cursor.execute(query,(final_url, fullname, profileTitle, photo,))
                            pav_pk = cursor.lastrowid
                            conn.commit()
                        
                        query="insert into linkedin_pav (linkedin_pk, pav_pk, degree, parent_pav_pk, position_no) values (%s, %s, %s, %s,%s)"
                        cursor.execute(query,(pk, pav_pk, degree, parent_pav_pk, position))
                        conn.commit()
                      except Exception as e:
                        print "Error while inserting linkedin_pav", e
            print              
            response.close()
          except Exception as e:
            print e
            logging.error(e)
    # Catch the database exception
    except ValueError as e:
      print e
      logging.error(e)
      raise
    except Exception as e:
      print e
      logging.error(e)
      # Re-raise the last exception
      raise
 

# Load nicknames from csv file compiled by Carlton Northern
# http://code.google.com/p/nickname-and-diminutive-names-lookup/
def loadNickNames(filename=None):
#    openConnection()
#    cursor = conn.cursor()
    logger = logging.getLogger(__name__)
    logging.info('loadNickNames')

    # Delete any old records in the database tables (master - detail)
    query = "delete from given_names"
    # execute the query
    cursor.execute(query)

    query = "delete from nicknames"
    cursor.execute(query)
    # accept the change
    conn.commit()

  
    filename = filename or 'names1.2.csv'
    filename = os.path.join(os.path.dirname(__file__), filename)
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
            logging.error(e)

    cursor.close()
#    closeConnection()

def searchTwitterUsers(dataset_pk, delete=True, startPage=1):
    logging.info('searchTwitterUsers')
    
    if dataset_pk:
        # search for each person's public profile on LinkedIn using primary key
        # Query for the list of people we want to find in the (T)raining set
        cursor.execute('''SELECT dataset_pk, first_name, last_name, alt_name_pk FROM people_alt_names where dataset_pk = %s ''', dataset_pk)
        all_rows = cursor.fetchall()
        for row in all_rows:
            # initialize query parameters for Twitter API
            pk = row[0]
            first = None
            last = None
            fullname = None
            alt_name_pk = None

            try:
                if delete:
                    # Delete any old records associated with this record in the dataset
                    query = "delete from twitter_candidates where dataset_pk = %s"
                    # execute the query
                    cursor.execute(query, (pk,))
                    print "Twitter Candidate Rows deleted:", cursor.rowcount
                    delete=False

                    # accept the change
                    conn.commit()
            # Catch the database exception
            except Exception as e:
                print "Database exception", e

            first = row[1]
            last = row[2]
            fullname = blank.join([first, last])
            alt_name_pk =  row[3]  
            # format Google search parameters for Twitter     
            searchName = termsep.join([first, last]).encode("utf-8")
            twitterName = '"' + fullname.encode("utf-8") + '"'

            query="allintitle:" + searchName
            print "Google Custom Search for Twitter: ", searchName

            try:
                # try to space our calls so we look like a human user
                randomWait()
                # Open the Google custom search URL
                # Use my CSE ID for the cx parameter
         
                url = "http://www.google.com/cse/api/013993674550209950690/cse/hav5cnkqrzk0&hl=%(lang)s&q=allintitle:%(query)s"
    
                # Build a service object for interacting with the API. Visit
                # the Google APIs Console <http://code.google.com/apis/console>
                # to get an API key for your own application. Use the ID for Twitter
                service = build("customsearch", "v1", developerKey="AIzaSyDyvnRIwlTLNA_HNKqHmpvpitSaDNfFJbU")

                # Return only a partial list of fields from the response
                try:
                    response = service.cse().list(
                    q=query,
                    cx="013993674550209950690:hav5cnkqrzk",
                    start=startPage
                    ).execute()

                    if (response != None): 
                        totalResults = response.get('queries').get('request')[0].get('totalResults',0)
                        print "About", totalResults, "Twitter Results"
                        if totalResults > 0:
                            getTwitterUsers(dataset_pk, twitterName, totalResults, alt_name_pk)
                        else:
                            totalResults = 0

                # Catch the Google exception
                except SearchError, e:
                    print "(1) Twitter Search failed: %s" % e
                    logging.error(e)
                except Exception, e:
                    print "(1) Google Custom Search for Twitter failed: %s" % e
                    logging.error(e)
            except SearchError, e:
                print "(2) Twitter Search failed: %s" % e
                logging.error(e)
            except Exception, e:
                print "(2) Google Custom Search for Twitter failed: %s" % e
                logging.error(e)
                # Re-raise the last exception
                raise

def searchTwitterVanity(dataset_pk, delete=False):
    logging.info('searchTwitterVanity')
    try:
        if dataset_pk:
            # search for each person's public profile on Twitter using the screen name derived from Linkedin Vanity URL
            query= '''select c.dataset_pk, l.screen_name from linkedin_candidates c, linkedin l where screen_name is not null and c.linkedin_pk = l.linkedin_pk and c.dataset_pk = %s '''
            print query
            cursor.execute(query,(int(dataset_pk)))
            all_rows = cursor.fetchall()
            for row in all_rows:
                # initialize query parameters for Twitter API
                pk = row[0]
                screen_name = row[1]

                try:
                    if delete:
                        # Delete any old records associated with this record in the dataset
                        query = "delete from twitter_candidates where dataset_pk = %s"
                        # execute the query
                        cursor.execute(query, (pk,))
                        print "Twitter Candidate Rows deleted:", cursor.rowcount
                        delete=False

                        # accept the change
                        conn.commit()
                # Catch the database exception
                except Exception as e:
                    print "Database exception on delete", e
                    logging.error(e)

                twitterName = '"@' + screen_name.encode("utf-8") + '"'
                print "Twitter screen name is: ", twitterName
                # Searching Twitter with an actual screen name should only match one row
                totalResults=1
                getTwitterUsers(dataset_pk, twitterName, totalResults, None)
    except Exception as e:
        print "Database exception on select", e
        logging.error(e)
        # Re-raise the last exception
        raise
      
def searchTwitterFollowers(dataset_pk, delete=False):
    logging.info('searchTwitterFollowers')
    try:
        if dataset_pk:
            # search for the followers. Exclude verified (high profile) users.
            query= '''select c.dataset_pk, c.twitter_profile_pk, t.screen_Name, t.follower_count, t.following_count 
            from twitter_profiles t, twitter_candidates c 
            where t.twitter_profile_pk = c.twitter_profile_pk
            and verified="FALSE"
            and c.dataset_pk = %s
            '''
            #print query
            cursor.execute(query,(dataset_pk))
            all_rows = cursor.fetchall()
            for row in all_rows:
                # initialize query parameters for Twitter API
                pk = row[0]
                twitter_profile_pk = row[1]
                screen_name = row[2]
                follower_count = row[3]

                try:
                    if delete:
                        # Delete any old records associated with this record in the dataset
                        query = "delete from twitter_followers where twitter_profile_pk = %s"
                        # execute the query
                        cursor.execute(query, (twitter_profile_pk,))
                        print "Twitter Followers Rows deleted:", cursor.rowcount
                        delete=False

                        # accept the change
                        conn.commit()
                # Catch the database exception
                except Exception as e:
                    print "Database exception on delete", e

                twitterName = screen_name.encode("utf-8")
                print "Twitter screen name is: ", twitterName
                # Searching Twitter with an actual screen name should only match one row
                totalResults=follower_count
                if totalResults > 0:
                    getTwitterFollowers(dataset_pk, twitter_profile_pk, twitterName, totalResults, None)
    except Exception as e:
        print "Database exception on select", e
        # Re-raise the last exception
        raise

def getTwitterUsers(dataset_pk, username, numItems, alt_name_pk):
    logging.info('getTwitterUsers')  
    try:
        # first set up authenticated API instance
        #auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        #auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
        #create an instance of a tweepy StreamListener to handle the incoming data
        #api = tweepy.API(auth, api_root='/1.1')
        
        api=loginTwitter()
        counter = 0
        remaining_hits = api.rate_limit_status('application')['resources']['application']['/application/rate_limit_status']['remaining']
        if (remaining_hits < 3):# or counter % 160 == 0:
            print '\n' 
            print 'You have', remaining_hits, 'API calls remaining in this window. Started sleeping at', time.ctime() 
            time.sleep(FIFTEEN_MIN)

        # Twitter API will only return 1000 items
        TwitterItems = min(int(ITEM_LIMIT), int(numItems))
        print "Requested: ", numItems, "Searching Twitter for: ", TwitterItems
        userItems = tweepy.Cursor(api.search_users, q=username).items(TwitterItems)
        for user in userItems:
                counter = counter + 1
                print user.name.encode("utf-8"), user.screen_name.encode("utf-8"), user.description.encode("utf-8"), user.location
                print user.url, user.profile_image_url, str(user.protected), user.followers_count, user.friends_count, str(user.verified)
                print "\n"

                try:
                    # does this Twitter profile already exist in the table?
                    query="select twitter_profile_pk from twitter_profiles where screen_name = %s"
                    cursor.execute(query,(user.screen_name))
                    row = cursor.fetchone()
                    if row is not None:
                        twitter_profile_pk =row[0]
                    else:
                        # Existing record not found. So we create a new one
                        # Insert the new profile
                        query = '''insert into twitter_profiles 
                        (username, screen_name, bio, location, url, 
                        protected, profile_image_url, follower_count, following_count, verified, alt_name_pk) 
                        values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                        # execute the query
                        cursor.execute(query, (user.name.encode("utf-8"), 
                                               user.screen_name.encode("utf-8"), 
                                               user.description.encode("utf-8"), 
                                               user.location, user.url, 
                                               str(user.protected), user.profile_image_url, 
                                               user.followers_count, user.friends_count,
                                               str(user.verified), alt_name_pk))
                        # Insert the new candidate
                        twitter_profile_pk = cursor.lastrowid
                    # Ignore duplicates if the primary key is already in the table
                    query = "insert ignore into twitter_candidates(twitter_profile_pk, dataset_pk, position_no) values ( %s, %s, %s)"
                    # execute the query
                    cursor.execute(query, (twitter_profile_pk, dataset_pk, counter))
                    final_url="http://www.twitter.com/" + user.screen_name.encode("utf-8")
                    # archive a copy of the web page
                    saveWebPage(user.screen_name.encode("utf-8"), 'twitter', final_url)
                    # accept the change
                    conn.commit()
                # Catch the database exception
                except Exception as e:
                    print "Database exception", e

            
                # Returns the remaining number of API requests available to the requesting user
                # before the API limit of 180 requests every 15 minutes
                # Calls to rate_limit_status do not count against the rate limit.
                remaining_hits = api.rate_limit_status('application')['resources']['application']['/application/rate_limit_status']['remaining']
           
                if (remaining_hits < 2):# or counter % 160 == 0:
                    print '\n' 
                    print 'You have', remaining_hits, 'API calls remaining in this window. Started sleeping at', time.ctime() 
                    time.sleep(FIFTEEN_MIN)
                else:
                    pass
                
        remaining_hits = api.rate_limit_status('application')['resources']['application']['/application/rate_limit_status']['remaining']
        print '\n'
        print 'You have', remaining_hits, 'API calls remaining in this window.', time.ctime()

    except tweepy.error.TweepError as e:
        print e.reason
        # Re-raise the last exception
        raise

def getTwitterFollowers(dataset_pk, twitter_profile_pk, username, numItems, alt_name_pk):
    logging.info('getTwitterFollowers')
    try:
        '''
        # first set up authenticated API instance
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
        #create an instance of a tweepy StreamListener to handle the incoming data
        api = tweepy.API(auth, api_root='/1.1')
        '''

        api=loginTwitter()

        counter = 0
        remaining_hits=api.rate_limit_status('application')['resources']['application']['/application/rate_limit_status']['remaining']
        if remaining_hits == 0:
            print '\n' 
            print 'You have', remaining_hits, 'API calls remaining in this window. Started sleeping at', time.ctime() 
            time.sleep(FIFTEEN_MIN)

        # Twitter API will only return 1000 items
        TwitterItems = min(int(ITEM_LIMIT), int(numItems))
        logging.info("User %s %s %s %s %s ", username, "Requested followers: ", numItems, "Searching Twitter for: ", TwitterItems)

        userItems = tweepy.Cursor(api.followers, screen_name=username, monitor_rate_limit=True, wait_on_rate_limit=True, wait_on_rate_limit_notify=True).items(TwitterItems)
        while True:
            try:
                user = userItems.next()
                counter = counter + 1
                print user.name.encode("utf-8"), user.screen_name.encode("utf-8"), user.description.encode("utf-8"), user.location.encode("utf-8")
                print user.url, user.profile_image_url, str(user.protected), user.followers_count, user.friends_count, str(user.verified)
                print "\n"

                try:
                    # does this Twitter followers profile already exist in the table?
                    query="select twitter_profile_pk from twitter_profiles where screen_name = %s"
                    cursor.execute(query,(user.screen_name))
                    row = cursor.fetchone()
                    if row is not None:
                        follower_twitter_profile_pk =row[0]
                    else:
                        # Existing record not found. So we create a new one
                        # Insert the new profile
                        query = '''insert into twitter_profiles 
                        (username, screen_name, bio, location, url, 
                        protected, profile_image_url, follower_count, following_count, verified, alt_name_pk) 
                        values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                        # execute the query
                        cursor.execute(query, (user.name.encode("utf-8"), 
                                               user.screen_name.encode("utf-8"), 
                                               user.description.encode("utf-8"), 
                                               user.location.encode("utf-8"), 
                                               user.url, 
                                               str(user.protected), user.profile_image_url, 
                                               user.followers_count, user.friends_count,
                                               str(user.verified), alt_name_pk))
                        # Insert the new candidate
                        follower_twitter_profile_pk = cursor.lastrowid
                    # Ignore duplicates if the primary key is already in the table
                    query = "insert ignore into twitter_followers(twitter_profile_pk, follower_twitter_profile_pk, position_no) values ( %s, %s, %s)"
                    # execute the query
                    cursor.execute(query, (twitter_profile_pk, follower_twitter_profile_pk, counter))
                
                    # accept the change
                    conn.commit()
                # Catch the database exception
                except Exception as e:
                    logging.error( "Database exception %s", e)

            
                # Returns the remaining number of API requests available to the requesting user
                # before the API limit of 180 requests every 15 minutes
                # Calls to rate_limit_status do not count against the rate limit.
                remaining_hits = api.rate_limit_status('application')['resources']['application']['/application/rate_limit_status']['remaining']
           
                if (remaining_hits < 2):# or counter % 160 == 0:
                    print '\n' 
                    print 'You have', remaining_hits, 'API calls remaining in this window. Started sleeping at', time.ctime() 
                    time.sleep(FIFTEEN_MIN)
                else:
                    pass
            
            except tweepy.error.TweepError as e:
                remaining_hits = api.rate_limit_status('application')['resources']['application']['/application/rate_limit_status']['remaining']
                print '\n'
                print 'You have', remaining_hits, 'API calls remaining in this window.', time.ctime()
                logging.error('Tweepy Error (a) %s', e.reason)
                logging.info('You have %s %s %s', remaining_hits, 'API calls remaining in this window.', time.ctime())
                userItems.next() 
            except StopIteration:
                break

        remaining_hits = api.rate_limit_status('application')['resources']['application']['/application/rate_limit_status']['remaining']
        print '\n'
        print 'You have', remaining_hits, 'API calls remaining in this window.', time.ctime()

    except tweepy.error.TweepError as e:
        logging.error("Tweepy error %s",  e.reason)
        print "Tweepy error before loop initiated %s", e.reason
        # Re-raise the last exception
        raise

def searchTwitterFollowing(dataset_pk, delete=False):
    logging.info('searchTwitterFollowing')
    try:
        if dataset_pk:
            # search for the followers. Exclude verified (high profile) accounts
            query= '''select c.dataset_pk, c.twitter_profile_pk, t.screen_Name, t.following_count 
            from twitter_profiles t, twitter_candidates c 
            where t.twitter_profile_pk = c.twitter_profile_pk
            and verified="FALSE"
            and c.dataset_pk = %s
             '''
            #print query
            cursor.execute(query,(dataset_pk))
            all_rows = cursor.fetchall()
            for row in all_rows:
                # initialize query parameters for Twitter API
                pk = row[0]
                twitter_profile_pk = row[1]
                screen_name = row[2]
                following_count = row[3]

                try:
                    if delete:
                        # Delete any old records associated with this record in the dataset
                        query = "delete from twitter_following where twitter_profile_pk = %s"
                        # execute the query
                        cursor.execute(query, (twitter_profile_pk,))
                        logging.debug("Twitter Following Rows deleted: %s", str(cursor.rowcount))
                        delete=False

                        # accept the change
                        conn.commit()
                # Catch the database exception
                except Exception as e:
                    logging.error("Database exception on delete %s", e)

                twitterName = screen_name.encode("utf-8")
                logging.debug("Twitter screen name is: %s", twitterName)

                # Searching Twitter with an actual screen name should only match one row
                totalResults=following_count
                if totalResults > 0:
                    getTwitterFollowing(dataset_pk, twitter_profile_pk, twitterName, totalResults, None)
    except Exception as e:
        logging.error("Database exception on select %s", e)
        # Re-raise the last exception
        raise
      
def getTwitterFollowing(dataset_pk, twitter_profile_pk, username, numItems, alt_name_pk):
    logging.info('getTwitterFollowing')
    try:
        '''
        # first set up authenticated API instance
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
        #create an instance of a tweepy StreamListener to handle the incoming data
        api = tweepy.API(auth, api_root='/1.1')
        '''
        
        api = loginTwitter()
        counter = 0
        remaining_hits=api.rate_limit_status('application')['resources']['application']['/application/rate_limit_status']['remaining']
        if remaining_hits == 0:
            print '\n' 
            print 'You have', remaining_hits, 'API calls remaining in this window. Started sleeping at', time.ctime() 
            time.sleep(FIFTEEN_MIN)

         # Twitter API will only return 1000 items
        TwitterItems = min(int(ITEM_LIMIT), int(numItems))
        logging.info("User %s %s %s %s %s",  username, "Requested friends/following: ", str(numItems), "Searching Twitter for: ", str(TwitterItems))
       
        userItems = tweepy.Cursor(api.friends, screen_name=username, monitor_rate_limit=True, wait_on_rate_limit=True, wait_on_rate_limit_notify=True).items(TwitterItems)
        for user in userItems:
            try:
                counter = counter + 1
                print user.name.encode("utf-8"), user.screen_name.encode("utf-8"), user.description.encode("utf-8"), user.location.encode("utf-8")
                print user.url, user.profile_image_url, str(user.protected), user.followers_count, user.friends_count, str(user.verified)
                print "\n"

                try:
                    # does this Twitter profile already exist in the table?
                    query="select twitter_profile_pk from twitter_profiles where screen_name = %s"
                    cursor.execute(query,(user.screen_name))
                    row = cursor.fetchone()
                    if row is not None:
                        following_twitter_profile_pk =row[0]
                    else:
                        # Existing record not found. So we create a new one
                        # Insert the new profile
                        query = '''insert into twitter_profiles 
                        (username, screen_name, bio, location, url, 
                        protected, profile_image_url, follower_count, following_count, verified, alt_name_pk) 
                        values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                        # execute the query
                        cursor.execute(query, (user.name.encode("utf-8"), 
                                               user.screen_name.encode("utf-8"), 
                                               user.description.encode("utf-8"), 
                                               user.location.encode("utf-8"), 
                                               user.url, 
                                               str(user.protected), user.profile_image_url, 
                                               user.followers_count, user.friends_count,
                                               str(user.verified), alt_name_pk))
                        # Insert the new candidate
                        following_twitter_profile_pk = cursor.lastrowid
                    # Ignore duplicates if the primary key is already in the table
                    query = "insert ignore into twitter_following (twitter_profile_pk, following_twitter_profile_pk, position_no) values ( %s, %s, %s)"
                    # execute the query
                    cursor.execute(query, (twitter_profile_pk, following_twitter_profile_pk, counter))
                
                    # accept the change
                    conn.commit()
                # Catch the database exception
                except Exception as e:
                    logging.error( "Database exception %s", e)
            
                # Returns the remaining number of API requests available to the requesting user
                # before the API limit of 180 requests every 15 minutes
                # Calls to rate_limit_status do not count against the rate limit.
                remaining_hits = api.rate_limit_status('application')['resources']['application']['/application/rate_limit_status']['remaining']
           
                if (remaining_hits < 2):# or counter % 160 == 0:
                    print '\n' 
                    print 'You have', remaining_hits, 'API calls remaining in this window. Started sleeping at', time.ctime() 
                    logging.info ('You have %s %s %s', remaining_hits, 'API calls remaining in this window. Started sleeping at', time.ctime() )
                    time.sleep(FIFTEEN_MIN)
                else:
                    pass
        
            except tweepy.error.TweepError as e:
                remaining_hits = api.rate_limit_status('application')['resources']['application']['/application/rate_limit_status']['remaining']
                print '\n'
                print 'You have', remaining_hits, 'API calls remaining in this window.', time.ctime()
                logging.error('Tweepy Error (a) %s', e.reason)
                logging.info('You have %s %s %s', remaining_hits, 'API calls remaining in this window.', time.ctime())
                userItems.next()

    except tweepy.error.TweepError as e:
        logging.error('Tweepy Error (b) %s', e.reason)
        # Re-raise the last exception
        raise
      
def getLinkedinScreenName():
    logging.info('getLinkedinScreenName')
    try:
        query='''update research.linkedin 
        set screen_name = replace(url_pub,'https://www.linkedin.com/in/','')
        where url_pub like '%linkedin.com/in%'
        '''
        cursor.execute(query)
        print "LinkedIn Screen Name updated for: ", cursor.rowcount, "rows"
        # accept the change
        conn.commit()

    # Catch the database exception
    except Exception as e:
        print "Database exception", e
        logging.error(e.reason)
        raise


def selectPerson():
    logging.info('selectPerson')
    choice=None
    try:
        # Query for the list of people we want to find in the (T)raining set
        cursor.execute('''SELECT dataset_pk, first_name, last_name FROM people where record_type= 'T'
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
            last_name  = row[2].lower()
            print dataset_pk, first_name, last_name
        choice = raw_input(" Enter a number>>  ")

        logging.info('Selected dataset key %s ', choice)

    # Catch the exception
    except Exception as e:
        print e
        logging.error(e)
        # Re-raise the last exception
        raise
      
    # Return menu selection to the main program
    return choice

def linkedinEditDistance(dataset_pk):
   logging.info('linkedinEditDistance')
   try:
     # start with people
      query= '''SELECT 
              concat(first_name, last_name), full_name, c.linkedin_pk
              FROM research.linkedin l,
              linkedin_candidates c,
              people d
              where l.linkedin_pk = c.linkedin_pk
              and c.dataset_pk = d.dataset_pk
              and c.dataset_pk = %s '''
      cursor.execute(query,(dataset_pk))
      all_rows = cursor.fetchall()
      
      for row in all_rows:
          distance = None
          source = row[0]
          source = source.translate(None, SPECIAL_CHARACTERS)
          # full name can contain special characters (period, comma, dash, apostrophe)
          destination = row[1]
          destination = destination.translate(None, SPECIAL_CHARACTERS)
          linkedin_pk = row[2]

          distance= nltk.metrics.edit_distance(source.lower(), destination.lower())
          print source, destination, distance
          if distance is not None:
            try:
                query='''update research.linkedin set edit_distance = %s where linkedin_pk = %s'''
                cursor.execute(query, (distance, linkedin_pk))
                print "LinkedIn Screen Name updated for: ", cursor.rowcount, "rows"
                # accept the change
                conn.commit()

            # Catch the database exception
            except Exception as e:
              print "Database exception", e
              logging.error(e)
   
   # Catch the exception
   except Exception as e:
       print e
       logging.error(e)
       # Re-raise the last exception
       raise
      
def twitterEditDistance(dataset_pk):
   logging.info('twitterEditDistance')
   try:
     # start with people
      query= '''SELECT 
              concat(first_name, last_name), username, c.twitter_profile_pk
              FROM research.twitter_profiles t,
              twitter_candidates c,
              people d
              where t.twitter_profile_pk = c.twitter_profile_pk
              and c.dataset_pk = d.dataset_pk
              and c.dataset_pk = %s '''
      cursor.execute(query,(dataset_pk))
      all_rows = cursor.fetchall()
      
      for row in all_rows:
          distance = None
          source = row[0]
          source = source.translate(None, SPECIAL_CHARACTERS)
          # full name can contain special characters (period, comma, dash, apostrophe)
          destination = row[1]
          destination = destination.translate(None, SPECIAL_CHARACTERS)
          twitter_profile_pk = row[2]

          distance= nltk.metrics.edit_distance(source.lower(), destination.lower())
          print source, destination, distance
          if distance is not None:
            try:
                query='''update research.twitter_profiles set edit_distance = %s where twitter_profile_pk = %s'''
                cursor.execute(query, (distance, twitter_profile_pk))
                print "Twitter Screen Name updated for: ", cursor.rowcount, "rows"
                # accept the change
                conn.commit()

            # Catch the database exception
            except Exception as e:
              print "Database exception", e
              logging.error(e)
   
   # Catch the exception
   except Exception as e:
       print e
       logging.error(e)
       #' Re-raise the last exception
       raise
      
def loadNeo():
     pass

def egoGraph(dataset_pk):
    g = nx.Graph()

    try:
        # start with people
        query= '''select dataset_pk, first_name, last_name from people where dataset_pk = %s '''
        cursor.execute(query,(dataset_pk))
        all_rows = cursor.fetchall()
        for row in all_rows:
            dataset_pk = row[0]
            first_name = row[1]
            last_name = row[2]
            fullname = blank.join([first_name, last_name])
            g.add_node(dataset_pk, name=fullname, color='#fcff00')    
    
        # draw the graph
        print g.nodes()
        plt.figure(figsize=(4,4))     
        nx.draw(g)


    # Catch the exception
    except Exception as e:
        print e
        logging.error(e)
        # Re-raise the last exception
        raise

##########################################################################             
#  This is main procedure in this package
############################################################################
def main(load=False):
    urllib3.disable_warnings()

    '''
    C:\Python27\lib\site-packages\requests\packages\urllib3\util\ssl_.py:79: InsecurePlatformWarning: 
    A true SSLContext object is not available. 
    This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. 
    For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
    InsecurePlatformWarning
     '''

    logging.info('\n=====================================================================')
    logging.info('Started processing at: %s', time.ctime() )

    try:
        #1 Open a database connection
        openConnection()
        global cursor
        cursor = conn.cursor()

        #2. Load the nicknames into the database
        if load:
            loadNickNames()

        #3. Select a training record to process
        dataset_pk = selectPerson()

        if dataset_pk:
            logging.info('Processing key# %s', dataset_pk)
            
            #4. Construct alternative names using nickname variations
            readSeedDB(dataset_pk)

            #5. Google Search for public profiles on LinkedIn
            searchGoogleCSE(dataset_pk)

            #6. Yahoo Search for undiscovered public profiles on LinkedIn
            #searchYahoo(dataset_pk)
   
            #6a Update potential screen names from LinkedIn
            getLinkedinScreenName()
             
            #7. Retrieve public profiles to get educational affiliation(s)
            linkedInAffiliation(dataset_pk)

            #8. Create 1st, 2nd, 3rd degree connections from LinkedIn "people also viewed"
            # on the public profile page
            peopleAlsoViewed(dataset_pk, degree = 1)
            peopleAlsoViewed(dataset_pk, degree = 2)
            peopleAlsoViewed(dataset_pk, degree = 3)


            #9a. Search for Twitter profiles with cleanup of old data
            searchTwitterUsers(dataset_pk, delete=True)

            
            #9b. Use derivatives, nicknames and the vanity URL from linkedin to derive a potential screen name
            searchTwitterFollowers(dataset_pk, delete=True)
            
            # Re-process a particular screen name
            #getTwitterFollowers(2,229,'Chelseaa_Kelley',1000,None)
            
            #11. Twitter following
            searchTwitterFollowing(dataset_pk, delete=True)

            #12. Apply the scoring model to the candidate entities
            '''
            linkedinEditDistance(dataset_pk)
            twitterEditDistance(dataset_pk)        
            scoreCandidates(dataset_pk)
            scoreTwitter (dataset_pk)
            '''
            #13 prune edges that don't meet filter condition. Load into Neo4j
            #loadNeo ()            

            #14. Graph visualization
            #egoGraph (dataset_pk)  
                        
        # Close the mySQL connection normally
        if conn.open:
            closeConnection()

            
        logging.info('Completed processing at: %s', time.ctime() )

    except Exception as e:
      logging.error('Main: Abnormal termination %s', e)
    finally:
      # Close the database connection
       if conn.open :
         closeConnection()


if __name__ == '__main__':
    #mainMenu.main_menu()
    # Re-set the log files for this run
    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
    logging.basicConfig(
        filename='./logs/access-log.'+ now, 
        filemode='w',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG)
    main(load=False)
          
    #saveWebPage('mark stevenson', 'twitter','http://www.twitter.com/msteve27')
