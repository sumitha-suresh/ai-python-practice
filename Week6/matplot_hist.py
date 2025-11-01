import matplotlib.pyplot as plt
import numpy as np

# Generate random data for the histogram
data = [10,20,15,20,35,50,11,12,5,8,10,11,45,50,60,23,1,0]

# Plotting a basic histogram
plt.hist(data, bins=5, color='pink', edgecolor='black')

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')

# Display the plot
plt.show()