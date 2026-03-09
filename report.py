import pandas as pd
import wbgapi as wb
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor

3# 1. Get actual country codes (excluding regions/aggregates)
country_codes = [eco['id'] for eco in wb.economy.list() if not eco.get('aggregate')]

# 2. Define the updated indicators, now including Agricultural Share
indicators = {
    'SI.POV.GINI': 'Gini_Index',
    'NY.GDP.PCAP.PP.CD': 'GDP_Per_Capita_PPP',
    'NE.TRD.GNFS.ZS': 'Trade_Openness',
    'SE.XPD.TOTL.GD.ZS': 'Edu_Expenditure',
    'SL.UEM.TOTL.ZS': 'Unemployment_Rate',
    'NV.AGR.TOTL.ZS': 'Agri_Share_GDP',
    'NV.IND.MANF.ZS': 'Manuf_Share_GDP',
    'NV.SRV.TOTL.ZS': 'Services_Share_GDP'
}

data_dict = {}

print("Fetching and averaging data over the last 10 years...")

# 3. Fetch and average each indicator separately
for code, name in indicators.items():
    # mrv=10 pulls the 10 most recent years for each country
    df_temp = wb.data.DataFrame(code, economy=country_codes, mrv=10)

    # Calculate the mean across those 10 years
    data_dict[name] = df_temp.mean(axis=1)

# 4. Combine all the averaged series into one clean DataFrame
df = pd.DataFrame(data_dict)

# 5. Drop countries that are missing data for ANY of these 6 variables
df_clean = df.dropna()

print(f"Total countries with complete data: {len(df_clean)}")
display(df_clean.head())

# Save to a new CSV so you don't overwrite your old one
df_clean.to_csv('Group1_Inequality_Data_With_Agri.csv')

# 1. Apply the winning transformations
# Y (Gini Index) stays as a level variable
Y_final = df_clean['Gini_Index']

# X variables: GDP and Trade become logged, the rest stay as level variables
X_final = pd.DataFrame()
X_final['Log_GDP'] = np.log(df_clean['GDP_Per_Capita_PPP'])
X_final['Log_Trade'] = np.log(df_clean['Trade_Openness'])
X_final['Edu_Expenditure'] = df_clean['Edu_Expenditure']
X_final['Unemployment_Rate'] = df_clean['Unemployment_Rate']
X_final['Agri_Share_GDP'] = df_clean['Agri_Share_GDP']
X_final['Manuf_Share_GDP'] = df_clean['Manuf_Share_GDP']
# (Services sector is left out as our reference category)

# 2. Add the constant
X_final = sm.add_constant(X_final)

# 3. Fit the final optimized OLS model
model_final = sm.OLS(Y_final, X_final)
results_final = model_final.fit()

# 4. Print the final summary
print("=== FINAL OPTIMIZED OLS REGRESSION ===")
print(results_final.summary())

# 5. Run a final VIF check to ensure the logs didn't introduce multicollinearity
print("\n=== FINAL VIF SCORES ===")
vif_data = pd.DataFrame()
vif_data["Variable"] = X_final.columns
vif_data["VIF"] = [variance_inflation_factor(X_final.values, i) for i in range(X_final.shape[1])]
print(vif_data.round(2))
