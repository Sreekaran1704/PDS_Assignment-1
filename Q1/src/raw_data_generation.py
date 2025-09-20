import os
import pandas as pd

data = {
    "Height": [65.8, 71.5, 69.4, 68.2, 67.8, 68.7, 69.8, 70.1, 67.9, 66.8],
    "Weight": [112, 136, 153, 142, 144, 123, 141, 136, 112, 120],
    "Age": [30, 19, 45, 22, 29, 50, 51, 23, 17, 39],
    "Grip strength": [30, 31, 29, 28, 24, 26, 22, 20, 19, 31],
    "Frailty": ["N", "N", "N", "Y", "Y", "N", "Y", "Y", "N", "N"]
}

# convert the data to a pandas dataframe
df = pd.DataFrame(data)

# get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

data_dir = os.path.join(script_dir, "..", "data/raw_data")
os.makedirs(data_dir, exist_ok=True) 

# create the csv file
csv_file = os.path.join(data_dir, "raw_data.csv")
# save the dataframe to the csv file
df.to_csv(csv_file, index=False)

print(f"Saved at: {csv_file}")