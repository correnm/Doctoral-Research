'''
@Author Corren McCoy, 2014
@Purpose Entity Resolution of known community with online social network
'''

__author__ = 'cmccoy@cs.odu.edu (Corren McCoy)'

from xgoogle.search import GoogleSearch, SearchError
from apiclient.discovery import build
from BeautifulSoup import BeautifulSoup
from ConfigParser import SafeConfigParser
from collections import defaultdict
import mainMenu

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


# blank space
blank=" "
lang="en"
wildcard="*"
termsep="+"
conjunction="+"

# define the empty dictionary
dataset = defaultdict(list)
linkedin_affiliation = defaultdict(list)
linkedin_pav = defaultdict(list)


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





def stripHtmlTags (htmlTxt):
    if htmlTxt is None:
        return None
    else:
        return ''.join(BeautifulSoup(htmlTxt).findAll(text=True))
      
        
def readSeedDB(param_dataset_pk=None):

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


            # Add any nicknames and inverse given names to the dataset (e.g., Joe <--> Joseph)
            cursor.execute('''SELECT nickname
            from nicknames n,
            given_names g
            where g.name_pk = n.name_pk
            and lower(first_name) = %s
            UNION select first_name
            from nicknames n,
            given_names g
            where g.name_pk = n.name_pk
            and lower(nickname) = %s ''', (first_name, first_name ))
            
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
              # to get an API key for your own application.
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
                      print "URL", url
                      location = res.get('pagemap',{}).get('person')[0].get('location')
                      print "Location", location
                      
                      # add each result to the table
                      query="insert into linkedin (title, location, url_pub, full_name, search_engine, alt_name_pk) values (%s, %s, %s, %s, %s, %s)"
                      cursor.execute(query,(title, location, url, resultFullname, searchEngine, alt_name_pk))

                      linkedin_pk = cursor.lastrowid
                      query="insert into linkedin_candidates (dataset_pk, linkedin_pk, position_no) values (%s, %s, %s)"
                      cursor.execute(query,(pk, linkedin_pk, position))
                      conn.commit()

                  nextPage=response.get('queries').get('nextPage')[0].get('startIndex')
                  startPage = nextPage
                  print "next", nextPage
              
                  response = service.cse().list(
                  q=searchString,
                  cx="013993674550209950690:ptr-mn8l7h0",
                  start=startPage
                  ).execute()


              # Catch the Google exception
              except SearchError, e:
                 print "Search failed: %s" % e              
              except Exception, e:
                 print "Google Custom Search failed: %s" % e
        except SearchError, e:
            print "Search failed: %s" % e              
        except Exception, e:
            print "Google Custom Search failed: %s" % e

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
    # Catch the database exception
    except Exception as e:
      print e
 


def peopleAlsoViewed(dataset_pk, degree):

    try:
        # For first degree, get the "people also viewed" from the original profile page
        if degree == 1:
            cursor.execute('''SELECT l.linkedin_pk, l.url_pub, null 
            FROM linkedin l,
            linkedin_candidates d
            where l.linkedin_pk = d.linkedin_pk
            and d.dataset_pk = %s ''' , (dataset_pk,))
        elif degree == 2:
            cursor.execute('''SELECT l.linkedin_pk, l.url_pub, p.pav_pk 
            FROM linkedin_pav p, 
            linkedin l,
            linkedin_candidates d 
            where p.linkedin_pk = l.linkedin_pk 
            and l.linkedin_pk = d.linkedin_pk
            and d.dataset_pk = %s and degree = 1 ''', (dataset_pk,))
        elif degree == 3:
             cursor.execute('''SELECT l.linkedin_pk, l.url_pub, p.pav_pk 
            FROM linkedin_pav p, 
            linkedin l,
            linkedin_candidates d 
            where p.linkedin_pk = l.linkedin_pk 
            and l.linkedin_pk = d.linkedin_pk
            and d.dataset_pk = %s and degree = 2 ''', (dataset_pk,))
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
          pav_pk = row[2]
          # search for each person's public profile on LinkedIn
          #for pk, value in linkedin_pav.items():
          url = str(value).strip('[]')
          url = url.strip('\'"')
          url = url.encode("utf-8")
          print pk, url, pav_pk 
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
            #url=url.encode('utf8')
            request=urllib2.Request(url)
            # Understanding the user agent string (http://msdn.microsoft.com/en-us/library/ms537503(VS.85).aspx)
            randomUserAgent=random.choice(BROWSERS)
            #print randomUserAgent
            request.add_header('User-agent', randomUserAgent)
            response=urllib2.urlopen(request)
            print "response" , response.code
            if response.code == 200:
                html=response.read()
                # decode byte stream to unicode
                html = html.decode("utf-8")
                # encode to ASCII byte stream, removing characters with codes >127
                html = html.encode("ascii", "ignore") 
                soup = BeautifulSoup(html)
                #DEBUG: show the html of the retrieved page
                #print soup
                peopleAlsoViewed= soup.html.body.find('div',{'class' : 'insights-browse-map'})
                #print peopleAlsoViewed
                if peopleAlsoViewed:
                    for temp in peopleAlsoViewed.findAll('li'):
                      photo = temp.find('img', {'class' : ''})['src']
                      print "Photo: ", photo
                      h4 = temp.find('h4')
                      temp_url = h4.find('a')
                      #print "temp:", temp_url
                      url = temp_url['href'].strip('?trk=pub-pbmap')
                      print "URL: ", url
                      fullname =temp_url.contents[0]
                      print "Full name", fullname
                      profileTitle = temp.find('p',{'class': 'browse-map-title'}).string
                      print "Title", profileTitle
                      try:
                        # Have we already seen this profile?
                        query='''select linkedin_pk from linkedin where url_pub = %s'''
                        cursor.execute(query, (url,))
                        link_row= cursor.fetchone()
                        if link_row:
                            pk = link_row[0]
                        else:
                            # New one. Add to table. Save the key
                            query="insert into linkedin (url_pub, full_name, title, profile_image_url) values (%s, %s, %s, %s)"
                            cursor.execute(query,(url, fullname, profileTitle, photo,))
                            pk = cursor.rowid

                        
                            query="insert into linkedin_pav (linkedin_pk, url, full_name, title, degree, parent_pav_pk) values (%s, %s, %s, %s, %s, %s)"
                        cursor.execute(query,(pk, url, fullname, profileTitle, degree, pav_pk,))
                        conn.commit()
                      except Exception as e:
                        print "Error while inserting linkedin_pav", e
            print              
            response.close()
          except Exception as e:
            print e
    # Catch the database exception
    except ValueError as e:
      print e
    except Exception as e:
      print e
    # Close the mySQL connection normally
    if conn.open:
        closeConnection()


# Load nicknames from csv file compiled by Carlton Northern
# http://code.google.com/p/nickname-and-diminutive-names-lookup/
def loadNickNames(filename=None):
#    openConnection()
#    cursor = conn.cursor()

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

    cursor.close()
#    closeConnection()

def searchTwitterUsers(dataset_pk=None):
    x = 1
      
   
def selectPerson():
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

    # Catch the exception
    except Exception as e:
        print e
 
    return choice
 
############################################################################             
#  This is main procedure in this package
############################################################################
def main(load=False):

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
            print "Processing key#", dataset_pk

            #4. Construct alternative names using nickname variations
            #readSeedDB(dataset_pk)

            #5. Google Search for public profiles on LinkedIn
            #searchGoogleCSE(dataset_pk)

            #6. Yahoo Search for undiscovered public profiles on LinkedIn
            #searchYahoo(dataset_pk)
    
            #7. Retrieve public profiles to get educational affiliation(s)
            #linkedInAffiliation(dataset_pk)

            #8. Create 1st, 2nd, 3rd degree connections from LinkedIn "people also viewed"
            # on the public profile page
            peopleAlsoViewed(dataset_pk, degree = 1)
            #peopleAlsoViewed(dataset_pk, degree = 2)
            #peopleAlsoViewed(dataset_pk, degree = 3)


            #9. Search for Twitter profiles
            #searchTwitterUsers(dataset_pk=None)

            #10. Twitter followers

            #11. Twitter following

            #12. Apply the scoring model

            #13. Graph visualization
             

        # Close the mySQL connection normally
        if conn.open:
            closeConnection()

    except ValueError as e:
      print e
    except Exception as e:
      print e
            
if __name__ == '__main__':
    #mainMenu.main_menu()
    main(load=False)