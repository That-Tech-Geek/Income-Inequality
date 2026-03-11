import pandas as pd
import wbgapi as wb
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan

# ---------------------------------------------------------
# 1. DATA FETCHING AND CLEANING
# ---------------------------------------------------------

# Get actual country codes (excluding regions/aggregates)
country_codes = [eco['id'] for eco in wb.economy.list() if not eco.get('aggregate')]

# Define the updated indicators, now including Agricultural Share
indicators = {
    'SI.POV.GINI': 'Gini_Index',
    'NY.GDP.PCAP.PP.CD': 'GDP_Per_Capita_PPP',
    'NE.TRD.GNFS.ZS': 'Trade_Openness',
    'SE.XPD.TOTL.GD.ZS': 'Edu_Expenditure',
    'SL.UEM.TOTL.ZS': 'Unemployment_Rate',
    'NV.AGR.TOTL.ZS': 'Agri_Share_GDP',
    'NV.IND.MANF.ZS': 'Manuf_Share_GDP',
    'NV.SRV.TOTL.ZS': 'Services_Share_GDP',
    'SL.TLF.CACT.FE.ZS': 'Female_Labor_Part'
}

data_dict = {}

print("Fetching and averaging data over the last 10 years...")

# Fetch and average each indicator separately
for code, name in indicators.items():
    # mrv=10 pulls the 10 most recent years for each country
    df_temp = wb.data.DataFrame(code, economy=country_codes, mrv=10)
    # Calculate the mean across those 10 years
    data_dict[name] = df_temp.mean(axis=1)

# Combine all the averaged series into one clean DataFrame
df = pd.DataFrame(data_dict)

# Drop countries that are missing data for ANY of these variables
df_clean = df.dropna()

print(f"Total countries with complete data: {len(df_clean)}\n")
# Temporarily display all rows without truncating
pd.set_option('display.max_rows', None)
display(df_clean)
pd.reset_option('display.max_rows')

# Save to a new CSV so you don't overwrite your old one
df_clean.to_csv('Group1_Inequality_Data_With_Agri.csv')

# ---------------------------------------------------------
# 2. MODEL PREPARATION AND INITIAL OLS
# ---------------------------------------------------------

# Apply the transformations
# Y (Gini Index) stays as a level variable
Y_final = df_clean['Gini_Index']

# X variables: ONLY GDP is logged now, the rest stay as level variables
X_final = pd.DataFrame()
X_final['Log_GDP'] = np.log(df_clean['GDP_Per_Capita_PPP'])
X_final['Trade_Openness'] = df_clean['Trade_Openness'] # Removed np.log() here
X_final['Edu_Expenditure'] = df_clean['Edu_Expenditure']
X_final['Unemployment_Rate'] = df_clean['Unemployment_Rate']
X_final['Agri_Share_GDP'] = df_clean['Agri_Share_GDP']
X_final['Manuf_Share_GDP'] = df_clean['Manuf_Share_GDP']
X_final['Female_Labor_Part'] = df_clean['Female_Labor_Part']
# (Services sector is left out as our reference category to avoid multicollinearity)

# Add the constant
X_final = sm.add_constant(X_final)

# Fit the initial OLS model
model_final = sm.OLS(Y_final, X_final)
results_final = model_final.fit()

print("=== INITIAL OLS REGRESSION ===")
print(results_final.summary())

# Run a VIF check to ensure no multicollinearity
print("\n=== FINAL VIF SCORES ===")
vif_data = pd.DataFrame()
vif_data["Variable"] = X_final.columns
vif_data["VIF"] = [variance_inflation_factor(X_final.values, i) for i in range(X_final.shape[1])]
print(vif_data.round(2))

# ---------------------------------------------------------
# 3. HETEROSCEDASTICITY DIAGNOSTICS & CORRECTION
# ---------------------------------------------------------

print("\n=== HETEROSCEDASTICITY DIAGNOSTICS ===")

# Formal Test: Breusch-Pagan Test
# Tests the null hypothesis that the variance of the errors is constant (homoscedasticity)
bp_test_stats = het_breuschpagan(results_final.resid, X_final.values)
bp_labels = ['Lagrange Multiplier Statistic', 'p-value', 'F-Statistic', 'F p-value']
bp_results = dict(zip(bp_labels, bp_test_stats))

print("Breusch-Pagan Test Results:")
for key, value in bp_results.items():
    print(f"  {key}: {value:.4f}")

if bp_results['p-value'] < 0.05:
    print("  Conclusion: Reject null hypothesis. Heteroscedasticity is present.")
else:
    print("  Conclusion: Fail to reject null hypothesis. (Though if borderline, robust errors are still recommended).")

# Visual Diagnostic: Residual Plot
plt.figure(figsize=(9, 6))
sns.residplot(x=results_final.fittedvalues, y=results_final.resid,
              lowess=True, scatter_kws={'alpha': 0.6}, line_kws={'color': 'red', 'lw': 2})
plt.title('Residuals vs. Fitted Values (Checking for Heteroscedasticity)', fontsize=14)
plt.xlabel('Fitted Values (Predicted Gini Index)', fontsize=12)
plt.ylabel('Residuals', fontsize=12)
plt.axhline(y=0, color='black', linestyle='--')
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

# Model Correction: Re-fit with Heteroscedasticity-Robust Standard Errors (HC3)
print("\n=== FINAL OLS REGRESSION (WITH HC3 ROBUST STANDARD ERRORS) ===")
robust_results = results_final.get_robustcov_results(cov_type='HC3')
print(robust_results.summary())
