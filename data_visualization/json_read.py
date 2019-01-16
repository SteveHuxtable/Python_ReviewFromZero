import json
'''
from urllib.request import urlopen

json_url = 'http://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)

req = response.read()

with open('btc_close_2017_urllib.json', 'wb') as f:
    f.write(req)

file_urllib = json.loads(req)
print(file_urllib)
'''

import requests
json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)

with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)
file_requests = req.json()

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

for btc_dict in btc_data:
    date = btc_dict['date']
    month = btc_dict['month']
    week = btc_dict['week']
    weekday = btc_dict['weekday']
    close = btc_dict['close']
    print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))

dates = []
months = []
weeks = []
weekdays = []
close = []

for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

import pygal
import math

line_chart = pygal.Line(x_label_rotation = 20, show_minor_x_labels = False)
line_chart.title = 'shou pan jia'
line_chart.x_labels = dates
N = 20

line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('shou pan jia', close_log)
line_chart.render_to_file('test_load.svg')

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)