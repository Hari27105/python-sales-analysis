import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create sample sales data
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 
                'Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones',
                'Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories',
                 'Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories',
                 'Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories'],
    'Sales': [45000, 500, 1500, 12000, 2000,
              48000, 450, 1600, 13000, 2200,
              47000, 520, 1550, 12500, 2100],
    'Quantity': [15, 50, 30, 20, 40,
                 16, 45, 32, 22, 42,
                 15, 48, 31, 21, 41],
    'Month': ['January', 'January', 'January', 'January', 'January',
              'February', 'February', 'February', 'February', 'February',
              'March', 'March', 'March', 'March', 'March']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('sales_data.csv', index=False)
print("✓ Sample sales data CSV created successfully!\n")

# Load the data
df = pd.read_csv('sales_data.csv')

# Display basic information
print("=" * 50)
print("SALES DATA ANALYSIS PROJECT")
print("=" * 50)
print("\n1. First 5 Rows of Data:")
print(df.head())

print("\n2. Dataset Information:")
print(df.info())

print("\n3. Basic Statistics:")
print(df.describe())

# Data Analysis
print("\n4. Total Sales by Product:")
product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print(product_sales)

print("\n5. Average Sales by Category:")
category_avg = df.groupby('Category')['Sales'].mean()
print(category_avg)

print("\n6. Monthly Total Sales:")
monthly_sales = df.groupby('Month')['Sales'].sum()
print(monthly_sales)

print("\n7. Top Selling Product:")
top_product = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(1)
print(top_product)

# Data Visualization
print("\n8. Creating visualizations...")

# Set style
plt.style.use('seaborn-v0_8-darkgrid')

# Create figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Sales Data Analysis Dashboard', fontsize=16, fontweight='bold')

# Plot 1: Sales by Product
product_sales.plot(kind='bar', ax=axes[0, 0], color='steelblue')
axes[0, 0].set_title('Total Sales by Product')
axes[0, 0].set_xlabel('Product')
axes[0, 0].set_ylabel('Sales (₹)')
axes[0, 0].tick_params(axis='x', rotation=45)

# Plot 2: Category-wise Sales (Pie Chart)
category_sales = df.groupby('Category')['Sales'].sum()
axes[0, 1].pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=90)
axes[0, 1].set_title('Sales Distribution by Category')

# Plot 3: Monthly Sales Trend
monthly_sales.plot(kind='line', ax=axes[1, 0], marker='o', color='green', linewidth=2)
axes[1, 0].set_title('Monthly Sales Trend')
axes[1, 0].set_xlabel('Month')
axes[1, 0].set_ylabel('Sales (₹)')
axes[1, 0].grid(True)

# Plot 4: Quantity Sold by Product
quantity_by_product = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
quantity_by_product.plot(kind='barh', ax=axes[1, 1], color='coral')
axes[1, 1].set_title('Total Quantity Sold by Product')
axes[1, 1].set_xlabel('Quantity')
axes[1, 1].set_ylabel('Product')

plt.tight_layout()
plt.savefig('sales_analysis_dashboard.png', dpi=300, bbox_inches='tight')
print("✓ Dashboard saved as 'sales_analysis_dashboard.png'")

plt.show()

print("\n" + "=" * 50)
print("Analysis Complete!")
print("=" * 50)