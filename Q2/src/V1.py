import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import df


df1 = df.copy()

figsize = (800/300) , (600/300)
dpi = 300

df_melted = df.melt(
    id_vars=['gender'],
    value_vars=['math score', 'reading score'],
    var_name="Subject",
    value_name="Score"
)

fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

sns.boxplot(
    x='Subject',
    y="Score",
    hue="gender",  # Change hue to gender
    data=df_melted,
    palette="Set2",
    width=0.5,
    ax=ax
)

ax.set_title("Math and Reading Scores by Gender", fontsize=8, weight="bold", pad=4)
ax.set_xlabel("Subject", fontsize=7)  # Change xlabel to Subject
ax.set_ylabel("Score", fontsize=7)


ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)


ax.legend(
    title="Gender", # Change legend title to Gender
    fontsize=3, title_fontsize=4,
    frameon=False,
    loc="upper left", bbox_to_anchor=(1.05, 1)
)

sns.despine()
plt.tight_layout(pad=0.5)


script_dir = os.path.dirname(os.path.abspath(__file__))
reports_dir = os.path.join(script_dir, "..", "reports")
os.makedirs(reports_dir, exist_ok=True)

# Save the plot as PNG
plots_dir = os.path.join(script_dir, "..", "plots")
os.makedirs(plots_dir, exist_ok=True)
plot_file = os.path.join(plots_dir, "V1.png")
plt.savefig(plot_file, dpi=300, bbox_inches="tight")

# Create markdown report
report_file = os.path.join(reports_dir, "Data_Visualizations_with_interpretation.md")
with open(report_file, "w") as f:
    f.write("Data Visualization 1 with it's interpretation: \n")
    f.write("--------------------------------\n")
    f.write("![Math and Reading Scores by Gender](../plots/V1.png)\n")
    f.write("\n")
    f.write("Interpretation: \n")
    f.write("In Math Scores males exhibit slightly higher median math scores compared to females. The distribution also shows that males tend to achieve both higher maximum scores and higher minimum scores, indicating stronger performance across the range. Females, on the other hand, display a wider spread with more low-end outliers, suggesting greater variability in performance.")
    f.write("\n")
    f.write("\n")
    f.write("Whereas coming to Reading Scores the trend reverses in reading,i.e.females outperform males on average and females have a higher median score and a wider interquartile range (IQR) skewed towards higher values, showing that many achieve top-end performance. However, females also display some of the lowest outliers, pulling their minimum scores below those of males, While, in males reading scores are more tightly distributed, but generally lower than females at the top end.")
    f.write("\n")






