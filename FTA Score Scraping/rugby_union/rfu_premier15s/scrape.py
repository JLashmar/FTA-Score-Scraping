from bs4 import BeautifulSoup
import requests
import csv
import re

fixture_source = requests.get('https://www.premier15s.com/fixtures-and-results/fixtures/').text  # decomment to use live website
# with open('templates/premier15s_fixtures.html') as fixture_source:
fixture_soup = BeautifulSoup(fixture_source, 'lxml')  # remove tab amd line above to use live website

fixture_file = open('premier15s_fixtures.csv', 'w', newline='')
fixture_writer = csv.writer(fixture_file)
fixture_writer.writerow(['id', 'round', 'home_team', 'match_date', 'away_team'])

for group in fixture_soup.find_all('div', 'group'):
    id = 0
    # id
    for roundNum in group.find_all('div', 'group-name'):
        roundNum = roundNum.text.strip()
        roundNum = roundNum.split(' ')
        roundNum = roundNum[1]
        # round
    for match in group.find_all('div', 'fix-repeat'):
        match_data = []
        id = id + 1
        match_data.append(id)
        match_data.append(roundNum)
        for homeTeam in match.find_all('div', 'fix-home'):
            homeTeam = homeTeam.text.strip()
            match_data.append(homeTeam)
            # home_team
        for date in match.find_all('div', 'fix-date'):
            date = date.text.strip()
            date = date.split(' ')
            day = date[0]
            month = date[1]
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
            date = month + " " + day
            if month == '01':
                date = month + "/" + day + "/2019"
                match_data.append(date)
            if month == '02':
                date = month + "/" + day + "/2019"
                match_data.append(date)
            if month == '03':
                date = month + "/" + day + "/2019"
                match_data.append(date)
            if month == '09':
                date = month + "/" + day + "/2018"
                match_data.append(date)
            if month == '10':
                date = month + "/" + day + "/2018"
                match_data.append(date)
            if month == '11':
                date = month + "/" + day + "/2018"
                match_data.append(date)
            if month == '12':
                date = month + "/" + day + "/2018"
                match_data.append(date)
            # match_date
        for awayTeam in match.find_all('div', 'fix-away'):
            awayTeam = awayTeam.text.strip()
            match_data.append(awayTeam)
            # away_team
        fixture_writer.writerow(match_data)
        # print(match_data)
fixture_file.close

#########
#results#
#########

result_source = requests.get('https://www.premier15s.com/fixtures-and-results/results/').text  # decomment to use live website
# with open('templates/premier15s_results.html') as result_source:
result_soup = BeautifulSoup(result_source, 'lxml')  # remove tab amd line above to use live website

result_file = open('premier15s_results.csv', 'w', newline='')
result_writer = csv.writer(result_file)
result_writer.writerow(['id', 'round', 'home_team', 'home_score', 'away_score', 'away_team'])

for group in result_soup.find_all('div', 'group'):
    id = 0
    # id
    for roundNum in group.find_all('div', 'group-name'):
        roundNum = roundNum.text.strip()
        roundNum = roundNum.split(' ')
        roundNum = roundNum[1]
        # round
    for match in group.find_all('div', 'fix-repeat'):
        match_data = []
        id = id + 1
        match_data.append(id)
        match_data.append(roundNum)
        for score in match.find('span'):
            score = score.strip()
            score = score.split('-')
            homeScore = score[0]
            awayScore = score[1]
        for homeTeam in match.find_all('div', 'fix-home'):
            homeTeam = homeTeam.text.strip()
            match_data.append(homeTeam)  # home_team
            match_data.append(homeScore)  # home_score
        for awayTeam in match.find_all('div', 'fix-away'):
            awayTeam = awayTeam.text.strip()
            match_data.append(awayScore)  # away_score
            match_data.append(awayTeam)  # away_team
        result_writer.writerow(match_data)
        # print(match_data)
result_file.close

#######
#table#
#######

table_source = requests.get('https://www.premier15s.com/fixtures-and-results/standings/').text  # decomment to use live website
# with open('templates/premier15s_table.html') as table_source:
table_soup = BeautifulSoup(table_source, 'lxml')  # remove tab amd line above to use live website

table_file = open('premier15s_table.csv', 'w', newline='')
table_writer = csv.writer(table_file)
table_writer.writerow(['id', 'position', 'team_name', 'won', 'draw', 'loss', 'points_for', 'points_against', 'points_difference', 'try_bonus', 'loss_bonus', 'points'])

for group in table_soup.find_all('tbody'):
    id = 0
    for table in group.find_all('tr')[1:]:
        id = id + 1
        row_data = []
        row_data.append(id)
        for position in table.find_all('td', 'table-position'):
            position = position.text.strip()
            row_data.append(position)
            # position
        for team in table.find_all('td', 'table-name'):
            team = team.text.strip()
            row_data.append(team)
            # team_name
        for won in table.find_all('td', 'table-won'):
            won = won.text.strip()
            row_data.append(won)
            # won
        for drawn in table.find_all('td', 'table-drawn'):
            drawn = drawn.text.strip()
            row_data.append(drawn)
            # draw
        for lost in table.find_all('td', 'table-lost'):
            lost = lost.text.strip()
            row_data.append(lost)
            # loss
        for f in table.find_all('td', 'table-f'):
            f = f.text.strip()
            row_data.append(f)
            # points_for
        for a in table.find_all('td', 'table-a'):
            a = a.text.strip()
            row_data.append(a)
            # points_against
        for bpts in table.find_all('td', 'table-bpts'):
            bpts = bpts.text.strip()
            row_data.append(bpts)
            # points_difference
        for tb in table.find_all('td', 'table-tb'):
            tb = tb.text.strip()
            row_data.append(tb)
            # try_bonus
        for lb in table.find_all('td', 'table-lb'):
            lb = lb.text.strip()
            row_data.append(lb)
            # loss_bonus
        for pts in table.find_all('td', 'table-pts'):
            pts = pts.text.strip()
            row_data.append(pts)
            # points
        table_writer.writerow(row_data)
        # print(row_data)
table_file.close
