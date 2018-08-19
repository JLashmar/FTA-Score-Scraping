from bs4 import BeautifulSoup
import requests
import csv

# source = requests.get('http://www.espn.com/golf/schedule').text #### decomment to use live website
with open('espn.html') as source:
    soup = BeautifulSoup(source, 'lxml')  # remove tab amd line above to use live website

#tournament_file = open('scrape_1_tournament.csv', 'w', newline='')
table_file = open('scrape_2_table.csv', 'w', newline='')

table_writer = csv.writer(table_file)
table_writer.writerow(['tournament_id', 'position', 'name', 'to_par', 'current_round', 'thru', 'round1', 'round2', 'round3', 'round4', 'total_score', 'id'])

# scrolls through the tournaments and finds the ID, used later on
tournament_id = []
tournament_count = 0

for comp in soup.find_all('tr'):
    for href in comp.find_all('td'):
        for link in href.find_all('a'):
            link = link['href']
            if 'tournament' in link:
                split = link.split("=")
                split_id = split[1]
                tournament_id.append(split_id)

for num in tournament_id:
    tournament = requests.get('http://www.espn.com/golf/leaderboard?tournamentId=' + num).text  # basically source #uncomment and indent to make like
    bs = BeautifulSoup(tournament, 'lxml')  # basically soup #uncomment and indent to make live

    # with open('table.html') as tournament:
    #bs = BeautifulSoup(tournament, 'lxml')
    tournament_count = tournament_count + 1
    for data in bs.find_all('header', 'matchup-header'):
        # name
        for tournament_name in data.find_all('h1'):
            tournament_name = tournament_name.text
        # date
        for date in data.find_all('div', 'date'):
            date = date.text
            split_date = date.split('-')
            date1 = split_date[0]  # date1 + year == 18 aug 2018
            date_block = split_date[1]
            date_block = date_block.split(',')
            date2 = date_block[0]  # date2 + year == 28 aug 2018
            year = date_block[1]
        # location
        for location in data.find_all('div', 'location'):
            location = location.text
        # course_detail
        for course_detail in data.find_all('div', 'content'):
            course_detail = course_detail.text.strip()
            detail = course_detail.split(' ')
            #par = detail[22]
            #par_score = detail[40]
            #yards = detail[58]
            #yards_distance = detail[76]
            #purse = detail[95]
            #purse_total = detail[112]
            #defending = detail[130]
            #defending_first_name = detail[149]
            #defending_last_name = detail[150]

    for row in bs.find_all('tr'):
        row_data = []
        row_data.append(tournament_count)
        # player specific data:
        # player finishing position
        for position in row.find_all('td', 'position'):
            position = position.text.strip()
            row_data.append(position)
            # print(position)
        # player name ################# need to split name up
        for name in row.find_all('a', 'full-name'):
            name = name.text.strip()
            row_data.append(name)
            # print(name)
        # to_par score
        for to_par in row.find_all('td', 'relativeScore'):
            to_par = to_par.text
            row_data.append(to_par)
            # print(to_par)
        # current_round score
        for current_round in row.find_all('td', 'relativeScore'):
            current_round = current_round.text
            row_data.append(current_round)
            # print(current_round)
        # thru score
        for thru in row.find_all('td', 'thru'):
            thru = thru.text
            row_data.append(thru)
            # print(thru)
        # round1 score
        for round1 in row.find_all('td', 'round1'):
            round1 = round1.text
            row_data.append(round1)
            # print(round1)
        # round2 score
        for round2 in row.find_all('td', 'round2'):
            round2 = round2.text
            row_data.append(round2)
            # print(round2)
        # round3 score
        for round3 in row.find_all('td', 'round3'):
            round3 = round3.text
            row_data.append(round3)
            # print(round3)
        # round4 score
        for round4 in row.find_all('td', 'round4'):
            round4 = round4.text
            row_data.append(round4)
            # print(round4)
        # total_score score
        for total_score in row.find_all('td', 'totalScore'):
            total_score = total_score.text
            row_data.append(total_score)
            # print(total_score)
        table_writer.writerow(row_data)


table_file.close

print('Done')
