import numpy as np 
import matplotlib.pyplot as plt 

barWidth = 0.25

Cohort1 = [12, 30, 1, 8, 22]
Cohort2 = [28, 6, 16, 5, 10] 
Cohort3 = [29, 3, 24, 25, 17] 

ch1 = np.arange(len(Cohort1))   #[0 1 2 3 4]
print(ch1)
ch2 = [x + barWidth for x in ch1]  #[0.25 1.25 2.25 3.25 4.25]
print(ch2)
# `ch3` is creating a list of x-coordinates for the bars of Cohort3 in the bar chart. It is calculated
# by adding the `barWidth` to each x-coordinate in the `ch2` list, which positions the bars for
# Cohort3 next to the bars for Cohort2 with the specified spacing.
# `ch3` is creating a list of x-coordinates for the bars of Cohort3 in the bar chart. It is calculated
# by adding the `barWidth` to each x-coordinate in the `ch2` list, which positions the bars for
# Cohort3 next to the bars for Cohort2 with the specified spacing.
ch3 = [x + barWidth for x in ch2] #[0.5 1.5 2.5 3.5 4.5]
print(ch3)

plt.bar(ch1, Cohort1, color ='r', width = barWidth, 
        edgecolor ='black', label ='Cohort1') 
plt.bar(ch2, Cohort2, color ='g', width = barWidth, 
        edgecolor ='black', label ='Cohort2') 
plt.bar(ch3, Cohort3, color ='b', width = barWidth, 
        edgecolor ='black', label ='Cohort3') 
#plt.title("Assignmment Status")
plt.title("Assignmment Status",fontname="Brush Script MT")
plt.xlabel('Cohort', fontname="Brush Script MT", fontweight ='bold', fontsize = 12) 
plt.ylabel('Assignments Completed', fontname="Brush Script MT", fontsize = 15) 
plt.xticks([r + barWidth for r in range(len(Cohort1))], 
        ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])

plt.legend()
plt.savefig('chart1.png')
plt.show() 