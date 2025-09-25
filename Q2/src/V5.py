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
report_file = os.path.join(reports_dir, "V5.png")
plt.savefig(report_file, dpi=300, bbox_inches="tight")
plt.show()

