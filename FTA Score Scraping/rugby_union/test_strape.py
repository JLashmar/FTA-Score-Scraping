from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('https://www.bbc.co.uk/sport/rugby-union/english-premiership/fixtures').text  # decomment to use live website
# with open('espn.html') as source:
soup = BeautifulSoup(source, 'lxml')  # remove tab amd line above to use live website

fixture_file = open('rfu_fixtures.csv', 'w', newline='')
fixture_writer = csv.writer(fixture_file)
fixture_writer.writerow(['id', 'match_date', 'home_team', 'away_team'])
# table
table_file = open('rfu_table.csv', 'w', newline='')
table_writer = csv.writer(table_file)
table_writer.writerow(
    ['id', 'position', 'team', 'played', 'win', 'loss', 'draw', 'points_for', 'points_against', 'points_difference',
     'try_bonus', 'loss_bonus', 'points']
)

# fixtures:
match_data = []
for comp in soup.find_all('div', {'id': 'rugby-match-list'}):
    for date in comp.find_all('h4'):
        date = date.text
        print(date.next_element)
    for data in comp.find_all('article'):
        team_list = []
        team_list.append(date)
        for home_team in data.find_all('abbr', {'data-role': 'home-team'}):
            home_team = home_team.text
            team_list.append(home_team)
        for away_team in data.find_all('abbr', {'data-role': 'away-team'}):
            away_team = away_team.text
            team_list.append(away_team)
        match_data.append(team_list)
# print(match_data)

fixture_file.close

# table
for data in soup.find_all('div', {'id': 'competitionstab-content3'}):
    id = 0
    for row in data.find_all('div', 'table_item'):
        id = id + 1
        team_row = []
        team_row.append(id)
        for data in row.find_all('li'):
            data = data.text
            team_row.append(data)
        table_writer.writerow(team_row)

table_file.close
