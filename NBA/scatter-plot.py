import requests
from bs4 import BeautifulSoup
import datetime
import plotly.express as px

def get_player_data(stat_1, stat_2):
    URL = 'https://www.basketball-reference.com/leagues/NBA_' + year + '_per_game.html'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_player_rows = soup.findAll("tr", {"class": "full_table"})
    data = {'name': [], str(stat_1): [], str(stat_2): []}

    for player in all_player_rows:
        if (str(stat_1) == 'fg_pct' or str(stat_1) == 'fg3_pct'):
            data_stat_1 = str(stat_1)
        else:
            data_stat_1 = str(stat_1) + '_per_g'

        if (str(stat_2) == 'fg_pct' or str(stat_2) == 'fg3_pct'):
            data_stat_2 = str(stat_2)
        else:
            data_stat_2 = str(stat_2) + '_per_g'

        player_name = player.find("td", {"data-stat": 'player'}).text
        player_stat_1 = player.find("td", {"data-stat": str(data_stat_1)}).text
        player_stat_2 = player.find("td", {"data-stat": str(data_stat_2)}).text


        data['name'].append(player_name)
        data[str(stat_1)].append(player_stat_1)
        data[str(stat_2)].append(player_stat_2)

    return data

print('Enter \'pts\' for points')
print('Enter \'trb\' for total rebounds')
print('Enter \'ast\' for asists')
print('Enter \'stl\' for steals')
print('Enter \'blk\' for blocks')
print('Enter \'tov\' for turonvers')
print('Enter \'fg_pct\' for field goal percent')
print('Enter \'fg3_pct\' for field goal percent \n')

x_stat_input = str(input('Enter the stat you want on the x axis: '))
y_stat_input = str(input('Enter the stat you want on the y axis: '))
year = str(input('Enter a year: '))

acceptable_stats = [ 'pts', 'trb', 'ast', 'stl', 'blk', 'tov', 'fg_pct', 'fg3_pct' ]

now = datetime.datetime.now()
if (year == '' or int(year) > now.year):
    print('Invalid year, please pick the current year or one in the past')
elif (str(x_stat_input) == str(y_stat_input)):
    print('Invalid statistic entry. Pick 2 different statistics')
elif (x_stat_input in acceptable_stats and y_stat_input in acceptable_stats):
    print('Generating your report ...')
    generate_data = get_player_data(x_stat_input, y_stat_input)
    df = generate_data
    fig = px.scatter(df,
                    x=str(x_stat_input),
                    y=str(y_stat_input),
                    hover_data=['name'])
    fig.show()
else:
    print('Invalid statistic entry. Please try again')