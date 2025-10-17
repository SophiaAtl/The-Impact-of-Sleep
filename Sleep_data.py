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


filtered = sleep_data.loc[mask].copy()

print(f"Rows before filtering: {len(sleep_data)}")
print(f"Rows after filtering unrealistic values: {len(filtered)}")

# 4. Remove duplicate rows if any exist
filtered = filtered.drop_duplicates()
print(f"Rows after removing duplicates: {len(filtered)}")

# 5. Update dataset to use the cleaned version
sleep_data = filtered.reset_index(drop=True)

# 6. Display summary of final dataset
print("Final dataset shape:", sleep_data.shape)
print("Final columns:", list(sleep_data.columns))
print(sleep_data.head())

