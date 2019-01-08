from matplotlib import pyplot as plt
import csv
from datetime import datetime

file_name = 'sitka_weather_07-2014.csv'
'''
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader) # 这是一个迭代器
    # print(header_row)

with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
'''
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)

    fig = plt.figure(dpi = 128, figsize=(10, 6))
    plt.plot(highs, c = 'red')
    # plt.show()

first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
print(first_date)
