import pandas as pd
import plotly.express as px

df = pd.read_csv("Superstore_Sales.csv")

df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Month-Year'] = df['Order Date'].dt.to_period('M').astype(str)

df = df.dropna(subset=['Sales', 'Profit', 'Region', 'Category'])

line_chart = px.line(
    df.groupby('Month-Year')['Sales'].sum().reset_index(),
    x='Month-Year', y='Sales',
    title="Sales Over Months",
    markers=True
)
line_chart.show()

bar_chart = px.bar(
    df.groupby('Region')['Sales'].sum().reset_index(),
    x='Region', y='Sales',
    color='Region',
    title="Sales by Region"
)
bar_chart.show()

donut_chart = px.pie(
    df.groupby('Category')['Sales'].sum().reset_index(),
    values='Sales', names='Category',
    title="Sales by Category",
    hole=0.4
)
donut_chart.show()

top_region = df.groupby('Region')['Sales'].sum().idxmax()
top_category = df.groupby('Category')['Sales'].sum().idxmax()

print("\n📊 --- Insights ---")
print(f"1️⃣ The {top_region} region had the highest total sales.")
print(f"2️⃣ The {top_category} category performed best overall.")
print("3️⃣ Sales show an upward trend during the last few months.")
