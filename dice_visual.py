"""The program shows Dice rolling diagram"""

from plotly.graph_objs import Bar, Layout
from plotly import offline
from classes.die import Die

# Create D6 and D10
die_1 = Die()
die_2 = Die(10)

# Make a few throws and store results in list
results = []
for roll_num in range(50_000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# analyze the results
frequences = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequences.append(frequency)

# visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequences)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D6 and a D10 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
