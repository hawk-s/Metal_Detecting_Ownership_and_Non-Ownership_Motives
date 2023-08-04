import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.diagnostic import het_white
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
import pandas as pd
'''
def ols_regression_robust(data, dependent_var, independent_vars):
    """
    Perform OLS regression with heteroskedasticity-robust standard errors and multicollinearity test.

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

    # Step 3: Compute heteroskedasticity-robust standard errors
    robust_results = results.get_robustcov_results(cov_type='HC1')

    # Step 4: Calculate regression summary
    regression_summary = robust_results.summary()

    # Step 5: Perform Breusch-Pagan test for heteroskedasticity
    bp_test = het_breuschpagan(robust_results.resid, X)

    # Step 6: Perform White's test for heteroskedasticity
    #white_test = het_white(robust_results.resid, X)

    # Step 7: Perform Variance Inflation Factor (VIF) test for multicollinearity
    vif = pd.DataFrame()
    vif["Variable"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    # Step 8: Print the regression summary and test results
    print("Regression Summary:")
    print(regression_summary)
    print("\nBreusch-Pagan Test for Heteroskedasticity:")
    print(bp_test)
    #print("\nWhite's Test for Heteroskedasticity:")
    #print(white_test)
    print("\nVariance Inflation Factor (VIF):")
    print(vif)

    return results
'''
#with the confusion matrix for the binary outcome:
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.diagnostic import het_white
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
import pandas as pd
import numpy as np

def ols_regression_robust(data, dependent_var, independent_vars):
    """
    Perform OLS regression with heteroskedasticity-robust standard errors and multicollinearity test.

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

    # Step 3: Compute heteroskedasticity-robust standard errors
    robust_results = results.get_robustcov_results(cov_type='HC1')

    # Step 4: Calculate regression summary
    regression_summary = robust_results.summary()

    # Step 5: Perform Breusch-Pagan test for heteroskedasticity
    bp_test = het_breuschpagan(robust_results.resid, X)

    # Step 6: Perform White's test for heteroskedasticity
    #white_test = het_white(robust_results.resid, X)

    # Step 7: Perform Variance Inflation Factor (VIF) test for multicollinearity
    vif = pd.DataFrame()
    vif["Variable"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    # Step 8: Print the regression summary and test results
    print("Regression Summary:")
    print(regression_summary)
    print("\nBreusch-Pagan Test for Heteroskedasticity:")
    print(bp_test)
    #print("\nWhite's Test for Heteroskedasticity:")
    #print(white_test)
    print("\nVariance Inflation Factor (VIF):")
    print(vif)

    # Step 9: Compute confusion matrix (for binary dependent variable)
    if len(np.unique(y)) == 2:
        predicted_probs = results.predict(X)  # Predicted probabilities
        predicted_classes = np.where(predicted_probs >= 0.5, 1, 0)  # Predicted classes based on a threshold (0.5)

        confusion_matrix = pd.crosstab(index=y, columns=predicted_classes, rownames=['Actual'], colnames=['Predicted'])
        print("\nConfusion Matrix:")
        print(confusion_matrix)

    return results
