from collections import Counter
from jira import JIRA
import getpass

options = {"server": "https://nhjira.nanthealth.com/"}
username = 'xxxx'


jira = JIRA(options=options, basic_auth=(username, "xxxx"))


issue = jira.issue('EBI-10436')

print(issue.fields.project.key)
print(issue.fields.issuetype.name)
print(issue.fields.reporter.displayName)
print(issue.fields.c)
