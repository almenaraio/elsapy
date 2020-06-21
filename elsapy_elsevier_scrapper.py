# Scraping bibliographic information from Elsevier using elsapy
# https://dev.elsevier.com/

import os
import csv
import json
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch

# Set working directory
os.chdir('c:/temp')
    
## Load configuration file with your API Key within it:
con_file = open("config.json")
config = json.load(con_file)
con_file.close()

## Initialize client
client = ElsClient(config["apikey"])
# client.inst_token = config['insttoken'] # Use this instead in case you have an institutional token

# My list of ISSNs for scraping
f = open('journalslist.csv', 'r')

journalslist = csv.reader(f, delimiter=',')
jlist = list(journalslist)

# Let's check how many items do we have
print(len(jlist))

# There is an upper limit of 5000 records to retrieve
# The code below retrieves the data as a "dump.json" file
try:
    for i in range(len(jlist)):
        issn = jlist[i:][1]
        journal = ElsSearch('ISSN(' + str(issn[1]) + ')', 'scopus')
        try:
            journal.execute(client, get_all = True)
        except:
            pass
            print('Error')
        else:
            print ('A total of', len(journal.results), 'articles We retrieved from the journal: 
			' + str(issn[0]) + ', ISSN = ' + str(issn[1]))
except:
    pass
    print('List complete')

f.close
