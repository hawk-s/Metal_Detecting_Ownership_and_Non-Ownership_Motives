import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_white, het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
from linearmodels import IV2SLS


import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.diagnostic import het_white
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

def ols_regression(data, dependent_var, independent_vars):
    """
    Perform OLS regression in Python.

    Args:
        data (DataFrame): The input DataFrame containing the data.
        dependent_var (str): The name of the dependent variable.
        independent_vars (list): A list of independent variables.

    Returns:
        RegressionResults: The fitted regression results object.
    """

    # Step 1: Prepare the data
    X = data[independent_vars]
    y = data[dependent_var]
    X = add_constant(X)  # Add a constant column for the intercept

    # Step 2: Fit the OLS model
    model = sm.OLS(y, X)
    results = model.fit()

    # Step 3: Calculate regression summary
    regression_summary = results.summary()

    # Step 4: Perform Breusch-Pagan test for heteroskedasticity
    bp_test = het_breuschpagan(results.resid, X)

    # Step 5: Perform White's test for heteroskedasticity
    #white_test = het_white(results.resid, X)

    # Step 6: Perform Variance Inflation Factor (VIF) test for multicollinearity
    vif = pd.DataFrame()
    vif["Variable"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    # Step 7: Perform Hausman test for endogeneity
    hausman_test = None  # Replace with the actual Hausman test code

    # Step 8: Print the regression summary and test results
    print("Regression Summary:")
    print(regression_summary)
    print("\nBreusch-Pagan Test for Heteroskedasticity:")
    print(bp_test)
    #print("\nWhite's Test for Heteroskedasticity:")
    #print(white_test)
    print("\nVariance Inflation Factor (VIF):")
    print(vif)
    print("\nHausman Test for Endogeneity:")
    print(hausman_test)

    return results







import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
'''
def ols_regression(data, dependent_var, independent_vars):
    """
    Perform OLS regression in Python.

    Args:
        data (DataFrame): The input DataFrame containing the data.
        dependent_var (str): The name of the dependent variable.
        independent_vars (list): A list of independent variables.

    Returns:
        dict: A dictionary containing the regression results and test summaries.
    """

    # Step 1: Prepare the data
    X = data[independent_vars]
    y = data[dependent_var]
    X = add_constant(X)  # Add a constant column for the intercept

    # Step 2: Fit the OLS model
    model = sm.OLS(y, X)
    results = model.fit()

    # Step 3: Calculate regression summary
    regression_summary = results.summary()

    # Step 4: Perform Breusch-Pagan test for heteroskedasticity
    bp_test = het_breuschpagan(results.resid, X)

    # Step 5: Perform Variance Inflation Factor (VIF) test for multicollinearity
    vif = pd.DataFrame()
    vif["Variable"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    # Step 6: Perform Hausman test for endogeneity
    hausman_test = None  # Replace with the actual Hausman test code

    # Step 7: Compile the results
    regression_results = {
        "Regression Summary": regression_summary,
        "Breusch-Pagan Test for Heteroskedasticity": bp_test,
        "Variance Inflation Factor (VIF)": vif,
        "Hausman Test for Endogeneity": hausman_test,
    }

    return regression_results
'''















#original fction:
'''
def ols_regression(data, dependent_var, independent_vars):
    """
    Perform OLS regression in Python.

    Args:
        data (DataFrame): The input DataFrame containing the data.
        dependent_var (str): The name of the dependent variable.
        independent_vars (list): A list of independent variables.

    Returns:
        dict: A dictionary containing the regression results and test summaries.
    """

    # Step 1: Prepare the data
    X = data[independent_vars]
    y = data[dependent_var]
    X = add_constant(X)  # Add a constant column for the intercept

    # Step 2: Fit the OLS model
    model = sm.OLS(y, X)
    results = model.fit()

    # Step 3: Calculate regression summary
    regression_summary = results.summary()

    # Step 4: Perform White's test for heteroskedasticity
    white_test = het_white(results.resid, X)

    # Step 5: Perform Breusch-Pagan test for heteroskedasticity
    bp_test = het_breuschpagan(results.resid, X)

    # Step 6: Perform Variance Inflation Factor (VIF) test for multicollinearity
    vif = pd.DataFrame()
    vif["Variable"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    # Step 7: Perform Hausman test for endogeneity
    iv_model = IV2SLS(y, X)
    iv_results = iv_model.fit(cov_type="unadjusted")
    hausman_test = iv_results.summary

    # Step 8: Compile the results
    regression_results = {
        "Regression Summary": regression_summary,
        "White's Test for Heteroskedasticity": white_test,
        "Breusch-Pagan Test for Heteroskedasticity": bp_test,
        "Variance Inflation Factor (VIF)": vif,
        "Hausman Test for Endogeneity": hausman_test
    }

    return regression_results
'''



#usage example::
import pandas as pd
'''
# Create a sample DataFrame
data = pd.DataFrame({
    'dependent_var': [1, 2, 3, 4, 5],
    'independent_var1': [2, 4, 6, 8, 10],
    'independent_var2': [3, 6, 9, 12, 15]
})

# Perform OLS regression
results = ols_regression(data, 'dependent_var', ['independent_var1', 'independent_var2'])

# Access the regression summary
print(results['Regression Summary'])
'''