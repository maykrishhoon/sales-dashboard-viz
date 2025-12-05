import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Laptops': [12000, 15000, 13000, 14000, 16000, 19000, 18000, 20000, 21000, 25000, 30000, 35000],
    'Phones':  [8000, 9000, 8500, 9500, 10000, 11000, 12000, 13000, 14000, 18000, 22000, 28000],
    'Accessories': [3000, 3200, 3100, 3500, 3800, 4000, 4200, 4500, 4800, 6000, 7500, 9000],
    'Profit_Margin': [15, 14, 16, 15, 17, 18, 19, 18, 20, 22, 25, 24] 
}

df = pd.DataFrame(data)


df['Total_Sales'] = df['Laptops'] + df['Phones'] + df['Accessories']

print("--- Data Loaded ---")
print(df.head())


sns.set_theme(style="whitegrid") 


fig = plt.figure(figsize=(14, 9))
gs = fig.add_gridspec(2, 2) 


ax1 = fig.add_subplot(gs[0, :]) 

sns.lineplot(data=df, x='Month', y='Laptops', marker='o', label='Laptops', ax=ax1)
sns.lineplot(data=df, x='Month', y='Phones', marker='o', label='Phones', ax=ax1)
sns.lineplot(data=df, x='Month', y='Accessories', marker='o', label='Accessories', ax=ax1)

ax1.set_title('Sales Trend (2024)', fontsize=15, fontweight='bold')
ax1.set_ylabel('Revenue ($)')


ax2 = fig.add_subplot(gs[1, 0])


totals = {
    'Laptops': df['Laptops'].sum(),
    'Phones': df['Phones'].sum(),
    'Accessories': df['Accessories'].sum()
}

colors = ['#4c72b0', '#dd8452', '#55a868'] 
ax2.bar(totals.keys(), totals.values(), color=colors)

ax2.set_title('Total Revenue by Category', fontsize=12)
ax2.set_ylabel('Total Sales ($)')


ax3 = fig.add_subplot(gs[1, 1]) 

sns.scatterplot(
    data=df, 
    x='Total_Sales', 
    y='Profit_Margin', 
    size='Profit_Margin', 
    hue='Month', 
    sizes=(100, 500), 
    legend=False, 
    ax=ax3
)

ax3.set_title('Correlation: Sales vs Profit Margin', fontsize=12)
ax3.set_xlabel('Sales Volume')
ax3.set_ylabel('Margin (%)')


best_month = df.loc[df['Total_Sales'].idxmax()]
ax3.text(best_month['Total_Sales'], best_month['Profit_Margin'], ' Dec (Best)', fontweight='bold')


plt.tight_layout()
print("✨ Dashboard generated! Check the popup window.")
plt.show()