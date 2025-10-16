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

#Part 3: Loop + conditional filtering (keeps arrays aligned) ----------
age_f, sleep_duration_f, sleep_quality_f = [], [], []
stress_level_f, physical_activity_f = [], []
heart_rate_f, daily_steps_f = [], []

dropped = 0
for a, sd, sq, sl, hr, steps, pa in zip(
    age, sleep_duration, sleep_quality, stress_level, heart_rate, daily_steps, physical_activity
):
    keep = (
        (3 <= sd <= 12) and
        (1 <= sq <= 10) and
        (1 <= sl <= 10) and
        (40 <= hr <= 120) and
        (0 <= steps <= 50000) and
        (15 <= a <= 90) and
        (0 <= pa <= 100)
    )
    if keep:
        age_f.append(a)
        sleep_duration_f.append(sd)
        sleep_quality_f.append(sq)
        stress_level_f.append(sl)
        heart_rate_f.append(hr)
        daily_steps_f.append(steps)
        physical_activity_f.append(pa)
    else:
        dropped += 1

# Convert lists back to NumPy arrays
age_f = np.array(age_f)
sleep_duration_f = np.array(sleep_duration_f)
sleep_quality_f = np.array(sleep_quality_f)
stress_level_f = np.array(stress_level_f)
heart_rate_f = np.array(heart_rate_f)
daily_steps_f = np.array(daily_steps_f)
physical_activity_f = np.array(physical_activity_f)

print(f"\nFiltered rows dropped: {dropped}")
print(f"Kept rows: {len(sleep_duration_f)}")
print("Arrays aligned:", len(age_f), len(sleep_duration_f), len(sleep_quality_f),
      len(stress_level_f), len(heart_rate_f), len(daily_steps_f), len(physical_activity_f))

sleep_data_filtered = pd.DataFrame({
    "Age": age_f,
    "Sleep Duration": sleep_duration_f,
    "Quality of Sleep": sleep_quality_f,
    "Stress Level": stress_level_f,
    "Heart Rate": heart_rate_f,
    "Daily Steps": daily_steps_f,
    "Physical Activity Level": physical_activity_f
})
# Goal: keep only plausible, analysis-ready rows so we can study how
# sleep duration/quality relate to stress, health (heart rate), and activity.
