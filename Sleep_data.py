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
#Skip BMI category
bmi = sleep_data["BMI Category"]  # this one is text, so we'll skip for now
#Include heart rate and daily steps as numeric arrays
heart_rate = sleep_data["Heart Rate"].to_numpy()
daily_steps = sleep_data["Daily Steps"].to_numpy()

# Part 3: Clean and filter dataset for our project

# 1. Remove unnecessary columns that are not relevant to our analysis
columns_to_drop = [
    "Person ID",         # Identification only, not analytical
    "Occupation",        # Not relevant to sleep-stress link
    "BMI Category",      # Only matters for obesity-focused research
    "Blood Pressure"     # Too specific for our study
]
sleep_data = sleep_data.drop(columns=columns_to_drop, errors="ignore")

# 2. Keep only columns that are relevant to our research questions
columns_to_keep = [
    "Gender",
    "Age",
    "Sleep Duration",
    "Quality of Sleep",
    "Stress Level",
    "Heart Rate",
    "Daily Steps",
    "Sleep Disorder"
]
sleep_data = sleep_data[columns_to_keep]

# ---------- Part 3: Manipulating the data ----------

# remove unnecessary columns
sleep_data = sleep_data.drop(["Person ID", "Occupation", "BMI Category", "Blood Pressure"], axis=1, errors="ignore")

# use a loop and conditional to remove duplicates
unique_rows = []
for i in range(len(sleep_data)):
    if list(sleep_data.iloc[i]) not in unique_rows:
        unique_rows.append(list(sleep_data.iloc[i]))

# rebuild the dataset without duplicates
clean = pd.DataFrame(unique_rows, columns=sleep_data.columns)

print("Rows before filtering:", len(sleep_data))
print("Rows after removing duplicates:", len(clean))
print("Final columns:", list(clean.columns))
print(clean.head())

# after you build `clean`
clean.to_csv("Sleep_data_clean.csv", index=False)