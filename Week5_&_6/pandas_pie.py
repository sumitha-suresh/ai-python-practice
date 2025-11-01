import matplotlib.pyplot as plt
import pandas as pd

# Data for the pie chart
participantlist = {'Company':['CTS', 'TCS', 'Wipro', 'TestLeaf'], 'partsize':[35, 25, 25, 15] }# Proportions of each category

# Create a DataFrame
df = pd.DataFrame(participantlist)

# Set 'Company' as the index
df.set_index('Company', inplace=True)

# Plot a pie chart
df.plot(kind='pie',y='partsize', autopct='%1.1f%%', figsize=(6, 6), legend=True)
#df.plot.pie(y='partsize', autopct='%1.1f%%', figsize=(6, 6), legend=True)

# Create the pie chart
#plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=60)

# Add a title (optional)
plt.title('Participant Distribution')

# Ensure the pie chart is drawn as a circle
plt.axis('equal')

# Display the chart
plt.show()