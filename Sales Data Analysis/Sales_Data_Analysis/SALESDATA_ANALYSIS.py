import pandas as pd
import matplotlib.pyplot as plt

#loading the dataset
df = pd.read_csv('sales_data.csv')

#preview the dataset
print("Initial Data Preview:")
print(df.head())

#here we convert the date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

#adding new column for total sales
df['Total Sales'] = df['Quantity Sold'] * df['Unit Price']

#handling missing values by filling with the median
df.fillna(df.median(numeric_only=True), inplace=True)

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# 1.Monthly sales
monthly_sales = df.resample('M', on='Date')['Total Sales'].sum()
print("\nMonthly Sales Summary:")
print(monthly_sales)

# 1.1 plotting monthly sales
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', color='blue', title='Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

# 2.Sales by product
sales_by_product = df.groupby('Product')['Total Sales'].sum()
print("\nTotal Sales by Product:")
print(sales_by_product)

# 2.1 Plotting sales by product
plt.figure(figsize=(8, 4))
sales_by_product.plot(kind='bar', color='purple', title='Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# 3. Top 5 regions by sales
top_regions = df.groupby('Region')['Total Sales'].sum().nlargest(5)
print("\nTop 5 Regions by Sales:")
print(top_regions)

# 3.1 Plotting top 5 regions by sales
plt.figure(figsize=(8, 4))
top_regions.plot(kind='barh', color='green', title='Top 5 Regions by Sales')
plt.xlabel('Total Sales')
plt.ylabel('Region')
plt.show()

# 4. Find average sales price
avg_sales_price = df.groupby('Product')['Unit Price'].mean()
print("\nAverage Sales Price by Product:")
print(avg_sales_price)

# 4.1 Plot average sales price
plt.figure(figsize=(8, 4))
avg_sales_price.plot(kind='bar', color='orange', title='Average Sales Price by Product')
plt.xlabel('Product')
plt.ylabel('Average Unit Price')
plt.show()

df.to_csv('processed_sales_data.csv', index=False)
print("\nProcessed data saved to 'processed_sales_data.csv'")
