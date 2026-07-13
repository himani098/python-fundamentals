import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/ecommerce_sales.csv")
print(df)

#display 
#head()
print(df.head(2))
#tail()
print(df.tail(2))
#shape
print(df.shape)
#describe()
print(df.describe())
#info()
print(df.info())

#create a new column
df["Total Amount"] = df["Quantity"] * df["Price"]
print(df)

#Numpy
total_revenue = df["Total Amount"].sum()
print("Total Revenue: ", total_revenue)
average_revenue = df["Total Amount"].mean()
print("Average Revenue: ", average_revenue)
highest_revenue = df["Total Amount"].max()
print("Highest Revenue: ", highest_revenue)
lowest_revenue = df["Total Amount"].min()
print("Lowest Revenue: ", lowest_revenue)

revenue = np.array(df["Total Amount"])

print("Total Revenue :", np.sum(revenue))
print("Average Revenue :", np.mean(revenue))
print("Highest Revenue :", np.max(revenue))
print("Lowest Revenue :", np.min(revenue))

#Pandas Analysis
highest_selling = df.loc[df["Quantity"].idxmax(), "Product"]
print("Highest Selling Product:", highest_selling)
highest_revenue = df.loc[df["Total Amount"].idxmax(), "Product"]
print("Highest Revenue Product:", highest_revenue)
average_price = df["Price"].mean()
print("Average Price:", average_price)
total_quantity = df["Quantity"].sum()
print("Total Quantity Sold:", total_quantity)
number_of_orders = df["Order_ID"].count()
print("Number of Orders:", number_of_orders)
# or
print("Number of Orders:", len(df))
total_revenue = df["Total Amount"].sum()
print("Total Revenue:", total_revenue)

#GroupBy
# Category-wise Total Revenue
print(df.groupby("Category")["Total Amount"].sum())
# Category-wise Average Revenue
print(df.groupby("Category")["Total Amount"].mean())
# Category-wise Total Quantity Sold
print(df.groupby("Category")["Quantity"].sum())

#or 
#All three together
print(
    df.groupby("Category").agg({
        "Total Amount": ["sum", "mean"],
        "Quantity": "sum"
    })
)


# Sorting
# Highest Revenue
print(df.sort_values(by="Total Amount", ascending=False))
# Lowest Revenue
print(df.sort_values(by="Total Amount"))

#Filtering
# Products with Price > 5000
print(df[df["Price"] > 5000])
# Electronics only
print(df[df["Category"] == "Electronics"])
# Quantity > 2
print(df[df["Quantity"] > 2])

#Handle Missing Values
# Introduce a Missing Value
df.loc[3, "Price"] = np.nan
# Check Missing Values
print(df.isnull().sum())
# Fill Missing Value
df["Price"] = df["Price"].fillna(df["Price"].mean())
print(df)
#or
df["Price"] = df["Price"].fillna(0)
print(df)
# Drop Missing Values
df.dropna(inplace=True)
print(df)
# or only check the Price column:
df.dropna(subset=["Price"], inplace=True)
print(df)


#Bar Chart
# Category vs Total Revenue
category_revenue = df.groupby("Category")["Total Amount"].sum()

plt.figure(figsize=(6,4))
plt.bar(category_revenue.index, category_revenue.values)
plt.title("Category vs Total Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.savefig("images/bar_chart.png")
plt.show()


# Pie Chart
# Revenue Share by Category
plt.figure(figsize=(6,6))

plt.pie(
    category_revenue.values,
    labels=category_revenue.index,
    autopct="%1.1f%%"
)

plt.title("Revenue Share")
plt.savefig("images/pie_chart.png")
plt.show()

# Line Chart
# Order ID vs Total Revenue
plt.figure(figsize=(6,4))

plt.plot(
    df["Order_ID"],
    df["Total Amount"],
    marker="o"
)

plt.xlabel("Order ID")
plt.ylabel("Revenue")

plt.title("Order Revenue")

plt.savefig("images/line_chart.png")

plt.show()


# Histogram
# Distribution of Prices
plt.figure(figsize=(6,4))

plt.hist(df["Price"], bins=5)

plt.title("Price Distribution")

plt.xlabel("Price")
plt.ylabel("Frequency")

plt.savefig("images/histogram.png")

plt.show()


# Scatter Plot
# Price vs Quantity
plt.figure(figsize=(6,4))

plt.scatter(
    df["Price"],
    df["Quantity"]
)

plt.xlabel("Price")
plt.ylabel("Quantity")

plt.title("Price vs Quantity")

plt.savefig("images/scatter.png")

plt.show()


# Multiple Line Chart
plt.figure(figsize=(7,4))

plt.plot(df["Order_ID"],df["Price"],marker="o",label="Price")

plt.plot(df["Order_ID"],df["Total Amount"],marker="s",label="Revenue")

plt.legend()

plt.xlabel("Order ID")

plt.title("Price vs Revenue")

plt.savefig("images/multiple_line.png")

plt.show()


# Subplots
fig, ax = plt.subplots(2,2,figsize=(10,8))
# Top Left
ax[0,0].bar(category_revenue.index,category_revenue.values)
ax[0,0].set_title("Bar Chart")
# Top Right
ax[0,1].pie(
    category_revenue.values,
    labels=category_revenue.index,
    autopct="%1.1f%%"
)
ax[0,1].set_title("Pie Chart")
# Bottom Left
ax[1,0].hist(df["Price"],bins=5)
ax[1,0].set_title("Histogram")
# Bottom Right
ax[1,1].scatter(df["Price"],df["Quantity"])
ax[1,1].set_title("Scatter Plot")
# Finally,

plt.tight_layout()

plt.savefig("images/dashboard.png")

plt.show()