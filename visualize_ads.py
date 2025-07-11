import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
file_path = "period_03_data/2024_fb_ads_president_scored_anon.csv"
output_dir = "plots/ads"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(file_path)

# Histogram of Estimated Spend
sns.histplot(df["estimated_spend"], bins=50, kde=True)
plt.title("Distribution of Estimated Ad Spend")
plt.xlabel("Estimated Spend")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(f"{output_dir}/estimated_spend_histogram.png")
plt.clf()

# Top 10 Bylines
top_bylines = df["bylines"].value_counts().nlargest(10)
sns.barplot(x=top_bylines.values, y=top_bylines.index)
plt.title("Top 10 Ad Sponsors (Bylines)")
plt.xlabel("Number of Ads")
plt.ylabel("Byline")
plt.tight_layout()
plt.savefig(f"{output_dir}/top_bylines_barplot.png")
plt.clf()

# Histogram of Estimated Impressions
sns.histplot(df["estimated_impressions"], bins=50, kde=True)
plt.title("Distribution of Estimated Impressions")
plt.xlabel("Impressions")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(f"{output_dir}/estimated_impressions_histogram.png")
plt.clf()