"""This program shows Random walk diagram. The green point is the beginning and the red is the end"""

import matplotlib.pyplot as plt

from classes.random_walk import RandomWalk

while True:
	# Create casual wandering
	rw = RandomWalk(50_000)
	rw.fill_walk()

	# plot points wandering on a schedule
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15, 9))

	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=5)

	ax.scatter(0, 0, c='green', edgecolor='none', s=50)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

	# hide the axis
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()

	# if you want to exit from program you need to enter 'n'
	keep_running = input("Generate a new wandering? (y/n)")
	if keep_running == 'n':
		break


