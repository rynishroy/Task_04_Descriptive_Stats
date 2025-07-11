import polars as pl

def analyze_with_polars(filepath):
    df = pl.read_csv(filepath)

    print("\n--- GENERAL STATISTICS ---")
    print(df.describe())

    print("\n--- UNIQUE VALUES FOR CATEGORICAL COLUMNS ---")
    for col in df.columns:
        if df[col].dtype == pl.Utf8:
            uniques = df[col].n_unique()
            most_common_df = df[col].value_counts().sort("count", descending=True)
            most_common = most_common_df[0, col] if most_common_df.shape[0] > 0 else "N/A"
            print(f"{col}: unique={uniques}, most_frequent={most_common}")

    numeric_cols = [col for col in df.columns if df[col].dtype in [pl.Float64, pl.Int64]]

    if "page_id" in df.columns:
        print("\n--- GROUPED BY page_id ---")
        group1 = df.group_by("page_id").agg(
            [pl.count()] + [pl.mean(col).alias(f"{col}_mean") for col in numeric_cols]
        )
        print(group1.head())

    if "page_id" in df.columns and "ad_id" in df.columns:
        print("\n--- GROUPED BY page_id AND ad_id ---")
        group2 = df.group_by(["page_id", "ad_id"]).agg(
            [pl.count()] + [pl.mean(col).alias(f"{col}_mean") for col in numeric_cols]
        )
        print(group2.head())

# Run for all datasets
print("=== FACEBOOK ADS ===")
analyze_with_polars("period_03_data/2024_fb_ads_president_scored_anon.csv")
print("\n\n=== FACEBOOK POSTS ===")
analyze_with_polars("period_03_data/2024_fb_posts_president_scored_anon.csv")
print("\n\n=== TWITTER POSTS ===")
analyze_with_polars("period_03_data/2024_tw_posts_president_scored_anon.csv")
