import pandas as pd

def analyze_with_pandas(filepath):
    df = pd.read_csv(filepath)

    print(f"\n--- GENERAL STATISTICS ---")
    print(df.describe(include='all'))

    print(f"\n--- UNIQUE VALUES FOR CATEGORICAL COLUMNS ---")
    for col in df.select_dtypes(include='object'):
        unique_vals = df[col].nunique()
        top_val = df[col].value_counts().idxmax()
        print(f"{col}: unique={unique_vals}, most_frequent={top_val}")

    numeric_cols = df.select_dtypes(include=['number']).columns

    print(f"\n--- GROUPED BY page_id ---")
    if 'page_id' in df.columns:
        grouped_page = df.groupby('page_id')[numeric_cols].agg(['count', 'mean', 'min', 'max'])
        print(grouped_page.head())

    print(f"\n--- GROUPED BY page_id AND ad_id ---")
    if 'page_id' in df.columns and 'ad_id' in df.columns:
        grouped_page_ad = df.groupby(['page_id', 'ad_id'])[numeric_cols].agg(['count', 'mean', 'min', 'max'])
        print(grouped_page_ad.head())

# Run for all datasets
print("=== FACEBOOK ADS ===")
analyze_with_pandas("period_03_data/2024_fb_ads_president_scored_anon.csv")
print("\n\n=== FACEBOOK POSTS ===")
analyze_with_pandas("period_03_data/2024_fb_posts_president_scored_anon.csv")
print("\n\n=== TWITTER POSTS ===")
analyze_with_pandas("period_03_data/2024_tw_posts_president_scored_anon.csv")
