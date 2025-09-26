import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import df


df2 = df.copy()
df2['Avg_score'] = df2[['math score', 'reading score', 'writing score']].mean(axis=1)
df2['Avg_score'] = df2['Avg_score'].round(2)

figsize = (800/300) , (600/300)
dpi = 300

plt.figure(figsize=figsize, dpi=300)

sns.barplot(x = 'lunch', y= 'Avg_score', data=df2)
plt.title("Average score by lunch")
plt.xlabel("Lunch")
plt.ylabel("Average score")

script_dir = os.path.dirname(os.path.abspath(__file__))
reports_dir = os.path.join(script_dir, "..", "reports")
os.makedirs(reports_dir, exist_ok=True)

plots_dir = os.path.join(script_dir, "..", "plots")
plot_file = os.path.join(plots_dir, "V3.png")
plt.savefig(plot_file, dpi=300, bbox_inches="tight")

report_file = os.path.join(reports_dir, "Data_Visualizations_with_interpretation.md")
with open(report_file, "a") as f:
    f.write("\n")
    f.write("Data Visualization 3 with it's interpretation: \n")
    f.write("--------------------------------\n")
    f.write("![Average score by lunch](../plots/V3.png)\n")
    f.write("\n")
    f.write("Interpretation: \n")
    f.write("By analysing this barplot we can clearly see a performance gap in average scores between students based on lunch type. i.e.Students receiving a standard lunch consistently achieve higher mean scores across subjects compared to those on free or reduced lunch programs. This suggests that access to standard lunch may be associated with better academic outcomes")
    f.write("\n")



