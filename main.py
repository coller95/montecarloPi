import random
import matplotlib.pyplot as plt

def generate_point():
	x = random.uniform(-1, 1)
	y = random.uniform(-1, 1)
	return x, y

# print(generate_point())


# Create a figure and axis
fig, ax = plt.subplots()

# Set labels and title
ax.set(xlabel='X-axis', ylabel='Y-axis', title='Dynamic Plot')

n = 10000000
m = 0
pltx = []
plty = []
for nn in range(1,n):
	x, y = generate_point()
	if x*x + y*y <= 1:
		m += 1

	pi = 4*m / nn

	pltx.append(nn)
	plty.append(pi)

	# Clear the previous plot
	ax.clear()

	ax.text(pltx[-1], plty[-1], f'{plty[-1]}', fontsize=10, verticalalignment='bottom')
	
	# Plot the updated data
	ax.plot(pltx, plty)

	# Show the plot
	plt.pause(0.001)

# Show the final plot
plt.show()
