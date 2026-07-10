# -------------------------------------------------------------
# Topic: Pandas Sorting and Grouping Operations
# Author: Nurnabi
# Goal: Learning how to sort values and group data by categories
# -------------------------------------------------------------

import pandas as pd

print("--- Step 1: Creating the DataFrame ---")
# 1. Creating a demo dataset with 5 products
data = {
    "Product": ["Laptop", "Mouse", "Chips", "Keyboard", "Chocolate"],
    "Category": ["Electronics", "Electronics", "Food", "Electronics", "Food"],
    "Price":,
    "Quantity": [5, 20, 50, 15, 40]
}
df = pd.DataFrame(data)
print("Original Data Table:")
print(df)
print("\n" + "="*50 + "\n")


print("--- Step 2: Sorting Data (High to Low Price) ---")
# 2. Sorting the data by 'Price' column in descending order
sorted_df = df.sort_values(by="Price", ascending=False)
print("Sorted Table by Price:")
print(sorted_df)
print("\n" + "="*50 + "\n")


print("--- Step 3: Grouping Data by Category ---")
# 3. Grouping data by 'Category' and calculating total sum of 'Quantity'
grouped_df = df.groupby("Category")["Quantity"].sum()
print("Total Product Quantity by Category:")
print(grouped_df)
