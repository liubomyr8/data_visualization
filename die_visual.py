"""The program shows Cube rolling diagram"""

import matplotlib.pyplot as plt
from classes.die import Die

# Create D6
die = Die()

# Make a few throws and store results in list
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

# analyze the results
frequences = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequences.append(frequency)

# visualize the results
x_values = list(range(1, die.num_sides+1))
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(x_values, frequences, s=15)

plt.show()

