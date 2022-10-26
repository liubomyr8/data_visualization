"""This program shows diagram of high and low temperatures in Sitka for 2018"""

import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

# Plot the high and low temperatures 

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='white', alpha=0.8)
ax.plot(dates, lows, c='white', alpha=0.8)
plt.fill_between(dates, highs, lows, facecolor='gray', alpha=0.2)

# Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()