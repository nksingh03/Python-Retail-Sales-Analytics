# Python Retail Sales Analytics

## Project Overview

This project analyzes retail sales data using Python. It uses **Pandas, NumPy, and Matplotlib** to clean the dataset, calculate sales insights, and create visualizations that help understand sales performance.

The project includes a synthetic retail sales dataset generated using Python.

## Tools and Technologies

- Python
- Pandas – data cleaning and analysis
- NumPy – data generation and numerical operations
- Matplotlib – data visualization

## Project Structure

```text
Python-Retail-Sales-Analytics/
│
├── analysis.py
├── generate_data.py
├── retail_sales.csv
├── README.md
│
└── output/
    ├── monthly_trend.png
    ├── top_products.png
    └── category_distribution.png
```

*The `output/` folder and chart images are created when you run the analysis.*

## Dataset

The dataset contains retail transaction information, including:

- Order ID
- Order Date
- Product Category
- Product
- Region
- Quantity
- Unit Price
- Revenue

The dataset is generated using the `generate_data.py` script and includes data-quality issues for cleaning practice, such as missing values, duplicate records, and invalid quantities.

## Data Cleaning

The analysis script performs the following cleaning steps:

1. Removes duplicate records.
2. Removes rows with missing quantities.
3. Removes records with zero or negative quantities.
4. Fills missing region values with `"Unknown"`.
5. Recalculates revenue using quantity multiplied by unit price.
6. Extracts the month from the order date for monthly analysis.

## Analysis Performed

The project analyzes:

- Monthly revenue trends
- Top-selling products by revenue
- Revenue by product category
- Revenue by region
- Average revenue per transaction

## Visualizations

The script generates the following charts in the `output/` folder:

- `monthly_trend.png` – monthly revenue trend
- `top_products.png` – top products by revenue
- `category_distribution.png` – revenue distribution by category

## How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Python-Retail-Sales-Analytics
```

### 3. Install the required libraries

```bash
pip install pandas numpy matplotlib
```

### 4. Run the analysis

Make sure `retail_sales.csv` is in the project folder, then run:

```bash
python analysis.py
```

The cleaned data analysis and visualization charts will be generated.

### Optional: Generate a new dataset

To create a fresh synthetic dataset, run:

```bash
python generate_data.py
```

Make sure the generated CSV is saved as `retail_sales.csv` in the project folder before running `analysis.py`.

## Key Learning Outcomes

- Data cleaning using Pandas
- Handling missing and duplicate values
- Working with dates and numerical data
- Performing exploratory data analysis
- Creating charts using Matplotlib
- Organizing a Python data analytics project

## Author

Nikhil Kumar Singh

