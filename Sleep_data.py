# -*- coding: utf-8 -*-

import pandas as pd
sleep_data=pd.read_csv("Sleep_data.csv")

import matplotlib.pyplot as plt
import numpy as np






sleep_duration_edited = []
for i in range(len(sleep_data["Sleep Duration"])):
    if sleep_data["Sleep Duration"][i] <9:
        sleep_duration_edited.append(sleep_data["Sleep Duration"][i])
























































#Part 4 
#g bar chart
average_sleep=sleep_data.groupby("Sleep Duration")["Stress Level"].mean()
plt.bar(average_sleep.index,average_sleep.values,color="blue")
plt.title("Averge Sleep By Stress Level")
plt.xlabel("Sleep Duration")
plt.ylabel("Stress Level")
plt.show()

#This bar chart demonstrates the average sleep by stress levels. This bar chart proves that the less sleep the people that participated in the data set, they had higher stress levels as it is een when the bar chart reaches the top of the y-axis.


#Part 4 
#H Scatter Plot
plt.scatter(sleep_data["Daily Steps"], sleep_data["Quality of Sleep"],
            color="purple")
plt.xlabel("Daily Steps")
plt.ylabel("Quality of Sleep")
plt.title("Relationship between Quality of Sleep and Daily Steps")
plt.grid(True)
plt.show()

#This scatter plot demonstrtes the relationship between quality of sleep and daily steps. On the x-axis, the amount of daily steps are shown by those who participated in the dataset and on the y-axis we have the quality of sleep. The scatter plot shows very mixed responses as their are dots everywhere and nothing is proportional.

#Part 4, 
#i, (Sleep Disorder) pie chart
rt_count=sleep_data.groupby("Sleep Disorder").size()
print(rt_count)
y=rt_count.values
mylabels=rt_count.index

plt.pie(y, labels=mylabels)
plt.title("Sleep Disorders in dataset")
plt.show()

#This pie chart demontstrates the sleep disorders in the dataset. The 2 most common sleep disorders are Slepp Apnea and Insomnia which come out to almost 50% each.






    
    










