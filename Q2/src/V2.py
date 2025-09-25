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
plt.show()

script_dir = os.path.dirname(os.path.abspath(__file__))
reports_dir = os.path.join(script_dir, "..", "reports")
os.makedirs(reports_dir, exist_ok=True)
report_file = os.path.join(reports_dir, "V2.png")
plt.savefig(report_file, dpi=300, bbox_inches="tight")
plt.show()

