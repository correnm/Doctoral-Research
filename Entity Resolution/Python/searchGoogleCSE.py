# Python libraries
from apiclient.discovery import build
from BeautifulSoup import BeautifulSoup
import collections
import csv
import logging
import MySQLdb
import os
import os.path
import random
import requests
import time
import urllib2
from xgoogle.search import GoogleSearch, SearchError

# my libraries
import manageMySQLDB
import saveWebPage

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
# blank space
blank=" "
lang="en"
wildcard="*"
termsep="+"
conjunction="+"
SPECIAL_CHARACTERS="1234567890!@#$%^&*()_+-={}[];':\"<>?,./ "

def author():
  """
  cmccoy@cs.odu.edu (Corren McCoy) @2015
  """
  
def help():
  """
  Google Custome Search Engine results for LinkedIn
  """
  print help.__doc__
  
def randomWait():
    # get a random number in this range (seconds)
    wait = random.uniform(2,5)
    time.sleep(wait)

 
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
        print response.code
        
        if response.code in (200, 301, 302, 303, 307):
            finalurl=response.geturl()
        else:
            finalurl=url
            
        if verbose:
            print "RESPONSE" , response.code
            print "START-URL", url
            print "FINAL-URL",finalurl
            print "ACTUAL", actualURL

            headers=response.info()
            print "DATE:", headers['date']
            print "HEADERS"
            print " -------------"
            print headers

    return finalurl
  
def scrapePage(url, format="source"):
  logging.info('Enter searchGoogleCSE.scrapePage')
  try:
    # Return in either raw view "source" format or as beautiful "soup"
    pageSource = None
    if url:
      #package the request
      url=url.encode('utf8')

      # Understanding the user agent string (http://msdn.microsoft.com/en-us/library/ms537503(VS.85).aspx)
      randomUserAgent=random.choice(BROWSERS)
      headers=dict()
      headers['User-Agent'] = randomUserAgent
    
      #print headers
      response=requests.get(url, headers=headers)
      if response.status_code == 200:
        html=response.text
        # decode byte stream to unicode
        #html = html.decode("utf-8","ignore")
        # encode to ASCII byte stream, removing characters with codes >127
        html = html.encode("ascii", "ignore") 
        soup = BeautifulSoup(html)

        if format == "soup":
          pageSource = soup
        else:
          pageSource = html
    else:
      # no URL passed
      pageSource = None
  except Exception as e:
    print e
    logging.error(e)
  logging.info('Exit searchGoogleCSE.scrapePage')  
  return pageSource

def linkedin(dataset_pk, delete=True, startPage=1):
    logging.info('Enter searchGoogleCSE.linkedin')
    
    manageMySQLDB.openConnection()
    cursor = manageMySQLDB.conn.cursor()
    searchEngine="Google"
    numResults=20
    totalResults=0 # CSE limit
    maxResults=100
    
    # search for each person's public profile on LinkedIn using primary key
    # Query for the list of people we want to find in the (T)raining set
    cursor.execute('''SELECT dataset_pk, first_name, ifnull(middle_name,''), last_name, alt_name_pk FROM people_alt_names where dataset_pk = %s ''', dataset_pk)
    all_rows = cursor.fetchall()
    for row in all_rows:
        # initialize query parameters for search engine
        pk = row[0]
        first = None
        middle= None
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
              manageMySQLDB.conn.commit()
        # Catch the database exception
        except Exception as e:
            print "Database exception", e
            logging.error("SearchGoogleCSE: Database exception %s", e)

        first  = row[1]
        middle = row[2]
        last   = row[3]
        alt_name_pk =  row[4]

        # use the middle name/init if it exists
        if middle:
          fullname = blank.join([blank.join([first, middle]), last])
          searchName = termsep.join( [termsep.join([first, middle]) , last])
        else:
          fullname = blank.join([first, last])
          searchName = termsep.join([first, last])
          
      
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
                while (response is not None): 
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

                      # Get the page source returned in Beautiful Soup format CORREN
                      soup = scrapePage(final_url, "soup")
                      
                      topCard = soup.html.body.find('div',{'id' : 'top-card'})
                      profilePicture = topCard.find('div', {'class': 'profile-picture'})
                      profileImageTemp = profilePicture.find('img')['src']
                      profileImageURL = finalURL(profileImageTemp)
                      print "picture", profileImageURL

                      headlineTemp = topCard.find('div', {'id' : 'headline'})
                      headline = headlineTemp.find('p').text
                      print "headline", headline

                      industry=topCard.find('dd',{'class' : 'industry'}).text
                      print "industry", industry
                      # there can be up to three websites listed on a public profile
                      websites = topCard.find('tr', {'id': 'overview-summary-websites'})
                      
                      if websites:
                        for temp in websites.findAll('li'):
                          websiteURL=None
                          siteAnchor = temp.find('a')['href']
                          if siteAnchor:
                            websiteURL = finalURL(siteAnchor)
                            print "website", websiteURL
                            # TODO insert website into table
                            
                      schoolsAttended= soup.html.body.find('div',{'id' : 'background-education-container'})
                      print "schools", schoolsAttended
                      if schoolsAttended:
                          for temp in schoolsAttended.findAll('h4',{'class':'summary fn org'}):
                            education = temp.find('a',{'title':'More details for this school'})
                            if education:
                              universityName = education.string
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
                            
                            # does this profile already exist in the table (i.e., same publicURL)?
                            query="select linkedin_pk from linkedin where url_pub = %s"
                            cursor.execute(query,(final_url))
                            row = cursor.fetchone()
                            if row is not None:
                                # save the existing primary key to use later. @TODO Should we update with latest information?
                                linkedin_pk =row[0]
                                # update in case the information changed
                                
                            else:
                                # Existing record not found. So we create a new record with data scraped from the page.
                                query="insert into linkedin (title, location, url_pub, full_name, search_engine, alt_name_pk) values (%s, %s, %s, %s, %s, %s)"
                                cursor.execute(query,(title, location, final_url, resultFullname, searchEngine, alt_name_pk))
                                # get the primary key from new record
                                linkedin_pk = cursor.lastrowid
                            # save the insert or update statement
                            manageMySQLDB.conn.commit()
                               
                                
                            print "linkedin_pk %s " % linkedin_pk 
                            print "pk %s" % pk 
                            print "position %s" % position
                            query="insert ignore into linkedin_candidates (dataset_pk, linkedin_pk, position_no) values (%s, %s, %s)"
                            print query
                            
                            # archive the html for the web page
                            saveWebPage.toFile(resultFullname.replace(" ","_"), 'linkedin', final_url)
                            try:
                              # insert into linkedin_candidates. we will ignore duplicate keys
                              cursor.execute(query,(pk, linkedin_pk, position))
                              manageMySQLDB.conn.commit()
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
                 logging.error(e)
              except Exception, e:
                 print "(1) Google Custom Search failed: %s" % e
                 logging.error(e)
        except SearchError, e:
            print "(2) Search failed: %s" % e
            logging.error(e)
        except Exception, e:
            print "(2) Google Custom Search failed: %s" % e
            logging.error(e)

    # Close the mySQL connection normally
    if manageMySQLDB.conn.open:
      manageMySQLDB.closeConnection()
    logging.info('Exit searchGoogleCSE')
