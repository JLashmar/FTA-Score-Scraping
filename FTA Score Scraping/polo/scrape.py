from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.pololine.com/tournament/').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Competition', 'Match Date', 'Team A', '"Team B', 'Score 1', 'Score 2'])

# Competition specific info

comp_file = open('competition_scrape.csv', 'w', newline='')
comp_writer = csv.writer(comp_file)
comp_writer.writerow(['Id', 'Place', 'Club', 'Level', 'Tournament Type', 'Winner Points', 'Finalist Points', 'Semis Points', 'Rest of Players Points', ])

for comp_name in soup.find_all('a', class_='eg-zone-element-1'):
    competition = comp_name.text
    link = comp_name['href']
    print(competition)
    print(link)

    next_level_link = requests.get(link).text  # basically source
    bs = BeautifulSoup(next_level_link, 'lxml')  # basically soup

    # inside each page
    for table in bs.find_all('div', 'sp-template-event-list'):
        for section in table.find_all('h4'):
            stage = section.text

        for data in bs.find_all('tr', 'sp-row'):
            # match_date
            try:
                match_date = data.date.text
                match_date = match_date.split(' ')[0]
                date = match_date.split('-')
                date = '%s-%s-%s' % (date[2], date[1], date[0])
            except Exception as e:
                pass

            # team names
            try:
                for team_name in data.find_all('td', 'data-teams'):
                    mylist = []
                    for names in team_name.find_all('a'):
                        name = names.text
                        mylist.append(name)
                    team1 = mylist[0]
                    team2 = mylist[1]
            except Exception as e:
                pass

            # score
            try:
                for score in data.find_all('td', 'data-results'):
                    score = score.text.split('-')
                    score1 = score[0]
                    score2 = score[1]
                    if score == '-':
                        list = [stage, competition, date, team1, team2, '0']
                        csv_writer.writerow(list)
                    else:
                        list = [stage, competition, date, team1, team2, score1, score2]
                        csv_writer.writerow(list)
            except Exception as e:
                pass
    # competition info
    try:
        for data in bs.find_all('ul', 'acf'):
            list_of_lists = []
            count = 0
            for listData in data.find_all('li'):
                count = count + 1
                stuff = listData.text.split(':')
                list_of_lists.append(stuff)
            matchers = ['Count', 'Place', 'Club', 'Level', 'Tournament Type', 'Winner Points', 'Finalist Points', 'Semis Points', 'Rest of Players Points', ]
            matching = [s for s in list_of_lists if any(xs in s for xs in matchers)]
            matched = matching

            # Location
            competition_data = []
            try:
                #place = matched[0][0]
                location = matched[0][1]
                location_data = [location]
                competition_data.append(location_data)
            except Exception as e:
                pass
            # Club
            try:
                #club = matched[1][0]
                club_name = matched[1][1]
                club_data = [club_name]
                competition_data.append(club_data)
            except Exception as e:
                pass
            # Level
            try:
                #level = matched[2][0]
                handicap = matched[2][1]
                handicap_data = [handicap]
                competition_data.append(handicap_data)
            except Exception as e:
                pass
            # Tournament Type
            try:
                #tournament_type = matched[3][0]
                type_name = matched[3][1]
                type_data = [type_name]
                competition_data.append(type_data)
            except Exception as e:
                pass
            # Ranking Point System
            # Winner Points
            try:
                #win_ranking = matched[4][0]
                win_points = matched[4][1]
                win_data = [win_points]
                competition_data.append(win_data)
            except Exception as e:
                pass
            # Runner Up Points
            try:
                #run_ranking = matched[5][0]
                run_points = matched[5][1]
                run_data = [run_points]
                competition_data.append(run_data)
            except Exception as e:
                pass
            # semi points
            try:
                #semi_ranking = matched[6][0]
                semi_points = matched[6][1]
                semi_data = [semi_points]
                competition_data.append(semi_data)
            except Exception as e:
                pass
            # appearance points
            try:
                #appearance_ranking = matched[7][0]
                appearance_points = matched[7][1]
                appearance_data = [appearance_points]
                competition_data.append(appearance_data)
            except Exception as e:
                pass

            comp_writer.writerow(competition_data)

    except Exception as e:
        pass

comp_file.close
csv_file.close

print('done')
