import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
x1 = np.array([11, 12, 13, 14, 15])
y = np.array([2, 4, 6, 8, 10])

plt.plot(x, y, marker='D', linestyle='dashed', color='r', label='Data Points 1')
plt.plot(x1, y, marker='P', linestyle='dotted', color='b', label='Data Points 2')
plt.title('Line Plot with Markers')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
#plt.legend()
#plt.legend(['Sample Data'],loc='upper center', ncol=2, shadow=True, fontsize='large')
plt.legend(['Sample Data 1', 'Sample Data 2'],loc='upper right', ncol=1, shadow=True, fontsize='5')
#plt.legend(bbox_to_anchor=(0.75, 1.15), ncol=2) 

"""
plt.legend(['Sample Data'],loc='lower right', ncol=2, shadow=True, fontsize='12')
plt.legend(['Sample Data'],loc='upper right', ncol=2, shadow=True, fontsize='16')
"""
plt.grid(True)
plt.show()