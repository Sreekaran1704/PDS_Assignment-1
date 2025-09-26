import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import df

df1 = df.copy()

figsize = (800/300) , (600/300)
dpi = 300

plt.figure(figsize=figsize, dpi=300)

corr = df[['math score', 'reading score', 'writing score']].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation matrix")

script_dir = os.path.dirname(os.path.abspath(__file__))
reports_dir = os.path.join(script_dir, "..", "reports")
os.makedirs(reports_dir, exist_ok=True)

plots_dir = os.path.join(script_dir, "..", "plots")
plot_file = os.path.join(plots_dir, "V4.png")
plt.savefig(plot_file, dpi=300, bbox_inches="tight")

report_file = os.path.join(reports_dir, "Data_Visualizations_with_interpretation.md")
with open(report_file, "a") as f:
    f.write("\n")
    f.write("Data Visualization 4 with it's interpretation: \n")
    f.write("--------------------------------\n")
    f.write("![Correlation matrix](../plots/V4.png)\n")
    f.write("\n")
    f.write("Interpretation: \n")
    f.write("This correlation matrix highlights strong positive associations among math, reading, and writing scores, with coefficients ranging from 0.80 to 0.95. This indicates that students who excel in one subject are highly likely to perform well in others, reflecting a strong underlying general academic ability.")
    f.write("\n")
    f.write("\n")
    f.write("Math, while still highly correlated with reading (r = 0.82) and writing (r = 0.80), emerges as the most distinct domain. This slightly weaker relationship suggests that math incorporates additional domain-specific skills such as abstract reasoning, numerical fluency, and quantitative problem-solving.")
    f.write("\n")

