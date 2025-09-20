import pandas as pd
from feature_engineering import df1
from sklearn.preprocessing import OneHotEncoder

def categorical_to_numerical_encoding(df1):
    df1["Frailty"] = df1["Frailty"].map({"N": 0, "Y": 1})
    return df1

def one_hot_encoding(df1):
    df1 = pd.concat([df1.drop(columns=["Age_Category"]),
                pd.DataFrame((enc := OneHotEncoder(sparse_output=False).fit(df1[["Age_Category"]])).transform(df1[["Age_Category"]]),
                             columns=enc.get_feature_names_out(["Age_Category"]),
                             index=df1.index)], axis=1)
    return df1


df2 = df1.copy()
df2 = categorical_to_numerical_encoding(df2)
with open("../log/complete_log.txt", "a") as f:
    f.write("The column Frailty is being converted to numerical encoding: \n")
    f.write("Categorical to Numerical Encoding Started: \n")
    f.write(df1.to_string())
    f.write("\n")
    f.write("--------------------------------\n")

df2 = one_hot_encoding(df2)
with open("../log/complete_log.txt", "a") as f:
    f.write("The column Age_Category is being converted to one hot encoding: \n")
    f.write("One Hot Encoding Started: \n")
    f.write(df1.to_string())
    f.write("\n")
    f.write("--------------------------------\n")

def final_data_frame2(df2):
    return df2
