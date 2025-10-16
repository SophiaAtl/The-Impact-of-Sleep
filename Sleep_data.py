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

# 3. Filter out unrealistic or implausible values
mask = (
    sleep_data["Age"].between(18, 70) &
    sleep_data["Sleep Duration"].between(4.0, 10.0) &
    sleep_data["Quality of Sleep"].between(2, 10) &
    sleep_data["Stress Level"].between(1, 10) &
    sleep_data["Heart Rate"].between(45, 110) &
    sleep_data["Daily Steps"].between(1000, 20000)
)

filtered = sleep_data.loc[mask].copy()

#Print summary of filtering results
print(f"\nFiltered rows dropped: {dropped}")
print(f"Kept rows: {len(sleep_duration_f)}")
print("Arrays aligned:", len(age_f), len(sleep_duration_f), len(sleep_quality_f),
      len(stress_level_f), len(heart_rate_f), len(daily_steps_f), len(physical_activity_f))

#Create a cleaned DataFrame with only valid rows
sleep_data_filtered = pd.DataFrame({
    "Age": age_f,
    "Sleep Duration": sleep_duration_f,
    "Quality of Sleep": sleep_quality_f,
    "Stress Level": stress_level_f,
    "Heart Rate": heart_rate_f,
    "Daily Steps": daily_steps_f,
    "Physical Activity Level": physical_activity_f
})
# Goal: keep only plausible, analysis-ready rows so we can study how sleep duration/quality relates to stress, health (heart rate), and activity.
