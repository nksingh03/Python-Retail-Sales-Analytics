"""
generate_data.py
----------------
Creates a realistic synthetic retail sales dataset and saves it as CSV.
This mimics the kind of raw data you'd download from Kaggle (with a
few intentional messy bits - missing values, duplicates - so the
cleaning step in analysis.py has real work to do).
"""

import numpy as np
import pandas as pd

np.random.seed(42)

# ---- Basic building blocks ----
categories = {
    "Electronics": ["Headphones", "Bluetooth Speaker", "Smartwatch", "Power Bank", "USB Cable"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket", "Sneakers", "Cap"],
    "Home & Kitchen": ["Mixer Grinder", "Non-stick Pan", "LED Lamp", "Water Bottle", "Storage Box"],
    "Beauty": ["Face Wash", "Shampoo", "Lipstick", "Moisturizer", "Perfume"],
    "Sports": ["Yoga Mat", "Dumbbells", "Football", "Cricket Bat", "Water Bottle Sipper"],
}

regions = ["North", "South", "East", "West"]

n_rows = 2000
start_date = pd.Timestamp("2024-01-01")
end_date = pd.Timestamp("2024-12-31")

rows = []
order_id = 1000

for _ in range(n_rows):
    category = np.random.choice(list(categories.keys()))
    product = np.random.choice(categories[category])
    region = np.random.choice(regions)

    # random date across the year, with a mild festive-season boost in Oct-Nov
    if np.random.rand() < 0.25:
        month = np.random.choice([10, 11])
    else:
        month = np.random.randint(1, 13)
    day = np.random.randint(1, 28)
    order_date = pd.Timestamp(year=2024, month=month, day=day)

    quantity = np.random.randint(1, 6)
    unit_price = round(np.random.uniform(150, 3500), 2)
    revenue = round(quantity * unit_price, 2)

    rows.append({
        "OrderID": order_id,
        "OrderDate": order_date,
        "Category": category,
        "Product": product,
        "Region": region,
        "Quantity": quantity,
        "UnitPrice": unit_price,
        "Revenue": revenue,
    })
    order_id += 1

df = pd.DataFrame(rows)

# ---- Introduce realistic messiness ----
# 1. Some missing Quantity values
missing_idx = np.random.choice(df.index, size=30, replace=False)
df.loc[missing_idx, "Quantity"] = np.nan

# 2. Some missing Region values
missing_idx2 = np.random.choice(df.index, size=20, replace=False)
df.loc[missing_idx2, "Region"] = np.nan

# 3. Some duplicate rows
dupes = df.sample(15, random_state=1)
df = pd.concat([df, dupes], ignore_index=True)

# 4. A few negative/incorrect Quantity values (data entry errors)
err_idx = np.random.choice(df.index, size=5, replace=False)
df.loc[err_idx, "Quantity"] = -1

# Shuffle rows so it looks like raw export, not generated in order
df = df.sample(frac=1, random_state=7).reset_index(drop=True)

df.to_csv("data/retail_sales.csv", index=False)
print(f"Generated {len(df)} rows -> data/retail_sales.csv")
