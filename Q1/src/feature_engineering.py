import pandas as pd
from unit_standardization import df1

def Add_BMI_Column(df1):
    df1['BMI'] = df1['Weight(kg)']/df1['Height(m)']*df1['Height(m)']
    df1['BMI'] = df1['BMI'].round(2)
    return df1

def divide_age_into_categories(age):
    if age < 30:
      return "<30"
    elif age >= 30 and age <= 45:
      return "30-40"
    elif age > 45 and age <= 60:
      return "45-60"
    else:
      return ">60"

def Add_Age_Category_Column(df1):
    df1.insert(3, "Age_Category", df1["Age"].apply(divide_age_into_categories))
    return df1


df1 = Add_BMI_Column(df1)
with open("../log/complete_log.txt", "a") as f:
    f.write("Feature Engineering Started: \n")
    f.write("BMI Column Added: \n")
    f.write(df1.to_string())
    f.write("\n")
    f.write("--------------------------------\n")


df1 = Add_Age_Category_Column(df1)
with open("../log/complete_log.txt", "a") as f:
    f.write("Age Column is being divided into categories and added as a new column: \n")
    f.write(df1.to_string())
    f.write("\n")
    f.write("--------------------------------\n")

with open("../log/complete_log.txt", "a") as f:
    f.write("Final Data Frame after Feature Engineering: \n")
    f.write(df1.to_string())
    f.write("\n")
    f.write("--------------------------------\n")

def final_data_frame(df1):
    return df1