## Python quickquery - run the setup and load JIRA.
## Generally intending to run and then drop to the interpreter via "python -i quickquery.py"
import getpass
import pprint
from jira import JIRA

servername = "https://nhjira.nanthealth.com"
username = 'rswarbrick'
#username = 'set-me-to-a-name'

def getauth ( username ):
    print ('Enter JIRA password for ' + username)
    pw = getpass.getpass("JIRA password:")
    return pw


# Don't encode passwords in Git anything :)
password = getauth(username)

jira = JIRA(server=servername, basic_auth=(username,password))
	

## -------------------------------------------------
## Grab all the JIRIA custom field names
## ------------------------------------------------    
resp=jira.fields()
fmap = { }
for i in resp:
   field_name=i[u'name']
   field_id=i[u'id']
   fmap[field_name]=field_id
   #print (i['name'])
pprint.pprint(fmap)

