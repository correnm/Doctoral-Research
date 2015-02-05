from linkedin import linkedin # pip install python-linkedin
import json
from prettytable import PrettyTable # pip install prettytable

# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application

CONSUMER_KEY = '7732yrpro58l3g'
CONSUMER_SECRET = 'PxWgCNiylQyaDDMj'
USER_TOKEN = 'e414da88-d7ff-4b33-99d2-d63958f9a46c'
USER_SECRET = 'e3aecb07-346d-4f22-8b5d-f42c82bd4487'

RETURN_URL = 'http://localhost:8080' # Not required for developer authentication

# Instantiate the developer authentication class

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                USER_TOKEN, USER_SECRET, 
                                RETURN_URL, 
                                permissions=linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

app = linkedin.LinkedInApplication(auth)

# Use the app...

app.get_profile()

connections = app.get_connections()

connections_data = 'linkedin_connections.json'

f = open(connections_data, 'w')
f.write(json.dumps(connections, indent=1))
f.close()

# You can reuse the data without using the API later like this...
# connections = json.loads(open(connections_data).read())


pt = PrettyTable(field_names=['Name', 'Location', 'URL'])
pt.align = 'l'

[ pt.add_row((c['firstName'] + ' ' + c['lastName'], c['location']['name'], c['siteStandardProfileRequest']['url'])) 
  for c in connections['values']
      if c.has_key('location')]

pt_txt = pt.get_string()
with open('linkedin_connections.txt','w') as file:
    file.write(pt_txt)
print pt

## Info for someone in your network
connection_id= connections['values'][20]['id']
connection_positions = app.get_profile(member_id=connection_id, selectors=['public-profile-url','positions'])
print json.dumps(connection_positions, indent=1)
