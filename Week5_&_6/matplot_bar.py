import matplotlib.pyplot as plt
import numpy as np

# Sample data
cohort = ['Cohort1', 'Cohort2', 'Cohort3', 'Cohort4']
values = [30, 40, 30, 45]

# Create the bar chart1
plt.bar(cohort, values, color='skyblue',width=0.5,align='edge')
#plt.barh(cohort, values, color='skyblue')

# Add labels and title
plt.xlabel('Cohort')
plt.ylabel('Problems Solved')
plt.title('Cohort Problem Solution Status')

# Display the plot
plt.show()