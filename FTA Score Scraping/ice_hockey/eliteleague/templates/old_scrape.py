from bs4 import BeautifulSoup
import requests
import csv
import re

# schedule_source = requests.get('https://eliteleague.co.uk/game-centre/schedule/?season_id=18470').text  # decomment to use live website
with open('templates/schedule.html') as schedule_source:
    schedule_soup = BeautifulSoup(schedule_source, 'lxml')  # remove tab amd line above to use live website
dataList = []
for data in schedule_soup.find_all('section', 'container'):
    date = data.find_all('h2')
    dataList.append(date)
    homeTeam = data.find_all('span', 'home-team')
    homeTeam = homeTeam
    dataList.append(homeTeam)
    # print(homeTeam)
# print(dataList)

final_list = []
dates = schedule_soup.find_all('div', 'date-row')
for c in range(len(dates)):
    temp_list = []  # stores things
    home_list = []
    away_list = []
    score_list = []
    temp_list.append(dates[c].text.replace('\n', ''))  # grabs the date div
    matchGroup = schedule_soup.find_all('div', 'game-set')  # finds all meetings as a list
    matchGroup = BeautifulSoup(str(matchGroup[c]), 'html.parser')  # finds the position in the meetings list based off of the date position in the date list
    for home in matchGroup.find_all('span', 'home-team'):
        home_list.append(home.text)
    for away in matchGroup.find_all('span', 'away-team'):
        away_list.append(away.text)
    for score in matchGroup.find_all('span', 'score'):
        score_list.append(score.text)
    temp_list.append(home_list)
    temp_list.append(away_list)
    temp_list.append(score_list)
    final_list.append(temp_list)
print(final_list)
