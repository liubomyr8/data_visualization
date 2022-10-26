"""This program shows the construction of a diagram based on lists of x and y-coordinate values"""

import matplotlib.pyplot as plt

x_val = range(1, 5001)
y_val = [x**2 for x in x_val]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_val, y_val, c=y_val, cmap=plt.cm.Greens, s=10)

ax.axis([0, 5000, 0, 25000000])
plt.show()