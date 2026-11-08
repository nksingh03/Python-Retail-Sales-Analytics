
import pandas as pd
import os
import matplotlib.pyplot as plt


class SalesAnalyzer:
   
    def __init__(self, csv_path: str):
        self.raw_path = csv_path
        self.df = pd.read_csv(csv_path, parse_dates=["OrderDate"])
        self.cleaned = False
        os.makedirs("output", exist_ok=True)

    # ------------------------------------------------------------------
    # 1. DATA CLEANING
    # ------------------------------------------------------------------
    def clean_data(self):
       
        before = len(self.df)

        self.df = self.df.drop_duplicates()

        self.df = self.df.dropna(subset=["Quantity"])

        self.df = self.df[self.df["Quantity"] > 0]

        self.df["Region"] = self.df["Region"].fillna("Unknown")

        self.df["Revenue"] = self.df["Quantity"] * self.df["UnitPrice"]

        self.df["Month"] = self.df["OrderDate"].dt.to_period("M").astype(str)

        after = len(self.df)
        self.cleaned = True
        print(f"[clean_data] Rows before cleaning: {before} | after cleaning: {after} "
              f"({before - after} rows removed)")
        return self.df

    def _check_cleaned(self):
        if not self.cleaned:
            raise RuntimeError("Call clean_data() before running analysis methods.")

    # ------------------------------------------------------------------
    # 2. ANALYSIS METHODS
    # ------------------------------------------------------------------
    def monthly_revenue_trend(self):
       
        self._check_cleaned()
        trend = self.df.groupby("Month")["Revenue"].sum().sort_index()
        return trend

    def top_products(self, n=5):
     
        self._check_cleaned()
        top = (
            self.df.groupby("Product")["Revenue"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )
        return top

    def category_distribution(self):
        
        self._check_cleaned()
        return self.df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

    def region_performance(self):
      
        self._check_cleaned()
        return self.df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

    def average_order_value(self):
       
        self._check_cleaned()
        return self.df["Revenue"].mean()

    # ------------------------------------------------------------------
    # 3. VISUALIZATIONS
    # ------------------------------------------------------------------
    def plot_monthly_trend(self, save_path="output/monthly_trend.png"):
        trend = self.monthly_revenue_trend()
        plt.figure(figsize=(9, 5))
        plt.plot(trend.index, trend.values, marker="o", color="#1F3864")
        plt.title("Monthly Revenue Trend (2024)")
        plt.xlabel("Month")
        plt.ylabel("Revenue")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        print(f"[plot_monthly_trend] Saved -> {save_path}")

    def plot_top_products(self, n=5, save_path="output/top_products.png"):
        top = self.top_products(n)
        plt.figure(figsize=(8, 5))
        plt.barh(top.index[::-1], top.values[::-1], color="#2E75B6")
        plt.title(f"Top {n} Products by Revenue")
        plt.xlabel("Revenue")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        print(f"[plot_top_products] Saved -> {save_path}")

    def plot_category_distribution(self, save_path="output/category_distribution.png"):
        dist = self.category_distribution()
        plt.figure(figsize=(7, 7))
        plt.pie(dist.values, labels=dist.index, autopct="%1.1f%%", startangle=90)
        plt.title("Revenue Share by Category")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        print(f"[plot_category_distribution] Saved -> {save_path}")


# ==========================================================================
# MAIN - runs the full analysis end-to-end
# ==========================================================================
if __name__ == "__main__":
    analyzer = SalesAnalyzer("retail_sales.csv")
    analyzer.clean_data()

    print("\n=== Monthly Revenue Trend ===")
    print(analyzer.monthly_revenue_trend())

    print("\n=== Top 5 Products by Revenue ===")
    print(analyzer.top_products(5))

    print("\n=== Revenue by Category ===")
    print(analyzer.category_distribution())

    print("\n=== Revenue by Region ===")
    print(analyzer.region_performance())

    print(f"\n=== Average Order Value ===\n{analyzer.average_order_value():.2f}")

    # Save charts
    analyzer.plot_monthly_trend()
    analyzer.plot_top_products()
    analyzer.plot_category_distribution()

    print("\nDone. Check the output/ folder for saved charts.")
