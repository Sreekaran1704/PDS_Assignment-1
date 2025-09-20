import os
import pandas as pd
from categorical_to_numerical_encoding import df2
from scipy.stats import pointbiserialr

def reporting(df2):
    summary = (
        df2.select_dtypes(include="number")
        .agg(["mean", "median", "std"])
        .T
    )
    print(summary)
    return summary

def find_correlation(df2):
    corr, p_value = pointbiserialr(df2["Frailty"], df2["Grip strength"])

    print("Correlation:", corr)
    print("P-value:", p_value)

    return corr, p_value

summary = reporting(df2)

with open("../log/complete_log.txt", "a") as f:
    f.write("Reporting Started: \n")
    f.write("Finding the mean, median, and standard deviation of the numerical columns: \n")
    f.write(summary.to_string())
    f.write("\n")
    f.write("--------------------------------\n")

corr, p_value = find_correlation(df2)
with open("../log/complete_log.txt", "a") as f:
    f.write("Finding the correlation between the Frailty and Grip_strength(kg) columns: \n")
    f.write(f"Correlation: {corr}")
    f.write("\n")
    f.write(f"P-value: {p_value}")
    f.write("\n")
    f.write("--------------------------------\n")

script_dir = os.path.dirname(os.path.abspath(__file__))
reports_dir = os.path.join(script_dir, "..", "reports")
os.makedirs(reports_dir, exist_ok=True)

report_file = os.path.join(reports_dir, "findings.md")
with open(report_file, "w") as f:
    f.write("## Findings \n")
    f.write('The mean, median, and standard deviation of the numerical columns are as follows: \n')
    f.write(summary.to_string())
    f.write("\n")
    f.write("--------------------------------\n")
    f.write("The correlation between the Frailty and Grip_strength(kg) columns is as follows: \n")
    f.write(f"Correlation: {corr}")
    f.write("\n")
    f.write(f"P-value: {p_value}")
    f.write("\n")
    f.write("--------------------------------\n")

report2 = os.path.join(reports_dir, "Strength_and_Frailty_Correlation.md")
with open(report2, "w") as f:
    f.write("## Strength and Frailty Correlation \n")
    f.write("The correlation between the Frailty and Grip_strength(kg) columns is as follows: \n")
    f.write(f"Correlation: {corr}")
    f.write("\n")
    f.write(f"P-value: {p_value}")
    f.write("\n")
    f.write("--------------------------------\n")