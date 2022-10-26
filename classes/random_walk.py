"""Class RandomWalk for Random walk diagram"""

from random import choice

class RandomWalk:
	"""Class that generate casual wanderings."""

	def __init__(self, num_points=5000):
		"""Initialize attributes of wanderings."""

		self.num_points = num_points
		#Всі блукання починаються з (0, 0)
		self.x_values = [0]
		self.y_values = [0]


	def fill_walk(self):
		"""Calculate all points of wanderings."""

		#Continue to take step while wanderings do not rich required length
		while len(self.x_values) < self.num_points:

			#decide in what order moves and for how long
			x_direction = choice([1, -1])
			x_distance = choice([0, 1, 2])
			x_step = x_direction * x_distance

			y_direcrtion = choice([1, -1])
			y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
			y_step = y_direcrtion * y_distance

			# Discard steps that are not moving anywhere
			if x_step == 0 and y_step == 0:
				continue

			# Calculate a new position
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y) 
