# Task_04_Descriptive_Stats

## Objective
This project explores descriptive statistics of social media activity during the 2024 US presidential election using three approaches:

- Pure Python (no external libraries)
- Pandas
- Polars

The datasets include Facebook ads, Facebook posts, and Twitter posts. Each script analyzes all three datasets for counts, means, unique values, and grouped statistics.

---

## 📁 Dataset Used
**Note:** These datasets must **NOT** be committed to your GitHub repo. Provide only links.

Download from:  
🔗 [period_03.zip - Google Drive](https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view?usp=sharing)

Extracted files include:
- `2024_fb_ads_president_scored_anon.csv`
- `2024_fb_posts_president_scored_anon.csv`
- `2024_tw_posts_president_scored_anon.csv`

---

## Files Included

| File | Description |
|------|-------------|
| `pure_python_stats.py` | Base Python approach for all 3 datasets |
| `pandas_stats.py` | Analysis using Pandas |
| `polars_stats.py` | Analysis using Polars |
| `.gitignore` | Prevents committing data and temp files |
| `README.md` | Documentation and instructions |

---

##  How to Run

Install required libraries:
```bash
pip install pandas polars

python pure_python_stats.py
python pandas_stats.py
python polars_stats.py

---

## 📁 Dataset Used
**Do not include this dataset in the repository.**

**Download from:**  
[period_03.zip - Google Drive](https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view?usp=sharing)

This dataset includes:
- Facebook ads
- Facebook posts
- Twitter posts

The Facebook ads dataset (2024_fb_ads_president_scored_anon.csv) has 41 columns, including:
page_id, ad_id
ad_creation_time

Categorical: bylines, currency

Nested JSON-like: delivery_by_region, demographic_distribution

Numeric: estimated_spend, estimated_impressions, estimated_audience_size, and various _illuminating topic scores

## Summary of Findings

### Facebook Ads:
- Most ads were sponsored in USD, with **"HARRIS FOR PRESIDENT"** being the most frequent byline.
- **Ad spending** and **impressions** were highly skewed, with a few ads receiving significantly higher engagement.
- Over **140,000 unique delivery regions** and **215,000 unique demographic profiles** indicate highly targeted campaigning.

### Facebook Posts:
- The majority of pages were categorized under **"PERSON"** or **"POLITICAL_CANDIDATE"**.
- Likes ranged from double digits to over 100,000 — suggesting large variation in public engagement.
- Video content (especially Live Video) tended to receive higher interaction counts than photos or links.

### Twitter Posts:
- Most tweets were posted via **"Twitter for iPhone"**, followed by **"Twitter Web App"**.
- Engagement (likes, retweets, views) followed a long-tail distribution, with a small number of tweets going viral.
- The majority of tweets were written in English (`lang = en`), and topic flags such as **"incivility"** and **"scam"** were infrequently triggered.
