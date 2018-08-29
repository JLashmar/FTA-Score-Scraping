from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('https://www.englandrugby.com/fixtures-and-results/teams/bath/gallagher-premiership/2018-2019/').text  # decomment to use live website
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
for comp in soup.find_all('div', {'id': 'competitionstab-content2'}):
    id = 0
    month_group = []
    for data in comp.find_all('div', 'small-12 large-12 medium-12 columns'):
        print(data)


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

print('finished fixtures')
