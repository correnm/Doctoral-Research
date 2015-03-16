'''
@Author Corren McCoy, 2014
@Purpose
Use the Twitter APIs to extract:
(1) the followers (count) of a certain user including the followers of those entities
(2) the following (count) of a certain user including the number of accounts his followers
are following.
(3) the friends (count) of a certain user include the number friends associated with his followers
Note:  The Twitter API indicates that following is otherwise known as their "friends"

Example request:
https://api.twitter.com/1.1/followers/list.json?cursor=-1&screen_name=sitestreams&skip_status=true&include_user_entities=false

This code leverages tweepy (https://code.google.com/p/tweepy/) which is a Python API for twitter.
It provides a nice wrapper for the Twitter APIs
'''
import codecs
import MySQLdb
import tweepy
import time
import urllib

# Initialize the oAuth authentication settings
# Documentation: https://dev.twitter.com/docs/auth/oauth
CONSUMER_KEY = "LrA1DdH1QJ5cfS8gGaWp0A"
CONSUMER_SECRET = "9AX14EQBLjRjJM4ZHt2kNf0I4G77sKsYX1bEXQCW8"
OAUTH_TOKEN = "1862092890-FrKbhD7ngeJtTZFZwf2SMjOPwgsCToq2A451iWi"
OAUTH_SECRET = "AdMQmyfaxollI596G82FBipfSMhagv6hjlNKoLYjeg8"

# mySQL connection string
sqlHost    = "localhost"
sqlUser    = "research"
sqlPasswd  = "c0ree3n"
sqlDb      = "research"


# Dr. Nelson's twitter account
#USERNAME='phonedude_mln'
USERNAME='msteve27'
dataset_pk = 4999
query=USERNAME.encode("utf-8")
print query
# variables used to manage the API rate limit
FIFTEEN_MIN=900 # seconds
FIVE_MIN=300
ITEM_LIMIT=1000

# first set up authenticated API instance
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
#create an instance of a tweepy StreamListener to handle the incoming data
api = tweepy.API(auth, api_root='/1.1')

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

openConnection()
cursor = conn.cursor()
# open the output file that will contain the data for graphing in "R"
usersFile = codecs.open('./twitterUsersFile.txt','w','utf-8')
# write the header line for identification
usersFile.write("ID" + "," + "NAME" +"," + "USERNAME" +"," + "DESCRIPTION" +"," +"LOCATION")

try:
    counter = 0
    userItems = tweepy.Cursor(api.search_users, q=USERNAME).items(1)
    for user in userItems:
            counter = counter + 1
            print user.name, user.screen_name, user.description, user.location, user.url, user.profile_image_url, str(user.protected)
            usersFile.write('\n')
            usersFile.write(str(counter) +',' + user.name + ',' + user.screen_name +',' + user.description +',' + user.location + ',' + user.url)

            try:
                # Insert the new profile
                query = "insert into twitter_profiles(username, screen_name, bio, location, website) values ( %s, %s, %s, %s, %s)"
                # execute the query
                cursor.execute(query, (user.name, user.screen_name, user.description,user.location,user.url,))

                # Insert the new candidate
                twitter_profile_pk = cursor.lastrowid
                query = "insert into twitter_candidates(twitter_profile_pk, dataset_pk) values ( %s, %s)"
                # execute the query
                cursor.execute(query, (twitter_profile_pk, dataset_pk,))

                
                # accept the change
                conn.commit()
            # Catch the database exception
            except Exception as e:
                print "Database exception", e


            
            # Returns the remaining number of API requests available to the requesting user
            # before the API limit of 180 requests every 15 minutes
            # Calls to rate_limit_status do not count against the rate limit.
            remaining_hits = api.rate_limit_status('application')['resources']['application']['/application/rate_limit_status']['remaining']
           
            if (remaining_hits < 5):# or counter % 160 == 0:
                print '\n' 
                print 'You have', remaining_hits, 'API calls remaining in this window. Started sleeping at', time.ctime() 
                time.sleep(FIFTEEN_MIN)
            else:
                pass
           #if counter == ITEM_LIMIT:
           #     # terminate the for loop
           #     break
           
    usersFile.close()
    print '\n'
    print 'You have', remaining_hits, 'API calls remaining in this window.', time.ctime()

    # Close the db connection
    if conn.open :
       closeConnection()

   
except tweepy.error.TweepError as e:
    print e.reason
    followersFile.close()
