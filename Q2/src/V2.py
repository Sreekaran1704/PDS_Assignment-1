import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import df

df1 = df.copy()

figsize = (800/300) , (600/300)
dpi = 300

plt.figure(figsize=figsize, dpi=dpi)

sns.boxplot(x='math score', y='test preparation course', data=df1)
plt.title("Math Scores by Test Preparation Course")
plt.xlabel("Math Score")
plt.ylabel("Test Preparation Course")

script_dir = os.path.dirname(os.path.abspath(__file__))
reports_dir = os.path.join(script_dir, "..", "reports")
os.makedirs(reports_dir, exist_ok=True)

plots_dir = os.path.join(script_dir, "..", "plots")
plot_file = os.path.join(plots_dir, "V2.png")
plt.savefig(plot_file, dpi=300, bbox_inches="tight")

report_file = os.path.join(reports_dir, "Data_Visualizations_with_interpretation.md")
with open(report_file, "a") as f:
    f.write("\n")
    f.write("Data Visualization 2 with it's interpretation: \n")
    f.write("--------------------------------\n")
    f.write("![Math Scores by Test Preparation Course](../plots/V2.png)\n")
    f.write("\n")
    f.write("Interpretation: \n")
    f.write("By analysing this boxplot we can clearly see a substantial benefit of completing the test preparation course on math performance. i.e. Students who completed the course achieved a much higher median score compared to those who did not, making a improvement in central performance. Their scores are also more tightly clustered, indicating greater consistency at a higher level of achievement. On the other hand, non-completers displayed both a lower median and a wider score spread, with the majority falling between the lowest score than the ones completed ones. This highlights not only weaker overall performance but also less predictability in outcomes.")
    f.write("\n")



