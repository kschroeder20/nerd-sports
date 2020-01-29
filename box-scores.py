import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

URL = 'https://www.basketball-reference.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

game_table = soup.findAll("div", {"class": "game_summary"})

for game in game_table:
    table = []
    winning_team = game.find("tr", {"class": "winner"}).find("a").text
    winning_team_score = game.find("tr", {
        "class": "winner"
    }).find("td", {
        "class": "right"
    }).text
    losing_team = game.find("tr", {"class": "loser"}).find("a").text
    losing_team_score = game.find("tr", {
        "class": "loser"
    }).find("td", {
        "class": "right"
    }).text

    game_link = 'https://www.basketball-reference.com/' + game.find(
        "td", {
            "class": "gamelink"
        }).find('a')['href']
    game_page = requests.get(game_link)
    game_soup = BeautifulSoup(game_page.content, 'html.parser')

    stats_table = game_soup.find("table", {"class": "stats_table"})
    header_elements = stats_table.find_all(
        'th', {"data-over-header": "Basic Box Score Stats"})
    headers = []
    for head in header_elements:
        headers.append(head.text)

    table_body = stats_table.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        player_row = []

        if row.find('th').text.strip() != 'Reserves' and row.find(
                'th').text.strip() != '':
            player_row.append(row.find('th').text.strip())

        player_stat_elms = row.find_all('td')

        for player in player_stat_elms:
            if player.text != 'Did Not Play' and player.text != 'Not With Team' and player.text != 'Did Not Dress' and player.text != '':
                player_row.append(player.text)

        table.append(player_row)
        # player_row.append(player_link.text)

    # players = []
    # player_rows = []
    # player_elements = stats_table.find_all('th', {"data-stat": "player"})
    # for player in player_elements:
    #     current_player_row = []
    #     current_player_row.append(player.text)

    #     player_stats_elements = player.find_all('td')

    #     for player in player_stats_elements:
    #         current_player_row.append(player.text)

    print(winning_team + " " + winning_team_score + " || " + losing_team +
          ' ' + losing_team_score)
    print(tabulate(table, headers=headers, tablefmt="psql"))
