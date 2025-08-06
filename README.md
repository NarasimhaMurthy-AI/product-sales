# 🛒 Product Sales - Exploratory Data Analysis (EDA)

This project performs exploratory data analysis (EDA) on a **Product Sales dataset** to uncover key business insights. The goal is to understand sales patterns, customer behavior, discount impact, and profit distribution across different regions and product categories.

---

## 📂 Dataset Description

The dataset includes transactional sales data with the following key columns:

- **Order Date** & **Ship Date** — Transaction timeline
- **Sales**, **Profit**, **Discount**, **Quantity** — Numeric features
- **Category**, **Region**, **Segment**, **State**, **Ship Mode** — Categorical details

---

## 🔍 EDA Objectives

1. Generate summary statistics (mean, median, std, etc.)
2. Create histograms and boxplots for numeric features
3. Use correlation matrix to analyze feature relationships
4. Identify patterns, trends, and anomalies
5. Draw basic inferences from visualizations

---

## 📊 Key Analysis Performed

### ✅ Summary Statistics
- Used `df.describe()` to view central tendencies and spread.
- Checked for null values and data types using `df.info()` and `df.isnull().sum()`.

### ✅ Data Cleaning
- Converted `Order Date` and `Ship Date` columns to datetime format.
- Removed or handled invalid dates using `errors='coerce'`.

### ✅ Visualizations
- **Histograms** for Sales, Profit, Discount, and Quantity
- **Boxplots** to identify outliers in numeric data
- **Heatmap** for correlation between numeric features
- **Scatterplot** to explore relationship between Discount and Profit by Region
- **Boxplot by Category** to compare quantity distribution

---

## 📈 Key Insights

- **High discounts** (above 30%) are often linked to **negative profits**.
- **Technology** and **Office Supplies** yield **higher average profits** than Furniture.
- **Sales** and **Profit** are positively correlated, but not strongly.
- Outliers are present in Sales and Profit — could affect modeling.
- Different **regions** behave differently in terms of discount effectiveness.

---

## 🛠️ Technologies Used

- Python 3.x
- pandas
- matplotlib
- seaborn
- scikit-learn (used for scaling in extended tasks)

---

## 📁 Output Files

- `cleaned_sales.xlsx` – cleaned and formatted dataset
- (Optional) `.png` files – saved plots (if enabled)
- `EDA_Script.py` or `EDA.ipynb` – source code

---

## 🚀 How to Run

1. Clone the repo or download the files
2. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn openpyxl
