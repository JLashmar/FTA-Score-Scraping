from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('http://www.rugby-league.com/superleague/fixtures').text  # decomment to use live website
# with open('templates/skysports.html') as source:
soup = BeautifulSoup(source, 'lxml')  # remove tab amd line above to use live website

#tournament_file = open('scrape_1_tournament.csv', 'w', newline='')
###comp_file = open('scrape_1_comp.csv', 'w', newline='')

###comp_writer = csv.writer(comp_file)
# taken out until fixed 'par_total', 'distance_total', 'purse_total', 'champ' keep in order
###comp_writer.writerow(['id', 'tournament_name', 'start_date', 'end_date', 'location'])

###table_file = open('scrape_2_table.csv', 'w', newline='')
###table_writer = csv.writer(table_file)
###table_writer.writerow(['tournament_id', 'position', 'name', 'to_par', 'current_round', 'thru', 'round1', 'round2', 'round3', 'round4', 'total_score'])

for comp in soup.find_all('section', 'competition font'):
    match_data = []
    for date in comp.find_all('h2'):
        date = date.text.strip()
        split = date.split(' ')
        date = split[1]
        date = re.sub('[JFMASONDabcdefghijklmnopqrstuqwreyz]', '', date)
        month = split[2]
        year = split[3]
        full_date = date + ' ' + month + ' ' + year + ' '
        match_data.append(full_date)
    for comps in comp.find_all('h3'):
        comps = comps.text.strip()
        match_data.append(comps)
    for data in comp.find_all('a'):
        game_data = []
        for rounds in data.find_all('span', 'left'):
            rounds = rounds.text.strip()
            game_data.append(rounds)
        for home in data.find_all('span', 'home'):
            home = home.text.strip()
            game_data.append(home)
        for away in data.find_all('span', 'away'):
            away = away.text.strip()
            game_data.append(away)
        for kickoff in data.find_all('span', 'ko'):
            kickoff = kickoff.text.strip()
            game_data.append(kickoff)

        match_data.append(game_data)

    # print(match_data)
for data in soup.find_all('button', 'load-more-matches'):
    for comp in soup.find_all('section', 'competition font'):
        match_data = []
        for date in comp.find_all('h2'):
            date = date.text.strip()
            split = date.split(' ')
            date = split[1]
            date = re.sub('[JFMASONDabcdefghijklmnopqrstuqwreyz]', '', date)
            month = split[2]
            year = split[3]
            full_date = date + ' ' + month + ' ' + year + ' '
            match_data.append(full_date)
        for comps in comp.find_all('h3'):
            comps = comps.text.strip()
            match_data.append(comps)
        for data in comp.find_all('a'):
            game_data = []
            for rounds in data.find_all('span', 'left'):
                rounds = rounds.text.strip()
                game_data.append(rounds)
            for home in data.find_all('span', 'home'):
                home = home.text.strip()
                game_data.append(home)
            for away in data.find_all('span', 'away'):
                away = away.text.strip()
                game_data.append(away)
            for kickoff in data.find_all('span', 'ko'):
                kickoff = kickoff.text.strip()
                game_data.append(kickoff)

            match_data.append(game_data)
        print(match_data)
