from bs4 import BeautifulSoup
import requests
import csv
import re

# schedule_source = requests.get('https://eliteleague.co.uk/game-centre/schedule/?season_id=18470').text  # decomment to use live website
with open('templates/test.html') as source:
    soup = BeautifulSoup(source, 'lxml')  # remove tab amd line above to use live website

final_list = []
dates = soup.find_all('div', 'date')
for c in range(len(dates)):
    temp_list = []  # stores things
    temp_list.append(dates[c].text)  # grabs the date div
    meeting = soup.find_all('div', 'meeting')  # finds all meetings as a list
    meeting = BeautifulSoup(str(meeting[c]), 'html.parser')  # finds the position in the meetings list based off of the date position in the date list
    for name in meeting.find_all('span', 'name'):
        temp_list.append(name.text)
    final_list.append(temp_list)
print(final_list)
