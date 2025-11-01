import matplotlib.pyplot as plt              
#list storing date in string format
date=["15/03","16/03","17/03"]
#list storing temperature values
temp=[8.4,9.3,11.8]
#create a figure plotting temp versus date
plt.title("Date wise Temperature") 
plt.plot(date, temp)
#show the figure
plt.show()
