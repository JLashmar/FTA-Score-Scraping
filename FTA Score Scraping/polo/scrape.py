from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.pololine.com/tournament/').text
soup = BeautifulSoup(source, 'lxml')

# csv_file = open('cms_scrape.csv', 'w')

# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Competition', 'Link'])

# for comp_name in soup.find_all('a', class_='eg-zone-element-1'):
#    competition = comp_name.text
#    link = comp_name['href']
#    print(competition)
#    print(link)
# print(comp_page)

#    csv_writer.writerow([competition, link])

comp_link = soup.find('a', class_='eg-zone-element-1')
link = comp_link['href']


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
        print(date)
    except Exception as e:
        pass

    # team names
    try:
        for team_name in data.find_all('td', 'data-teams'):
            for names in team_name.find_all('a'):
                name = names.text
                name = name
                print(name)
    except Exception as e:
        pass

    # score
    try:
        for score in data.find_all('td', 'data-results'):
            score = score.text
            if score == '-':
                print('0')
            else:
                print(score)
    except Exception as e:
        pass

    # print(data.prettify())


# for info in comp_link.find('li'):
# print(info)

# csv_file.close
