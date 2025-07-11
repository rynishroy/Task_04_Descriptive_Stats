import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = "period_03_data/2024_fb_posts_president_scored_anon.csv"
output_dir = "plots/fb_posts"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(file_path)

# Convert Likes to numeric if needed
if df["Likes"].dtype == object:
    df["Likes"] = pd.to_numeric(df["Likes"].str.replace(",", ""), errors='coerce')

# Histogram of Likes
sns.histplot(df["Likes"].dropna(), bins=50, kde=True)
plt.title("Distribution of Facebook Post Likes")
plt.xlabel("Likes")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(f"{output_dir}/likes_histogram.png")
plt.clf()

# Top 10 Page Categories
top_categories = df["Page Category"].value_counts().nlargest(10)
sns.barplot(x=top_categories.values, y=top_categories.index)
plt.title("Top 10 Facebook Page Categories")
plt.xlabel("Frequency")
plt.ylabel("Page Category")
plt.tight_layout()
plt.savefig(f"{output_dir}/page_category_barplot.png")
plt.clf()