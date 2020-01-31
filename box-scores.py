import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

URL = 'https://www.basketball-reference.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

game_table = soup.findAll("div", {"class": "game_summary"})

for game in game_table:
    winning_table = []
    winning_headers = []
    winning_team = game.find("tr", {"class": "winner"}).find("a").text
    winning_team_abv = game.find("tr", {"class": "winner"}).find("a")['href'].split('/')[2]
    winning_team_score = game.find("tr", {"class": "winner"}).find("td", {"class": "right"}).text
    losing_table = []
    losing_headers = []
    losing_team = game.find("tr", {"class": "loser"}).find("a").text
    losing_team_abv = game.find("tr", {"class": "loser"}).find("a")['href'].split('/')[2]
    losing_team_score = game.find("tr", {"class": "loser"}).find("td", {"class": "right"}).text

    game_link = 'https://www.basketball-reference.com/' + game.find("td", {"class": "gamelink"}).find('a')['href']
    game_page = requests.get(game_link)
    game_soup = BeautifulSoup(game_page.content, 'html.parser')

    winning_stats_table = game_soup.find(id="box-" + winning_team_abv + "-game-basic")
    winning_header_elements = winning_stats_table.find_all('th', {"data-over-header": "Basic Box Score Stats"})
    for head in winning_header_elements:
        winning_headers.append(head.text)

    winning_table_body = winning_stats_table.find('tbody')
    winning_table_rows = winning_table_body.find_all('tr')

    for row in winning_table_rows:
        winning_player_row = []

        if row.find('th').text.strip() != 'Reserves':
            winning_player_row.append(row.find('th').text.strip())

        player_stat_elms = row.find_all('td')

        for player in player_stat_elms:
            if player.text != 'Did Not Play' and player.text != 'Not With Team' and player.text != 'Did Not Dress':
                winning_player_row.append(player.text)

        winning_table.append(winning_player_row)

    losing_stats_table = game_soup.find("table", {"id": "box-"+losing_team_abv+"-game-basic"})
    losing_header_elements = losing_stats_table.find_all('th', {"data-over-header": "Basic Box Score Stats"})
    losing_headers = []
    for head in losing_header_elements:
        losing_headers.append(head.text)

    losing_table_body = losing_stats_table.find('tbody')
    losing_table_rows = losing_table_body.find_all('tr')

    for row in losing_table_rows:
        losing_player_row = []

        if row.find('th').text.strip() != 'Reserves':
            losing_player_row.append(row.find('th').text.strip())

        player_stat_elms = row.find_all('td')

        for player in player_stat_elms:
            if player.text != 'Did Not Play' and player.text != 'Not With Team' and player.text != 'Did Not Dress':
                losing_player_row.append(player.text)

        losing_table.append(losing_player_row)

    print("")
    print(winning_team + " " + winning_team_score + " || " + losing_team + ' ' + losing_team_score)
    print("")
    print(winning_team)
    print(tabulate(winning_table, headers=winning_headers, tablefmt="psql"))
    print("")
    print(losing_team)
    print(tabulate(losing_table, headers=losing_headers, tablefmt="psql"))
