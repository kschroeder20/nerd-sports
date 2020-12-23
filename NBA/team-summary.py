import requests
from bs4 import BeautifulSoup
import datetime
from tabulate import tabulate

def get_team_data(team_abvr, year):
    URL = 'https://www.basketball-reference.com/teams/' + team_abvr + '/' + year + '.html'
    print(URL)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    player_table = soup.findAll("table", {"id": "per_game"})

    headers = []
    for table in player_table:
        header_elements = table.findAll('th')
        for head in header_elements:
            headers.append(head.text)
    print(headers)


team_abvr = str(input('Enter team abbriviateion (ex: \'LAC\'): '))
year = str(input('Enter a year: '))

now = datetime.datetime.now()
if (year == '' or int(year) > now.year + 1):
    print('Invalid year, please pick the current year or one in the past')
else:
    get_team_data(team_abvr, year)


