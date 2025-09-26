import os
import pandas as pd


df = pd.read_csv("../data/raw_data/Students Performance.csv")

null_summary = df.isnull().sum()

print(df['gender'].value_counts())
print('\n')
print(df['parental level of education'].value_counts())
print('\n')
print(df['race/ethnicity'].value_counts())
print('\n')
print(df['lunch'].value_counts())
print('\n')
print(df['test preparation course'].value_counts())
print('\n')

print(df['gender'].dtype)
print(df['parental level of education'].dtype)
print(df['race/ethnicity'].dtype)
print(df['lunch'].dtype)
print(df['test preparation course'].dtype)
print(df['math score'].dtype)
print(df['reading score'].dtype)
print(df['writing score'].dtype)

script_dir = os.path.dirname(os.path.abspath(__file__))

data_dir = os.path.join(script_dir, "..", "data/cleaned_data")
log_dir = os.path.join(script_dir, "..", "log")
os.makedirs(log_dir, exist_ok=True) 
os.makedirs(data_dir, exist_ok=True) 

csv_file = os.path.join(data_dir, "cleaned_data.csv")
df.to_csv(csv_file, index=False)
print(f"Saved at: {csv_file}")

log_file = os.path.join(log_dir, "complete_log.txt")
with open(log_file, "w") as f:
    f.write("Data Cleaning Started: \n")
    f.write(null_summary.to_string())
    f.write("\n")
    f.write("--------------------------------\n")

print(f"Null values summary saved at: {log_file}")

with open(log_file, "a") as f:
    f.write("Value counts for seeing if any errors in the columns like any anamolies or any other issues: \n")
    f.write(df['gender'].value_counts().to_string())
    f.write("\n")
    f.write("--------------------------------\n")
    f.write(df['parental level of education'].value_counts().to_string())
    f.write("\n")
    f.write("--------------------------------\n")
    f.write(df['race/ethnicity'].value_counts().to_string())
    f.write("\n")
    f.write("--------------------------------\n")
    f.write(df['lunch'].value_counts().to_string())
    f.write("\n")
    f.write("--------------------------------\n")
    f.write(df['test preparation course'].value_counts().to_string())
    f.write("\n")
    f.write("--------------------------------\n")

with open(log_file, "a") as f:
    f.write("Checking all the data types to see if there are any errors: \n")
    f.write('Gender Data Type:')
    f.write(str(df['gender'].dtype))
    f.write("\n")
    f.write('Parental Level of Education Data Type:')
    f.write(str(df['parental level of education'].dtype))
    f.write("\n")
    f.write('Race/Ethnicity Data Type:')
    f.write(str(df['race/ethnicity'].dtype))
    f.write("\n")
    f.write('Lunch Data Type:')
    f.write(str(df['lunch'].dtype))
    f.write("\n")
    f.write('Test Preparation Course Data Type:')
    f.write(str(df['test preparation course'].dtype))
    f.write("\n")
    f.write('Math Score Data Type:')
    f.write(str(df['math score'].dtype))
    f.write("\n")
    f.write('Reading Score Data Type:')
    f.write(str(df['reading score'].dtype))
    f.write("\n")
    f.write('Writing Score Data Type:')
    f.write(str(df['writing score'].dtype))
    f.write("\n")


