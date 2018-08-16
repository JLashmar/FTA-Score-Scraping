from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.pololine.com/tournament/').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Competition', 'Match Date', 'Team A', '"Team B', 'Score 1', 'Score 2'])

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
            print(stage)

        for data in bs.find_all('tr', 'sp-row'):
            # match_date
            try:
                match_date = data.date.text
                match_date = match_date.split(' ')[0]
                date = match_date.split('-')
                date = '%s-%s-%s' % (date[2], date[1], date[0])
                print(date)
            except Exception as e:
                pass

            # team names
            try:
                for team_name in data.find_all('td', 'data-teams'):
                    mylist = []
                    for names in team_name.find_all('a'):
                        name = names.text
                        mylist.append(name)
                    # print(mylist)
                    team1 = mylist[0]
                    team2 = mylist[1]
                    # print(team2)
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
csv_file.close

print('done')
