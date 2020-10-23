#  Python quickquery - run the setup and load JIRA.
#  Generally intending to run and then drop to the interpreter via "python -i quickquery.py"
import getpass
import pprint
from jira import JIRA


servername = "https://nhjira.nanthealth.com"
username = 'kbennett'
#username = 'set-me-to-a-name'
#mvf_id = '1702'
# wb = Workbook()
# wb.save('SparkDay7Stories.xlsx')

def getauth ( username ):
    print('Enter JIRA password for ' + username)
    pw = getpass.getpass("JIRA password:")
    return pw

def getmvfstories ( mvf_id ):
    stories = jira.search_issues('project= NNO AND issuetype in (Bug,Story,Task) AND \'MVF ID\' =' + mvf_id)
    esr = jira.search_issues('project= ESR AND issuetype in (Bug, Story, Task) AND \'MVF ID\' =' + mvf_id)
    for key in stories:
        issue = jira.issue(key)
        print(key)
        print(issue.fields.customfield_10633)
        print(issue.fields.resolutiondate)
    for key in esr:
        print(key)
        print(issue.fields.customfield_10633)
        print(issue.fields.resolutiondate)



# Don't encode passwords in Git anything :)
password = getauth(username)

jira = JIRA(server=servername, basic_auth=(username,password))
	

# ################################################
# # Grab all the JIRIA custom field names
# # ------------------------------------------------
# resp=jira.fields()
# fmap = {}
# for i in resp:
#     field_name=i[u'name']
#     field_id=i[u'id']
#     fmap[field_name]=field_id
#     #print (i['name'])
# pprint.pprint(fmap)

getmvfstories('1702')


