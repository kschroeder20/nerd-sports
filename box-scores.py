import requests
from bs4 import BeautifulSoup

URL = 'https://www.basketball-reference.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

game_table = soup.findAll("div", {"class": "game_summary"})

for game in game_table:
    winning_team = game.find("tr", {"class": "winner"}).find("a").text
    winning_team_score = game.find("tr", {"class": "winner"}).find("td", {"class": "right"}).text
    losing_team = game.find("tr", {"class": "loser"}).find("a").text
    losing_team_score = game.find("tr", {"class": "loser"}).find("td", {"class": "right"}).text

    game_link = 'https://www.basketball-reference.com/' + game.find("td", {"class": "gamelink"}).find('a')['href']
    game_page = requests.get(game_link)
    game_soup = BeautifulSoup(game_page.content, 'html.parser')

    print(winning_team + " " + winning_team_score + " || " + losing_team + ' ' + losing_team_score)
    print(game_link)