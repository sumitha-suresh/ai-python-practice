import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("C:/Users/Admin/.vscode/extensions/sourcery.sourcery-1.37.0-win32-x64/exercises/data1.csv") 
print("Press 1 for line")
print("Press 2 for bar")
print("Press 3 for hist")
a=(int) (input("Enter Options"))

if(a==1):
    #create a line plot of different color for each week
    df.plot.line(color=['red','blue','brown','green'],marker="*",markersize=10,linewidth=3,linestyle="--",title='Sales Report')
elif (a==2):
    # plots a bar chart with the column "Days" as x axis
    df.plot(kind='bar',x='Day',title='Car Sales Report',color=['red', 'yellow','purple','blue'],edgecolor='Green',linewidth=2,linestyle='--')
elif a==3:
    df.plot(kind='hist',x='Day',bins=5,title='Car Sales Report',color=['red', 'yellow','purple','blue'],edgecolor='Green',linewidth=2,linestyle=':',hatch='o')
# Set title to "Car Sales Report"
#plt.title('Car Sales Report')
# Label x axis as "Days"
plt.xlabel('Days') 
# Label y axis as "Sales in Rs"
plt.ylabel('Sales in Rs')
plt.show()