"""This program shows diagram Daily values of rain in Death Valley for 2018"""

import csv
from datetime import datetime as dat
from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	rains, dates = [], []

	for row in reader:
		current_date = dat.strptime(row[2], '%Y-%m-%d')
		dates.append(current_date)  # x

		rain = float(row[3])
		rains.append(rain)  # y

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='red')
plt.title("Daily values of rain - 2018", fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('% of rain', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()






