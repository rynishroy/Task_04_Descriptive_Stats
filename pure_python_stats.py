import csv
import math
from collections import defaultdict, Counter

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

def compute_stats(data):
    numeric = defaultdict(list)
    non_numeric = defaultdict(list)

    for row in data:
        for key, val in row.items():
            if is_float(val):
                numeric[key].append(float(val))
            else:
                non_numeric[key].append(val)

    print("\n--- NUMERIC COLUMNS ---")
    for col, values in numeric.items():
        count = len(values)
        mean = sum(values) / count if count else 0
        min_val = min(values)
        max_val = max(values)
        stddev = math.sqrt(sum((x - mean) ** 2 for x in values) / count) if count else 0
        print(f"{col}: count={count}, mean={mean:.2f}, min={min_val}, max={max_val}, stddev={stddev:.2f}")

    print("\n--- NON-NUMERIC COLUMNS ---")
    for col, values in non_numeric.items():
        freq = Counter(values)
        most_common = freq.most_common(1)[0] if freq else ("N/A", 0)
        unique_count = len(freq)
        print(f"{col}: unique={unique_count}, most_frequent={most_common[0]} ({most_common[1]} times)")

def load_csv(path):
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

print("=== FACEBOOK ADS ===")
data = load_csv("period_03_data/2024_fb_ads_president_scored_anon.csv")
compute_stats(data)

print("\n\n=== FACEBOOK POSTS ===")
data = load_csv("period_03_data/2024_fb_posts_president_scored_anon.csv")
compute_stats(data)

print("\n\n=== TWITTER POSTS ===")
data = load_csv("period_03_data/2024_tw_posts_president_scored_anon.csv")
compute_stats(data)
