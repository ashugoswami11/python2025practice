import pandas as pd

df = pd.read_csv("sales_data.csv", sep=",")


# print(df.head())                               Shows first 5 rows
# print("rows and columns are: ", df.shape)      I checked the size of the dataset to understand how much data I’m working with
# print(df.info())                               I used df.info() to check data types and missing values.
# print(df.isnull().sum())                       df.isnull() identifies empty values and .sum() counts how many missing values are present in each column.


#now converting Order_Date into proper date format
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors = "coerce", dayfirst = True)


#now i am removing rows where Order_Date is missing
df = df.dropna(subset=["Order_Date"])


#now filling missing quantitites with average
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())


#now cleaning sales column
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())


#removing duplicate rows 
df = df.drop_duplicates()

#now checking duplicate rows
#print("Duplicate rows: ", df.duplicated().sum())


#creating month column 
df["Month"] = df["Order_Date"].dt.month_name()


#monthly sales
df["Sales"] = df["Sales"].round(0)
df["Month_No"] = df["Order_Date"].dt.month
monthly_sales = df.groupby(["Month_No", "Month"])["Sales"].sum().sort_index()
print(monthly_sales)

#top Products
df["Product"] = df["Product"].str.strip()
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending = False)
print(top_products)


#Region-wise Performance
df["Region"] = df["Region"].str.title()
region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales)


df = df.drop(columns=["Month_No"]) #dropping the month no. because it has no use in the final cleaned sales data
df.to_csv("cleaned_sales_data.csv", index = False)


