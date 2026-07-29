# Retail Sales Data Analysis

A Python project that analyzes a retail sales dataset to find revenue
trends, top-performing products, and seasonal patterns — built with
Pandas, NumPy, and Matplotlib, using a simple OOP structure.

## Files
- `generate_data.py` — creates a synthetic (but realistic) retail sales
  dataset with intentional messiness (missing values, duplicates, bad
  entries), saved to `data/retail_sales.csv`.
- `analysis.py` — the main project. Contains the `SalesAnalyzer` class
  that cleans the data and computes insights.
- `output/` — saved charts (`monthly_trend.png`, `top_products.png`,
  `category_distribution.png`).

## How to run
```bash
pip install pandas numpy matplotlib
python generate_data.py   # creates the dataset (only needed once)
python analysis.py        # runs cleaning + analysis + saves charts
```

## What the code actually does (read this before your interview)

### 1. Data Cleaning (`clean_data`)
- Drops exact duplicate rows.
- Drops rows where `Quantity` is missing (can't calculate revenue
  without it).
- Removes rows with negative/zero `Quantity` (bad data entries).
- Fills missing `Region` with `"Unknown"` instead of deleting the sale
  — you don't want to lose real revenue data just because one field
  is missing.
- Recalculates `Revenue = Quantity * UnitPrice` so the numbers are
  always internally consistent.

**Why this matters in an interview:** Data cleaning decisions always
have a "why." Be ready to explain: *why drop vs. fill?* The rule of
thumb used here — if the missing field is required to calculate the
core number (Quantity → Revenue), drop it; if it's just a descriptive
field (Region), fill it so you don't lose real data.

### 2. Analysis methods
- `monthly_revenue_trend()` — groups by month, sums revenue.
- `top_products(n)` — groups by product, sums revenue, sorts
  descending, takes top N.
- `category_distribution()` — revenue share per category.
- `region_performance()` — revenue per region.
- `average_order_value()` — mean revenue per row.

All of these use the same core Pandas pattern: **groupby → aggregate
→ sort**. If you understand this one pattern deeply, you can explain
every method in the class.

### 3. Why a class (OOP) instead of just functions?
The `SalesAnalyzer` class bundles the data (`self.df`) with the
methods that operate on it. This means:
- You load the CSV once, clean it once, and then call as many
  analysis methods as you want without re-passing the data around.
- It's a simple, honest use of OOP — a class holding state
  (`self.df`) plus methods (behavior) — exactly the kind of example
  you'd want to explain if asked "do you know OOP?"

### 4. Visualizations
- Line chart for the monthly trend (shows the Oct–Nov festive-season
  spike clearly).
- Horizontal bar chart for top products.
- Pie chart for category share.

## Key insights you can talk about
- Revenue spikes sharply in **October and November** (festive season
  effect built into the data) — a good example of *seasonal pattern*
  detection.
- **Perfume, T-Shirt, and Non-stick Pan** are the top revenue-driving
  products.
- Revenue is fairly evenly spread across categories and regions, with
  **Home & Kitchen** slightly ahead.
- Average order value is a useful single-number summary of overall
  order size — good for tracking over time.

## Possible follow-up questions to prepare for
- "Why did you use `groupby` here instead of a loop?" → It's vectorized
  and much faster than manually looping through rows in Python.
- "How would you handle a much larger dataset?" → Mention chunked
  reading (`pd.read_csv(..., chunksize=...)`) or using a database
  instead of loading everything into memory.
- "What would you add next?" → Ideas: correlation between price and
  quantity sold, customer segmentation, day-of-week analysis.
