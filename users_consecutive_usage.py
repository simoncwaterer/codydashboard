import csv
import pandas as pd
from datetime import datetime, timedelta

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Customer Cody user-level usage table with dates (v2 events) 2024-06-27T1134.csv')
df = df.dropna(subset=['Instance user ID'])

# Convert the 'date' column to datetime format
df['Timestamp Date'] = pd.to_datetime(df['Timestamp Date'])
# Convert the 'Instance user ID' column from float to int
df['Instance user ID'] = df['Instance user ID'].astype(int)

# Remove rows where all event counts are zero
df = df[(df['Chat Events'] != 0) | (df['Command Events'] != 0) | (df['Combined Completion Suggestions'] != 0)]

# Find user_ids with entries for 3 consecutive days
user_ids_with_consecutive_days = []
for user_id, group in df.groupby('Instance user ID'):
    dates = group['Timestamp Date'].sort_values().tolist()
    for i in range(len(dates) - 2):
        if (dates[i+1] - dates[i]) == timedelta(days=1) and (dates[i+2] - dates[i+1]) == timedelta(days=1):
            user_ids_with_consecutive_days.append(user_id)
            break

# Write the user_ids with entries for 3 consecutive days to a CSV file
with open('user_ids_with_consecutive_days.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['user_id'])
    for user_id in user_ids_with_consecutive_days:
        writer.writerow([user_id])

# How large is the set of user ids
print("Number of user ids with entries for 3 consecutive days:")
print(len(set(user_ids_with_consecutive_days)))

# How many user ids are there in the original data set
print("Number of user ids in the original data set:")
print(len(set(df['Instance user ID'])))