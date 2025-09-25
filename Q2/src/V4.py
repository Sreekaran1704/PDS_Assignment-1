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
report_file = os.path.join(reports_dir, "V4.png")
plt.savefig(report_file, dpi=300, bbox_inches="tight")
plt.show()

