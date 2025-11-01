import matplotlib.pyplot as plt
import numpy as np

categories = ['Ford', 'Honda', 'Hyundai']
data1 = np.array([20, 30, 40])
data2 = np.array([30, 20, 10])

plt.bar(categories, data1, label='Series 1',width=0.25)
plt.bar(categories, data2, bottom=data1, label='Series 2',width=0.25) # Stacked on top of data1
plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Stacked Bar Chart")
plt.legend()
plt.show()