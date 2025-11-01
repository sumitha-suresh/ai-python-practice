import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['CTS', 'TCS', 'Wipro', 'TestLeaf']
sizes = [35, 25, 25, 15]  # Proportions of each category

# Create the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=60)

# Add a title (optional)
plt.title('Participant Distribution')

# Ensure the pie chart is drawn as a circle
plt.axis('equal')

# Display the chart
plt.show()