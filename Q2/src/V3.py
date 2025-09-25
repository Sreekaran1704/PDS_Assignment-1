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
report_file = os.path.join(reports_dir, "V3.png")
plt.savefig(report_file, dpi=300, bbox_inches="tight")
plt.show()




