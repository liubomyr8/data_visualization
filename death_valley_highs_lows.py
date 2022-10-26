"""This program shows diagram of high and low temperatures in Death Valley for 2018"""

import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        try:
        	high = int(row[5])  # x1
        	low = int(row[6])  # x2
        except ValueError:
        	print(f"Missing data for {current_date}")
        else:
	        hig = (high - 32) * 5 / 9
	        highs.append(hig)

	        lo = (low - 32) * 5 / 9
	        lows.append(lo)

# Plot the high and low temperatures 

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='white', alpha=0.8)
ax.plot(dates, lows, c='white', alpha=0.8)
plt.fill_between(dates, highs, lows, facecolor='gray', alpha=0.2)

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()