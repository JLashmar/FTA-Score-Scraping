from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.pololine.com/tournament/').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Competition', 'Link'])

for comp_name in soup.find_all('a', class_='eg-zone-element-1'):
    competition = comp_name.text
    link = comp_name['href']
    print(competition)
    print(link)

    csv_writer.writerow([competition, link])

csv_file.close
