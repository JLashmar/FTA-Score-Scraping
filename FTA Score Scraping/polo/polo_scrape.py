from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.pololine.com/tournament/').text
soup = BeautifulSoup(source, 'lxml')

# Competition specific info

comp_file = open('competition_data.csv', 'w', newline='', encoding='utf-8')
comp_writer = csv.writer(comp_file)
comp_writer.writerow(['comp_name', 'place', 'club', 'level', 'tournament_type', 'winner_points', 'finalist_points', 'semi_points', 'appearance_points', 'id'])

event_file = open('event_data.csv', 'w', newline='', encoding='utf-8')

event_writer = csv.writer(event_file)
event_writer.writerow(['stage', 'match_date', 'team_a', 'team_b', 'team_a_score', 'team_b_score', 'competition', 'id'])

comp_id = 0
match_id = 0
for comp_name in soup.find_all('a', class_='eg-zone-element-1'):
    competition = comp_name.text
    link = comp_name['href']
    print(competition)
    # print(link)
    comp_id = comp_id + 1
    print(comp_id)

    next_level_link = requests.get(link).text  # basically source
    bs = BeautifulSoup(next_level_link, 'lxml')  # basically soup

    # Match Data
    for table in bs.find_all('div', 'sp-template-event-list'):
        for section in table.find_all('h4'):
            stage = section.text

        for data in bs.find_all('tr', 'sp-row'):
            match_id = match_id + 1
            # print(match_id)
            # match_date
            try:
                match_date = data.date.text
                match_date = match_date.split(' ')[0]
                date = match_date.split('-')
                date = '%s-%s-%s' % (date[0], date[1], date[2])
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
                    score = score.text
                    if score == '-':
                        list = [stage, date, team1, team2, '0', '0', comp_id, match_id]
                        event_writer.writerow(list)
                        #print("this match was printed")
                    else:
                        score = score.split('-')
                        score1 = score[0]
                        score2 = score[1]
                        data = [stage, date, team1, team2, score1, score2, comp_id, match_id]
                        event_writer.writerow(data)
                        #print("this match was not printed")
            except Exception as e:
                pass
    # competition info
    try:
        for data in bs.find_all('ul', 'acf'):
            list_of_lists = []
            for listData in data.find_all('li'):
                stuff = listData.text.split(':')
                list_of_lists.append(stuff)
            matchers = ['Count', 'Place', 'Club', 'Level', 'Tournament Type', 'Winner Points', 'Finalist Points', 'Semis Points', 'Rest of Players Points', ]
            matching = [s for s in list_of_lists if any(xs in s for xs in matchers)]
            matched = matching

            # Location
            competition_data = []
            competition_data.append(competition)
            #id = id + 1
            # competition_data.append(id)
            try:
                #place = matched[0][0]
                location = matched[0][1]
                location = location.replace(",", "")
                print(location)
                location_data = location
                competition_data.append(location_data)
            except Exception as e:
                location_data = 'null'
                competition_data.append(location_data)
            # Club
            try:
                #club = matched[1][0]
                club_name = matched[1][1]
                club_data = club_name
                competition_data.append(club_data)
            except Exception as e:
                club_data = 'null'
                competition_data.append(club_data)
            # Level
            try:
                #level = matched[2][0]
                handicap = matched[2][1]
                handicap_data = handicap
                competition_data.append(handicap_data)
            except Exception as e:
                handicap_data = 'null'
                competition_data.append(handicap_data)
            # Tournament Type
            try:
                #tournament_type = matched[3][0]
                type_name = matched[3][1]
                type_data = type_name
                competition_data.append(type_data)
            except Exception as e:
                type_data = 'null'
                competition_data.append(type_data)
            # Ranking Point System
            # Winner Points
            try:
                #win_ranking = matched[4][0]
                win_points = matched[4][1]
                win_data = win_points
                competition_data.append(win_data)
            except Exception as e:
                win_data = 0
                competition_data.append(win_data)
            # Runner Up Points
            try:
                #run_ranking = matched[5][0]
                run_points = matched[5][1]
                run_data = run_points
                competition_data.append(run_data)
            except Exception as e:
                run_data = 0
                competition_data.append(run_data)
            # semi points
            try:
                #semi_ranking = matched[6][0]
                semi_points = matched[6][1]
                semi_data = semi_points
                competition_data.append(semi_data)
            except Exception as e:
                semi_data = 0
                competition_data.append(semi_data)
            # appearance points
            try:
                #appearance_ranking = matched[7][0]
                appearance_points = matched[7][1]
                appearance_data = appearance_points
                competition_data.append(appearance_data)
                # print(appearance_data)
            except Exception as e:
                appearance_data = 0
                competition_data.append(appearance_data)
                # print(appearance_data)
            competition_data.append(comp_id)

            comp_writer.writerow(competition_data)

    except Exception as e:
        pass

comp_file.close
event_file.close

print('done')
