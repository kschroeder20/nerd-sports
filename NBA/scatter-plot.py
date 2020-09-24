import requests
from bs4 import BeautifulSoup
import datetime

print('Enter \'pts\' for points')
print('Enter \'trb\' for total rebounds \n')

x_stat_input = str(input('Enter the stat you want on the x axis: '))
y_stat_input = str(input('Enter the stat you want on the y axis: '))
year = str(input('Enter a year: '))

now = datetime.datetime.now()
if (year == '' or int(year) >= now.year):
    print('Invalid year')
else:
    URL = 'https://www.basketball-reference.com/leagues/NBA_' + year + '_per_game.html'
    page = requests.get(URL)

    x_stat_choice = determine_axis_value(x_stat_input, 'x_axis')
    y_stat_choice = determine_axis_value(y_stat_input, 'y_axis')

    if (x_stat_choice == 'pts'):
        print("Points")
    elif (x_stat_choice == 'trb'):
        print("Total Rebounds")
    else:
        print('Invalid statistic')

def determine_axis_value(stat_input, axis):
    if (stat_input == 'pts'):
        axis_array = get_axis_array('pts')
    elif (stat_input == 'trb'):
        print("Total Rebounds")
    else:
        print('Invalid statistic')

# def get_axis_array():
