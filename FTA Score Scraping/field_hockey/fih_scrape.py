from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('https://tms.fih.ch/competitions?view=all').text  # decomment to use live website
# with open('espn.html') as source:
soup = BeautifulSoup(source, 'lxml')  # remove tab amd line above to use live website

# for table in soup.find_all('div', 'portlet-body'):
#    for link in table.find_all('a'):
#        print(link)

for i in range(1, 2):
    url = "https://tms.fih.ch/competitions?view=all&page=%s" % i
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for table in soup.find_all('table'):
        for col in table.find_all('td'):
            for link in col.find_all('a'):
                print(link)
