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
print_group = []
for comp in soup.find_all('div', {'id': 'competitionstab-content2'}):
    id = 0
    month_group = []

    for fixture in comp.find_all('div', 'fixturedate'):
        fixture = fixture.text
        fixture = fixture.split(" ")
        date = fixture[1]
        date = date.replace('st', '')
        date = date.replace('nd', '')
        date = date.replace('rd', '')
        date = date.replace('th', '')
        month = fixture[2]
        month_list = ['August', 'September', 'October', 'November', 'December']
        if any(month in s for s in month_list):
            first_half = "2018 " + month
            match_date = first_half + " " + date
        else:
            second_half = "2019 " + month
            match_date = second_half + " " + date
        month_group.append(match_date)
    for item in comp.find_all('div', 'pseudo-table'):
        id = id + 1
        fixture_group = []
        fixture_group.append(id)
        for teams in item.find_all('a'):
            teams = teams.text
            fixture_group.append(teams)
        fixture_writer.writerow(fixture_group)
        print_group.append(fixture_group)
    print_group.append(month_group)
    # fixture_writer.writerow(month_group)
print(print_group)

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
