import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



print("""


The following info is included in the table:


National_Debt_Trillions: Total US federal debt (public + intragovernmental)
Debt_to_GDP_Percent: Debt as percentage of Gross Domestic Product
Median_Rent_Monthly: National median monthly rent for 2-bedroom apartment
Median_Home_Price: US median home sale price
Median_Mortgage_Monthly: Estimated monthly payment (30-year, 20% down, average rate)
Debt_Per_Capita: National debt divided by US population
Rent_Burden_Index: Indexed to 2000 (100 = baseline year)

US Debt currently stands at 38 Trillion Dollars! """)
print("\n")
print("\n")


df = pd.read_csv('/Users/russellredman'
                 '/Documents/Pandas/pythonProject'
                 '/projects_4/debt.csv')


df_debt_index = df.set_index('Year')
print(df_debt_index.to_string())

def rent_analysis(rent):
    if rent <650:
        return "Low Monthly Rent - Very Affordable"
    elif 650 < rent <=900:
        return "Low-Medium Monthly Rent - Still Affordable"
    elif 900 < rent <=1300:
        return "Medium Rent - Slightly Less Affordable "
    elif 1300 < rent <=2000:
        return " High Rent - Less Affordable"
    elif rent >2000:
        return "Extremely High Rent - Extremely Unaffordable"
    else:
        return "No Info Listed"

df_debt_index['Monthly_Rent_analysis'] = (df_debt_index['Median_Rent_Monthly']
                                          .apply(rent_analysis))




def home_price_analysis(home_prices):
    if home_prices <150000:
        return "Extremely Low Home Price"
    elif 150000 < home_prices <=250000:
        return "Low Home Price"
    elif 250000 < home_prices <=350000:
        return "Medium Home Price"
    elif 350000 < home_prices <= 450000:
        return "Medium-High Home Price"
    elif 450000 < home_prices <=600000:
        return "High Home Price"
    elif home_prices >600000:
        return "Extremely High Home Price"
    else:
        return "No Info Listed"

df_debt_index['Home_Price_Analysis'] = (df_debt_index['Median_Home_Price']
                                        .apply(home_price_analysis))
print(df_debt_index.to_string())




# -----------------------------------------------------------------------------

# Set style
sns.set_style("whitegrid")
sns.set_palette("husl")

# CREATE JUST ONE CHART
plt.figure(figsize=(12, 8))

# Your scatter plot with regression line
sns.regplot(data=df_debt_index,
            x='National_Debt_Trillions',
            y='Median_Mortgage_Monthly',
            scatter_kws={'alpha':0.6, 's':80},
            line_kws={'color':'red', 'linewidth':2})

# Title and labels (use plt, not axes!)
plt.title('National Debt vs Monthly Mortgage\nDoes US Debt Affect Housing Costs Over Time?',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('National Debt (Trillions $)', fontsize=12)
plt.ylabel('Monthly Mortgage Payment ($)', fontsize=12)

# Optional: Add correlation value
correlation = df_debt_index['National_Debt_Trillions'].corr(df_debt_index['Median_Mortgage_Monthly'])
plt.text(0.05, 0.95, f'Correlation: {correlation:.3f}',
         transform=plt.gca().transAxes,
         fontsize=12,
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

# Save and show
plt.tight_layout()
plt.savefig('US_Debt_Mortgage_Analysis.png', dpi=300, bbox_inches='tight')
print("✅ Chart saved!")
plt.show()
