"""Class Die for Dice rolling histogram"""

from random import randint

class Die:
	"""Class represents one cube"""
	
	def __init__(self, num_sides=6):
		"""Determine cube with 6 facet"""
		self.num_sides = num_sides

	def roll(self):
		"""Return casual meaning from 1 to 6"""
		return randint(1, self.num_sides)


