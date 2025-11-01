import matplotlib.pyplot as plt
import numpy as np

# Prepare data
x = np.random.rand(50) * 10
y = np.random.rand(50) * 10
colors = np.random.rand(50) * 100  # Values from 0 to 100 for color mapping

# Create scatter plot with cmap
plt.scatter(x, y, c=colors, cmap='plasmma', s=150, alpha=0.7, edgecolor='black')

# Add colorbar
plt.colorbar(label='Data Value')

# Add labels and title
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Scatter Plot with Plasma Colormap')

# Show the plot
plt.show()