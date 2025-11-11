# -*- coding: utf-8 -*-

import pandas as pd
sleep_data=pd.read_csv("Sleep_data.csv")

# Show the first few rows
print(sleep_data.head())

# Display dataset info
print(sleep_data.info())

import numpy as np

# Convert important numeric columns to NumPy arrays
age = sleep_data["Age"].to_numpy()
sleep_duration = sleep_data["Sleep Duration"].to_numpy()
sleep_quality = sleep_data["Quality of Sleep"].to_numpy()
physical_activity = sleep_data["Physical Activity Level"].to_numpy()
stress_level = sleep_data["Stress Level"].to_numpy()

#Include heart rate and daily steps as numeric arrays
heart_rate = sleep_data["Heart Rate"].to_numpy()
daily_steps = sleep_data["Daily Steps"].to_numpy()


# ---------- Part 3: Manipulating the data ----------

# remove unnecessary columns
sleep_data = sleep_data.drop(["Person ID", "Occupation", "Blood Pressure"], axis=1, errors="ignore")

# use a loop and conditional to remove duplicates
unique_rows = []
for i in range(len(sleep_data)):
    if list(sleep_data.iloc[i]) not in unique_rows:
        unique_rows.append(list(sleep_data.iloc[i]))

# rebuild the dataset without duplicates
clean = pd.DataFrame(unique_rows, columns=sleep_data.columns)

print("Rows before filtering:", len(sleep_data))
print("Rows after removing duplicates:", len(clean))

# after you build `clean`
clean.to_csv("Sleep_data_clean.csv", index=False)
print("Final columns:", list(clean.columns))
print(clean.head())
# ---------- Part 4: Plotting the data ----------
import matplotlib.pyplot as plt

#1)Plot a histogram of Quality of sleep from the cleaned dataset
# Shows how sleep quality scores are distributed accross all individuales

#convert String values to numerical values
clean["Quality of Sleep"] = pd.to_numeric(clean["Quality of Sleep"], errors='coerce')  

#Create histogram
clean['Quality of Sleep'].plot.hist(
    bins=np.arange(clean['Quality of Sleep'].min(), clean['Quality of Sleep'].max() +1,1), # so the bars can touch eachother          
    color='skyblue',     
    edgecolor='black',
    rwidth=1,
    figsize=(6,4),      
)    
#Add tittle and lables
plt.title('Distribution of Sleep Quality')
plt.xlabel('Quality of Sleep')
plt.ylabel('Number of individuals')
plt.grid(True,linestyle='--',alpha=0.6)         
plt.show()

#2) Plot with more than 1 array 
# Compare Sleep Duration and Heart Rate for the same participants

# x-axis: participant index
x = np.arange(len(clean))
y_sleep = clean['Sleep Duration']
y_hr    = clean['Heart Rate']

plt.figure(figsize=(10, 5))
plt.plot(x, y_sleep, label='Sleep Duration (hours)', color='blue', linestyle='-', linewidth=2)
plt.plot(x, y_hr,    label='Heart Rate (BPM)',     color='red',  linestyle='--', linewidth=2)

plt.title('Sleep Duration vs Heart Rate (same participants)')
plt.xlabel('Participant index')
plt.ylabel('Value')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()



#3) Plot with grid
#Bar graph: The average quality of sleep by BMI Category
#To compare the weight of a person (using the BMI indication ) to the effect on the quality of sleep

#Use the average sleep quality per BMI category
avg_sleep_by_bmi=clean.groupby('BMI Category')['Quality of Sleep'].mean()

# Smaller Y-axis values
plt.yticks(np.arange(0,10,0.5))

#Create a bar graph 
avg_sleep_by_bmi.plot(kind='bar',color='purple',edgecolor='black')

plt.xlabel('BMI Category')
plt.ylabel('Average Quality of Sleep')
plt.title('Average Quality of Sleep by BMI Category')
plt.grid(axis='y',linestyle='--', alpha=0.7)
plt.show() 



#4) Plot with 2 subplots side by side
#Compare Physical activity levels and sleep duration and heart rate and sleep duration 
#to see what is the impact of an active life style on sleep and mostly see if there is any possible relationships

#Create 2 subplots side by side
fig, axes = plt.subplots(1, 2, figsize=(14, 5))  

# SubPlot 1: The effect of Physical Activity Levels on Sleep Duration 
x1 = clean['Physical Activity Level']
y1 = clean['Sleep Duration']
axes[0].scatter(x1, y1, color='blue', label='Data points')
m1, b1 = np.polyfit(x1, y1,1)  # Linear trendline
axes[0].plot(x1, m1*x1 + b1, color='red', label=f'Trendline')
axes[0].set_xlabel('Daily Steps')
axes[0].set_ylabel('Quality of Sleep(h)')
axes[0].set_title('The effect of physical activity on Sleep Duration')
axes[0].legend()

#SubPlot 2: The effect of Heart Rate on Sleep Duration
x2 = clean['Heart Rate'] 
y2 = clean['Sleep Duration']
axes[1].scatter(x2, y2, color='green', label='Data points')
m2, b2 = np.polyfit(x2, y2, 1)
axes[1].plot(x2, m2*x2 + b2, color='red', label=f'Trendline')
axes[1].set_xlabel('Heart Rate (BPM)')
axes[1].set_ylabel('Sleep Duration (h)')
axes[1].set_title('The effect of Heart Rate on Sleep Duration')
axes[1].legend()

# Adjust layout 
plt.tight_layout()
plt.show()


#Part 4 
#g bar chart
# This section creates a bar chart showing the average sleep duration grouped by stress level.
# It helps visualize how stress levels may affect the average duration of sleep.
average_sleep=sleep_data.groupby("Sleep Duration")["Stress Level"].mean()
plt.bar(average_sleep.index,average_sleep.values,color="blue")
plt.title("Averge Sleep By Stress Level")
plt.xlabel("Sleep Duration")
plt.ylabel("Stress Level")
plt.show()

#This bar chart demonstrates the average sleep by stress levels. This bar chart proves that the less sleep the people that participated in the data set, they had higher stress levels as it is een when the bar chart reaches the top of the y-axis.


#Part 4 
#H Scatter Plot
# This section generates a scatter plot comparing the quality of sleep and the number of daily steps.
# It helps identify if physical activity levels influence sleep quality.
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
# This section creates a pie chart showing the proportion of each sleep disorder in the dataset.
# It provides insight into the most common sleep disorders among participants.
rt_count=sleep_data.groupby("Sleep Disorder").size()
print(rt_count)
y=rt_count.values
mylabels=rt_count.index

plt.pie(y, labels=mylabels)
plt.title("Sleep Disorders in dataset")
plt.show()

#This pie chart demontstrates the sleep disorders in the dataset. The 2 most common sleep disorders are Slepp Apnea and Insomnia which come out to almost 50% each.






    
    










