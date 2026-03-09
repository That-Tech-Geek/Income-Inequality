# Macroeconomic Determinants of Income Inequality: A Cross-Country Empirical Analysis

**Authors:** Sambit Mishra, Dhruv Tyagi, Ritobrata Purkayastha, Barsha Mishra, Jahnvi Bahl

**Date:** March 9, 2026

---

## Abstract

This paper examines correlates of income inequality across a sample of 125 countries using cross-sectional regression analysis. Drawing on theoretical frameworks from the inequality literature, we investigate the relationship between the Gini coefficient and several economic variables: GDP per capita, trade openness, education expenditure, unemployment rate, agricultural share of GDP, and manufacturing share of GDP. The analysis is informed by established theories such as the Kuznets curve hypothesis and the Stolper-Samuelson theorem. Results indicate negative associations between inequality and GDP per capita, trade openness, and agricultural share, and a positive association with the unemployment rate. Education expenditure and manufacturing share are not statistically significant. These findings represent empirical patterns and should not be interpreted as causal.

---

## 1. Introduction

### 1.1 Background
Income inequality remains a central topic in economic research and policy. Cross-country differences in inequality are well-documented, and the roles of economic structure and globalization continue to be explored. This study contributes by testing several hypothesized correlates of inequality using recent cross-sectional data.

### 1.2 Objectives
1. Examine empirical associations between income inequality and selected macroeconomic variables.
2. Assess consistency with predictions from Kuznets and Stolper-Samuelson frameworks.
3. Present regression results with appropriate interpretive caveats.

---

## 2. Literature Review

### 2.1 The Kuznets Curve Hypothesis
Kuznets (1955) proposed an inverted-U relationship between economic development and inequality: inequality rises during early industrialization and declines at later stages. This motivates the inclusion of GDP per capita (in logs) in our model.

### 2.2 Stolper-Samuelson Theorem
The Stolper-Samuelson theorem suggests that trade liberalization affects income distribution by altering returns to factors of production. The direction of the effect depends on a country's factor endowments, making the expected sign of trade openness ambiguous. We include trade openness (in logs) to capture this.

---

## 3. Data and Methodology

### 3.1 Data Sources
Cross-sectional data for 125 countries are drawn from the World Bank's World Development Indicators.

### 3.2 Variable Description

#### Dependent Variable:
- **Gini_Index**: Gini coefficient (0 = perfect equality, 100 = perfect inequality).

#### Independent Variables:
- **Log_GDP**: Natural log of GDP per capita (constant USD).
- **Log_Trade**: Natural log of trade openness [(exports + imports)/GDP %].
- **Edu_Expenditure**: Public education expenditure (% of GDP).
- **Unemployment_Rate**: Total unemployment (% of labor force).
- **Agri_Share_GDP**: Agriculture value added (% of GDP).
- **Manuf_Share_GDP**: Manufacturing value added (% of GDP).

### 3.3 Theoretical Expectations

| Variable             | Suggested Pattern | Basis in Literature |
|----------------------|-------------------|----------------------|
| Log_GDP              | Negative at higher income | Kuznets (1955) |
| Log_Trade            | Ambiguous | Stolper-Samuelson; Bourguignon (2017) |
| Edu_Expenditure      | Potentially negative | Frieden (2001) |
| Unemployment_Rate    | Potentially positive | Bourguignon (2017) |
| Agri_Share_GDP       | Context-dependent | Kuznets (1955); Bourguignon (2017) |
| Manuf_Share_GDP      | Context-dependent | Kuznets (1955); Bourguignon (2017) |

$$Gini\_Index_i = \beta_0 + \beta_1 \ln(GDPpc_i) + \beta_2 \ln(Trade_i) + \beta_3 EduExp_i + \beta_4 Unemp_i + \beta_5 AgriShare_i + \beta_6 ManufShare_i + \varepsilon_i$$

## 4. Results

### 4.1 Regression Output

| Variable             | Coefficient | Std. Error | t-ratio | P>|t|   | [0.025  | 0.975] |
|----------------------|-------------|------------|---------|---------|---------|--------|
| const                | 101.2399    | 10.937     | 9.257   | 0.000   | 79.582  | 122.898|
| Log-GDP              | -4.6682     | 0.890      | -5.244  | 0.000   | -6.431  | -2.906 |
| Log-Trade            | -4.5148     | 1.165      | -3.875  | 0.000   | -6.822  | -2.208 |
| Edu-Expenditure      | 0.2553      | 0.383      | 0.667   | 0.506   | -0.502  | 1.013  |
| Unemployment Rate    | 0.3269      | 0.111      | 2.933   | 0.004   | 0.106   | 0.548  |
| Agri_Share_GDP       | -0.4539     | 0.118      | -3.831  | 0.000   | -0.688  | -0.219 |
| Manuf_Share_GDP      | 0.0643      | 0.096      | 0.668   | 0.505   | -0.126  | 0.255  |

**R-squared:** 0.386  
**Adj. R-squared:** 0.355  
**F-statistic:** 12.36 (p = 9.25e-11)  
**N:** 125  
**Durbin-Watson:** 1.854  

### 4.2 Variance Inflation Factors

| Variable             | VIF   |
|----------------------|-------|
| const                | 430.70|
| Log-GDP              | 3.95  |
| Log-Trade            | 1.29  |
| Edu-Expenditure      | 1.19  |
| Unemployment Rate    | 1.25  |
| Agri_Share_GDP       | 4.30  |
| Manuf_Share_GDP      | 1.11  |

### 4.3 Interpretation
- **Log_GDP**: Negative and significant. A 1% higher GDP per capita is associated with a 0.0467 point lower Gini.
- **Log_Trade**: Negative and significant. A 1% higher trade openness is associated with a 0.045 point lower Gini.
- **Edu_Expenditure**: Positive but insignificant.
- **Unemployment Rate**: Positive and significant. A 1 percentage point higher unemployment is associated with a 0.327 point higher Gini.
- **Agri_Share_GDP**: Negative and significant. A 1 point higher agricultural share is associated with a 0.454 point lower Gini.
- **Manuf_Share_GDP**: Positive but insignificant.

### 4.4 Summary of Empirical Patterns
1. Higher GDP per capita → lower Gini.
2. Higher trade openness → lower Gini.
3. Higher unemployment → higher Gini.
4. Larger agricultural sector → lower Gini.
5. No significant associations for education expenditure or manufacturing share.

---

## 5. Conclusion

### 5.1 Summary of Findings
- Negative association: GDP per capita, trade openness, agricultural share.
- Positive association: unemployment rate.
- Insignificant: education expenditure, manufacturing share.

These are descriptive correlations, not causal estimates.

### 5.2 Limitations
- Cross-sectional design limits causal inference.
- Gini is an aggregate measure; may miss within-country disparities.
- Data quality varies; top incomes may be under-sampled.
- Potential endogeneity not addressed.

### 5.3 Future Research
- Panel data methods.
- Instrumental variables for endogeneity.
- Disaggregated inequality measures.
- Regional heterogeneity analysis.

---

## References

1. Acemoglu, D., Johnson, S., & Robinson, J. A. (2001). The colonial origins of comparative development. *American Economic Review*.
2. Bourguignon, F. (2017). World changes in inequality. *BIS Working Papers*.
3. Cramer, C. (2003). Does inequality cause conflict? *Journal of International Development*.
4. Frieden, J. (2001). Inequality, causes and possible futures. *Harvard University*.
5. Joyce, J. P. (2008). Globalization and inequality. In S. Asefa (Ed.), *Globalization and International Development*.
6. Kuznets, S. (1955). Economic growth and income inequality. *American Economic Review*.
7. Stolper, W. F., & Samuelson, P. A. (1941). Protection and real wages. *Review of Economic Studies*.
8. Winters, L. A., McCulloch, N., & McKay, A. (2004). Trade liberalization and poverty. *Journal of Economic Literature*.


### 3.4 Model Specification
We estimate the following OLS regression with robust standard errors:
