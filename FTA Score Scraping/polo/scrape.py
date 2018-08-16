from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.pololine.com/tournament/').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Competition', 'Match Date', 'Team A', '"Team B', 'Score'])

for comp_name in soup.find_all('a', class_='eg-zone-element-1'):
    competition = comp_name.text
    link = comp_name['href']
    print(competition)
    print(link)

    next_level_link = requests.get(link).text  # basically source
    bs = BeautifulSoup(next_level_link, 'lxml')  # basically soup

    # inside each page
    for data in bs.find_all('tr', 'sp-row'):
        # match_date
        try:
            match_date = data.date.text
            match_date = match_date.split(' ')[0]
            date = match_date.split('-')
            date = '%s-%s-%s' % (date[2], date[1], date[0])
            # print(date)
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
            scorelist = []
            for score in data.find_all('td', 'data-results'):
                score = score.text
                scorelist.append(score)
                print(scorelist)
                if score == '-':
                    list = [competition, date, team1, team2, '0', '0']
                    csv_writer.writerow(list)
                    # print(list)
                else:
                    list = [competition, date, team1, team2, score]
                    csv_writer.writerow(list)
                    # print(list)
        except Exception as e:
            pass

csv_file.close

print('done')
