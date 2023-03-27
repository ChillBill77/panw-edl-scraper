# Import required modules
import datetime
from lxml import html
import requests
import random

# Request the page
page = requests.get('https://docs.paloaltonetworks.com/resources/edl-hosting-service')
 
# Request the page
#page = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')
 
# Parsing the page
tree = html.fromstring(page.content)

# Get element using XPath
url = tree.xpath('//*[@id]/div/div/table/tbody/tr[1]/td[2]/p[1]/a/text()')
description = tree.xpath('//*[@id]/div/div/table/tbody/tr[1]/td[2]/p[2]/text()')

#Convert to list for group naming
naming = list(url)
grp_naming = [w.replace('https://saasedl.paloaltonetworks.com/feeds','GRP').replace('/','_').replace('-','_') for w in naming]

#Nicer output with easy grep and random hours to prevent overload
for g,q,a in zip (grp_naming, url, description):
    result = str({1}).format(g,q,a).find('ipv4',1)
    if result > 1:
       print('{0}:\n-URL: {1} \n-Description: {2}\n-set_command:\n set external-list "{0}" type ip description "{2}" url {1} recurring daily at '.format(g,q,a), random.randrange(0, 23, 1))
    else:
       print('{0}:\n-URL: {1} \n-Description: {2}\n-set_command:\n set external-list "{0}" type url description "{2}" url {1} recurring daily at '.format(g,q,a), random.randrange(0, 23, 1))