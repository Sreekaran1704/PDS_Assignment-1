from math import log
import os
import pandas as pd

df1 = pd.read_csv("../data/raw_data/raw_data.csv")

print(df1.head())

null_summary =df1.isnull().sum()
print(null_summary)

# get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

data_dir = os.path.join(script_dir, "..", "data/cleaned_data")
log_dir = os.path.join(script_dir, "..", "log")
os.makedirs(data_dir, exist_ok=True) 

# create the csv file
csv_file = os.path.join(data_dir, "cleaned_data.csv")
# save the dataframe to the csv file
df1.to_csv(csv_file, index=False)

print(f"Saved at: {csv_file}")

#Saving the null summary to a text file for logging and reference
log_file = os.path.join(data_dir, "null_values_summary_table.txt")
log_file1 = os.path.join(log_dir, "complete_log.txt")

with open(log_file, "w") as f:
    f.write("Null Values Summary: \n")
    f.write(null_summary.to_string())

print(f"Null values summary saved at: {log_file}")

with open(log_file1, "w") as f:
    f.write("Data Cleaning Started : \n")
    f.write ("Calculating Null values at each column: \n")
    f.write(null_summary.to_string())
    f.write("\n")
    f.write("--------------------------------\n")

print(f"Null values summary saved at: {log_file1}")