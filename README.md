
---

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
