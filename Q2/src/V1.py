import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import df


df1 = df.copy()

figsize = (800/300) , (600/300)
dpi = 300

df_melted = df1.melt(
    id_vars=['gender'],
    value_vars=['math score', 'reading score'],
    var_name="Subject",
    value_name="Score"
)

fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

sns.boxplot(
    x='gender',
    y="Score",
    hue="Subject",
    data=df_melted,
    palette="Set2",
    width=0.5,
    ax=ax
)

ax.set_title("Math and Reading Scores by Gender", fontsize=8, weight="bold", pad=4)
ax.set_xlabel("Gender", fontsize=7)
ax.set_ylabel("Score", fontsize=7)


ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)


ax.legend(
    title="Subject",
    fontsize=3, title_fontsize=4,
    frameon=False,
    loc="upper left", bbox_to_anchor=(1.05, 1)
)

sns.despine()
plt.tight_layout(pad=0.5)


script_dir = os.path.dirname(os.path.abspath(__file__))
reports_dir = os.path.join(script_dir, "..", "reports")
os.makedirs(reports_dir, exist_ok=True)
report_file = os.path.join(reports_dir, "V1.png")
plt.savefig(report_file, dpi=300, bbox_inches="tight")
plt.show()




