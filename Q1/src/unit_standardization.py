import pandas as pd

def unit_standardization(df1):
    df1.rename(columns={"Height": "Height(m)"}, inplace=True)
    df1['Height(m)'] = df1['Height(m)']*0.0254
    df1.rename(columns={"Weight": "Weight(kg)"}, inplace=True)
    df1['Weight(kg)'] = df1['Weight(kg)']*0.453592
    df1.rename(columns={"Grip_strength": "Grip_strength(kg)"}, inplace=True)
    return df1

df1 = pd.read_csv("../data/cleaned_data/cleaned_data.csv")
df1 = unit_standardization(df1)

with open("../log/complete_log.txt", "a") as f:
    f.write("Unit Standardization Started: \n")
    f.write("Data frame after unit standardization: \n")
    f.write(df1.to_string())
    f.write("\n Unit Standardization Completed \n")
    f.write("--------------------------------\n")
