import matplotlib.pyplot as plt

def autopct_format(pct):
    print(pct)
    # Calculate the actual value from the percentage
    val = int(round(pct * total / 100.0))
    return f'{val}' # Format as an integer

# Data for the pie chart
labels = ['CTS', 'TCS', 'Wipro', 'TestLeaf']
sizes = [35, 25, 25, 15]  # Proportions of each category
total = sum(sizes)

# Create the pie chart
plt.pie(sizes, labels=labels, autopct=autopct_format, startangle=90,frame=True,shadow=True)

plt.legend()
# Add a title (optional)
plt.title('Participant Distribution')

# Ensure the pie chart is drawn as a circle
plt.axis('equal')

# Display the chart
plt.show()