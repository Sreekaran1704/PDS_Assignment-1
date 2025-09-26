import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import df

df1 = df.copy()

g = sns.lmplot(
    x="reading score",
    y="writing score",
    data=df1,
    hue="test preparation course",
    height = 600 / 300 ,
    aspect = (800 / 300) / (600 / 300),
    palette="Set2",
)

g.set_axis_labels("Reading Score", "Writing Score")
plt.title("Reading Score vs Writing Score")

# Build mapping for legend labels with counts
counts = df1["test preparation course"].value_counts()
label_map = {
    "not completed": f"not completed (n={counts['not completed']})",
    "completed": f"completed (n={counts['completed']})"
}

# Remove the default seaborn legend
g._legend.remove()

# Add custom legend
handles, labels = g.axes[0,0].get_legend_handles_labels()
new_labels = [label_map[label] for label in labels]
plt.legend(handles, new_labels, title="test preparation course")

script_dir = os.path.dirname(os.path.abspath(__file__))
reports_dir = os.path.join(script_dir, "..", "reports")
os.makedirs(reports_dir, exist_ok=True)

plots_dir = os.path.join(script_dir, "..", "plots")
plot_file = os.path.join(plots_dir, "V5.png")
plt.savefig(plot_file, dpi=300, bbox_inches="tight")

report_file = os.path.join(reports_dir, "Data_Visualizations_with_interpretation.md")
with open(report_file, "a") as f:
    f.write("\n")
    f.write("Data Visualization 5 with it's interpretation: \n")
    f.write("--------------------------------\n")
    f.write("![Reading Score vs Writing Score](../plots/V5.png)\n")
    f.write("\n")
    f.write("Interpretation: \n")
    f.write("The Scatter Plot shows strong positive linear relationship between reading and writing scores.So,the students who perform well in reading also perform well in writing.")
    f.write("\n")
    f.write("\n")
    f.write("When considering the effect of test preparation, the slopes of the regression lines for completers and non-completers are nearly identical, showing that the underlying relationship between reading and writing remains consistent regardless of test prep. However, the slightly higher intercept for course completers suggests a consistent advantage: at any given level of reading proficiency, students who completed the course tend to achieve marginally higher writing scores.")
    f.write("\n")
