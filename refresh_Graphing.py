import matplotlib.pyplot as plt

# Create the data
x_axis = [12, 15, 36, 65]
y_axis = [15, 19, 40, 60]

# Plot the data
plt.plot(x_axis, y_axis, marker='o')

# Add titles and labels
plt.title('Line using Line Graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)

# Show the plot
plt.show()

