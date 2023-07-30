import numpy as np
import statsmodels.api as sm
from scipy.stats import chi2
'''
def wald_test(model, hypotheses_variables):
    """
    Perform a Wald test for joint significance of variables in logistic regression (logit) or probit models.

    Parameters:
        model : statsmodels.discrete.discrete_model.BinaryModel
            The fitted logistic regression (logit) or probit model object.
        hypotheses_variables : list of str
            A list of variable names for which joint significance is to be tested.

    Returns:
        wald_statistic : float
            The Wald test statistic.
        p_value : float
            The p-value associated with the Wald test statistic.
    """
    # Get the estimated coefficients and covariance matrix
    params = model.params
    cov_matrix = model.cov_params()

    # Get the coefficient names from the model
    coefficient_names = model.model.exog_names

    # Index of the coefficients corresponding to the hypotheses variables
    hypotheses_indices = [coefficient_names.index(var) for var in hypotheses_variables]

    # Extract the submatrix from the covariance matrix and coefficients vector
    hypotheses_cov_matrix = cov_matrix[hypotheses_indices][:, hypotheses_indices]
    hypotheses_params = params[hypotheses_indices]

    # Calculate the Wald test statistic
    wald_statistic = np.dot(np.dot(hypotheses_params, np.linalg.inv(hypotheses_cov_matrix)), hypotheses_params)

    # Degrees of freedom for the chi-square distribution
    df = len(hypotheses_variables)

    # Calculate the p-value associated with the Wald test statistic
    p_value = 1 - chi2.cdf(wald_statistic, df)

    return wald_statistic, p_value
'''
# Example usage:
'''
# Assuming your model2_LOGIT is already fitted and the DataFrame containing the data used to fit the model is df_log_3.
# Define the variables for the joint significance test
hypotheses_variables = ['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate']

# Perform the Wald test
wald_statistic, p_value = wald_test(model2_LOGIT, hypotheses_variables)

print("Wald Test Statistic:", wald_statistic)
print("P-value:", p_value)
'''


import numpy as np
import statsmodels.api as sm
from scipy.stats import chi2

def wald_test(model, hypotheses_variables):
    """
    Perform a Wald test for joint significance of variables in logistic regression (logit) or probit models.

    Parameters:
        model : statsmodels.discrete.discrete_model.BinaryModel
            The fitted logistic regression (logit) or probit model object.
        hypotheses_variables : list of str
            A list of variable names for which joint significance is to be tested.

    Returns:
        wald_statistic : float
            The Wald test statistic.
        p_value : float
            The p-value associated with the Wald test statistic.
    """
    # Get the estimated coefficients and covariance matrix
    params = model.params
    cov_matrix = model.cov_params()

    # Get the coefficient names from the model
    coefficient_names = model.model.exog_names

    # Index of the coefficients corresponding to the hypotheses variables
    hypotheses_indices = [coefficient_names.index(var) for var in hypotheses_variables]

    # Extract the submatrix from the covariance matrix and coefficients vector
    hypotheses_cov_matrix = cov_matrix.loc[hypotheses_variables, hypotheses_variables]
    hypotheses_params = params[hypotheses_variables]

    # Calculate the Wald test statistic
    wald_statistic = np.dot(np.dot(hypotheses_params, np.linalg.inv(hypotheses_cov_matrix)), hypotheses_params)

    # Degrees of freedom for the chi-square distribution
    df = len(hypotheses_variables)

    # Calculate the p-value associated with the Wald test statistic
    p_value = 1 - chi2.cdf(wald_statistic, df)

    return wald_statistic, p_value

# Rest of the logit_regression_roc_wald function remains the same.
