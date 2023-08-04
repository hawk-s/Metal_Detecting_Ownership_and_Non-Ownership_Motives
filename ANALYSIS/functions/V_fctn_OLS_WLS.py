import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.diagnostic import het_white
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
import pandas as pd
def ols_regression_wls(data, dependent_var, independent_vars):
    """
    Perform OLS regression with weighted least squares (WLS) and multicollinearity test.

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

    # Step 2: Compute the weights based on the inverse of the squared residuals
    model = sm.OLS(y, X)
    results = model.fit()
    weights = 1.0 / (results.resid**2)

    # Step 3: Fit the WLS model
    wls_model = sm.WLS(y, X, weights=weights)
    wls_results = wls_model.fit()

    # Step 4: Calculate regression summary
    regression_summary = wls_results.summary()

    # Step 5: Perform Breusch-Pagan test for heteroskedasticity
    #bp_test = het_breuschpagan(wls_results.resid, X)

    # Step 6: Perform White's test for heteroskedasticity
    #white_test = het_white(wls_results.resid, X)

    # Step 7: Perform Variance Inflation Factor (VIF) test for multicollinearity
    vif = pd.DataFrame()
    vif["Variable"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    # Step 8: Print the regression summary and test results
    print("Regression Summary:")
    print(regression_summary)
    #print("\nBreusch-Pagan Test for Heteroskedasticity:")   #does not make sense for WLS since WLS already accounts for heteroskedasticity...
    #print(bp_test)
    #print("\nWhite's Test for Heteroskedasticity:")
    #print(white_test)
    print("\nVariance Inflation Factor (VIF):")
    print(vif)

    return wls_results
