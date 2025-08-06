import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("Product_Sales.csv", encoding='latin1')


#  Info and Nulls
# --------------------------
print("🔹 First 5 Rows:\n", df.head())
print("\n🔹 Shape of Data:", df.shape)
print("\n🔹 Null Value Summary:\n", df.isnull().sum())
print("\n🔹 Data Types:\n", df.dtypes)
print("\n🔹 Summary Statistics:\n", df.describe(include='all'))


# Convert Dates (Fix Dates)
 
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

 
#   Correlation Heatmap
 
numeric_cols = ['Sales', 'Quantity', 'Discount', 'Profit']
plt.figure(figsize=(8, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap - Numeric Columns")
plt.tight_layout()
plt.show()

 
#   Distribution Plots
 
for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

 
#   Boxplot by Category
 
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='Category', y='Profit')
plt.title('Profit Distribution per Category')
plt.tight_layout()
plt.show()

 
# 6. Scatterplot: Discount vs Profit
 
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Discount', y='Profit', hue='Region')
plt.title('Discount vs Profit by Region')
plt.tight_layout()
plt.show()
print(df.shape)
# ...existing code...



# Save cleaned DataFrame to Excel
df.to_excel("cleaned_sales.xlsx", index=False)
plt.savefig("filename.png")



print("File saved as cleaned_sales.xlsx")

