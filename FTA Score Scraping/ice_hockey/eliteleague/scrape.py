from bs4 import BeautifulSoup
import requests
import csv
import re

schedule_source = requests.get('https://eliteleague.co.uk/game-centre/schedule/?season_id=18470').text  # decomment to use live website
# with open('templates/schedule.html') as schedule_source:
schedule_soup = BeautifulSoup(schedule_source, 'lxml')  # remove tab amd line above to use live website

fixture_file = open('fixtures.csv', 'w', newline='')
fixture_writer = csv.writer(fixture_file)
fixture_writer.writerow(['id', 'date', 'home_team', 'away_team', 'score'])

final_list = []
dates = schedule_soup.find_all('div', 'date-row')
for c in range(len(dates)):
    temp_list = []  # stores things
    # grabs the date div
    matchGroup = schedule_soup.find_all('div', 'game-set')  # finds all meetings as a list
    matchGroup = BeautifulSoup(str(matchGroup[c]), 'html.parser')  # finds the position in the meetings list based off of the date position in the date list
    for match in matchGroup.find_all('div', 'col-8 col-lg-10 text-center'):
        homeTeam = match.find('span', 'home-team')
        homeTeam = homeTeam.text
        awayTeam = match.find('span', 'away-team')
        awayTeam = awayTeam.text
        score = match.find('span', 'score')
        score = score.text  # need to fix this so that the weird question mark isnt there
        score = score.replace('–', '-')
        date = dates[c].text.replace('\n', '')
        teams = date, homeTeam, awayTeam, score
        teams = list(teams)
        temp_list.append(teams)
    final_list.append(temp_list)
# print(final_list)

matchId = 0
for date in final_list:
    for game in date:
        matchData = []
        matchId = matchId + 1
        matchData.append(matchId)
        date = game[0]
        date = date.split(' ')
        day = date[1]
        month = date[2]
        year = date[3]
        if month == "Jan":
            month = '01'
        if month == "Mar":
            month = '03'
        if month == "Sep":
            month = '09'
        if month == "Oct":
            month = '10'
        if month == "Nov":
            month = '11'
        if month == "Dec":
            month = '12'
        date = month + "/" + day + "/" + year
        homeTeam = game[1]
        awayTeam = game[2]
        score = game[3]
        matchData.append(date)
        matchData.append(homeTeam)
        matchData.append(awayTeam)
        matchData.append(score)
        fixture_writer.writerow(matchData)
        # match_date

fixture_file.close

#######
#Table#
#######

league_source = requests.get('https://eliteleague.co.uk/game-centre/standings/?season_id=18470').text  # decomment to use live website
# with open('templates/table.html') as league_source:
league_soup = BeautifulSoup(league_source, 'lxml')  # remove tab amd line above to use live website

table_file = open('league_standings.csv', 'w', newline='')
table_writer = csv.writer(table_file)
table_writer.writerow(['id', 'team', 'points', 'played', 'win', 'loss', 'overtime_loss', 'pct', 'goal_for', 'goal_against', 'pim', 'streak', ])

for table in league_soup.find_all('tbody'):
    id = 0
    for data in table.find_all('tr'):
        tableData = []
        id = id + 1
        teamData = data.find_all('th')
        team = teamData[0].text
        points = teamData[1].text
        num = data.find_all('td')
        played = num[0].text
        win = num[1].text
        loss = num[2].text
        overtime_loss = num[3].text
        pct = num[4].text
        goal_for = num[5].text
        goal_against = num[6].text
        pim = num[7].text
        streak = num[8].text
        tableData.append(id)
        tableData.append(team)
        tableData.append(points)
        tableData.append(played)
        tableData.append(win)
        tableData.append(loss)
        tableData.append(overtime_loss)
        tableData.append(pct)
        tableData.append(goal_for)
        tableData.append(goal_against)
        tableData.append(pim)
        tableData.append(streak)
        table_writer.writerow(tableData)

table_file.close

#####
#Cup#
#####

cup_source = requests.get('https://eliteleague.co.uk/game-centre/standings/?season_id=18469').text  # decomment to use live website
# with open('templates/table.html') as cup_source:
cup_soup = BeautifulSoup(cup_source, 'lxml')  # remove tab amd line above to use live website

cup_file = open('cup_standings.csv', 'w', newline='')
cup_writer = csv.writer(cup_file)
cup_writer.writerow(['id', 'team', 'points', 'played', 'win', 'loss', 'overtime_loss', 'pct', 'goal_for', 'goal_against', 'pim', 'streak', ])

cup_file.close
