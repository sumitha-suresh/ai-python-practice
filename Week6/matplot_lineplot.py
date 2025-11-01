import matplotlib.pyplot as plt
import numpy as np

# Data for the line plot
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 1, 5, 3])

# Create the line plot
plt.plot(x, y)

# Add labels and title for clarity
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Simple Line Plot Example")

# Add a grid for better readability (optional)
plt.grid(True)

# Display the plot
plt.show()