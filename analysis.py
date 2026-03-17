import pandas as pd

data = pd.read_csv("sales.csv")

# create revenue column
data["revenue"] = data["price"] * data["quantity"]

# total revenue
total_revenue = data["revenue"].sum()

# revenue per product
revenue_per_product = data.groupby("product")["revenue"].sum()

# top selling product
top_product = revenue_per_product.idxmax()

# print results
print("Total Revenue:", total_revenue)
print("\nRevenue per product:")
print(revenue_per_product)
print("\nTop Selling Product:", top_product)

# save results to file
with open("report.txt", "w") as file:
    file.write(f"Total Revenue: {total_revenue}\n\n")
    file.write("Revenue per product:\n")
    file.write(str(revenue_per_product))
    file.write(f"\n\nTop Selling Product: {top_product}")