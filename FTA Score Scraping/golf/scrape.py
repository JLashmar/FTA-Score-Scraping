from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('http://www.espn.com/golf/schedule').text  # decomment to use live website
# with open('espn.html') as source:
soup = BeautifulSoup(source, 'lxml')  # remove tab amd line above to use live website

#tournament_file = open('scrape_1_tournament.csv', 'w', newline='')
comp_file = open('scrape_1_comp.csv', 'w', newline='')

comp_writer = csv.writer(comp_file)
# taken out until fixed 'par_total', 'distance_total', 'purse_total', 'champ' keep in order
comp_writer.writerow(['id', 'tournament_name', 'start_date', 'end_date', 'location'])

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
    tournament = requests.get('http://www.espn.com/golf/leaderboard?tournamentId=' + num).text  # basically source #uncomment indent to make like
    bs = BeautifulSoup(tournament, 'lxml')  # basically soup #uncomment and indent to make live

# with open('table.html') as tournament:
#bs = BeautifulSoup(tournament, 'lxml')
# tournament_count = tournament_count + 1

    for data in bs.find_all('header', 'matchup-header'):
        course_data = []
        tournament_count = tournament_count + 1
        print(tournament_count)
        course_data.append(tournament_count)
        # name
        for tournament_name in data.find_all('h1'):
            tournament_name = tournament_name.text
            course_data.append(tournament_name)
        # date
        for date in data.find_all('div', 'date'):
            date = date.text
            split_date = date.split('-')
            date1 = split_date[0]  # date1 + year == 18 aug 2018
            date1 = date1.split(' ')
            month = date1[0]
            date1 = date1[1]
            date_block = split_date[1]
            date_block = date_block.split(',')
            date2 = date_block[0]  # date2 + year == 28 aug 2018
            date2 = re.sub('[JFMASONDabcdefghijklmnopqrstuqwreyz]', '', date2)
            print(date2)
            year = date_block[1]
            start_date = month + (' ') + date1 + year
            end_date = month + date2 + year
            course_data.append(start_date)
            course_data.append(end_date)
        # location
        for location in data.find('div', 'location'):
            location = location
            course_data.append(location)
            print(location)
        #################
        # course_detail #
        #  needs work   #
        #################
        # for course_detail in data.find_all('div', 'content'):
        #    course_detail = course_detail.text.strip()
        #    detail = course_detail.split(' ')
        #    try:
        #        par = detail[6]
        #        par = par.split('Y')
        #        par_total = par[0]
        #        course_data.append(par_total)
        #        print(par_total)
        #    except Exception as e:
        #        course_data.append('0')
        #    try:
        #        distance = detail[7]
        #        distance = distance.split('P')
        #        distance_total = distance[0]  # use this
        #        course_data.append(distance_total)
        #    except Exception as e:
        #        course_data.append('0')
        #    try:
        #        purse = detail[8]
        #        purse = purse.split('D')
        #        purse_total = purse[0]  # use this
        #        course_data.append(purse_total)
        #    except Exception as e:
        #        course_data.append('0')
        #    try:
        #        champ1 = detail[9]
        #        champ2 = detail[10]
        #        champ = champ1 + ' ' + champ2  # use this
        #        course_data.append(champ)
        #    except Exception as e:
        #        course_data.append('0')
        #    print(detail)

        # writing section
        comp_writer.writerow(course_data)
    loop_count = 0
    for row in bs.find_all('tr'):
        row_data = []
        loop_count = loop_count + 1

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
        if row_data == [tournament_count]:
            pass
        else:
            row_data.append(loop_count)
            table_writer.writerow(row_data)


table_file.close

print('Done')
