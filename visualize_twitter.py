import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = "period_03_data/2024_tw_posts_president_scored_anon.csv"
output_dir = "plots/twitter"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(file_path)

# Histogram of Like Count
sns.histplot(df["likeCount"], bins=50, kde=True)
plt.title("Distribution of Twitter Likes")
plt.xlabel("Likes")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(f"{output_dir}/likes_histogram.png")
plt.clf()

# Top 10 Sources
top_sources = df["source"].value_counts().nlargest(10)
sns.barplot(x=top_sources.values, y=top_sources.index)
plt.title("Top 10 Tweet Sources")
plt.xlabel("Frequency")
plt.ylabel("Source")
plt.tight_layout()
plt.savefig(f"{output_dir}/source_barplot.png")
plt.clf()
