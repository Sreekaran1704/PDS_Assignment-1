import os
import pandas as pd

df = pd.read_csv("../data/cleaned_data/cleaned_data.csv")


def new_df(df):
    df["test preparation course"] = df["test preparation course"].replace({
    "none": "not completed",
    "completed": "completed"
})
    return df



