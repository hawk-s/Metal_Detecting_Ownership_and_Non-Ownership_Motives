import statsmodels.api as sm
from sklearn.metrics import roc_curve, auc
import pandas as pd
import matplotlib.pyplot as plt
'''
def logit_regression_roc(data, dependent_var, independent_vars):
    """
    Perform Logit regression and compute ROC curve.

    Args:
        data (DataFrame): The input DataFrame containing the data.
        dependent_var (str): The name of the dependent variable.
        independent_vars (list): A list of independent variables.

    Returns:
        LogitResults: The fitted Logit regression results object.
    """

    # Step 1: Prepare the data
    X = data[independent_vars]
    y = data[dependent_var]
    X = sm.add_constant(X)  # Add a constant column for the intercept

    # Step 2: Fit the Logit model
    model = sm.Logit(y, X)
    results = model.fit()

    # Step 3: Calculate predicted probabilities
    predicted_probs = results.predict(X)

    # Step 4: Compute ROC curve and AUC
    fpr, tpr, thresholds = roc_curve(y, predicted_probs)
    roc_auc = auc(fpr, tpr)

    # Step 5: Plot ROC curve
    plt.plot(fpr, tpr, label='ROC curve (AUC = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], 'k--')  # Diagonal line
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.show()

    # Step 6: Print the regression summary and AUC
    print("Logit Regression Summary:")
    print(results.summary())
    print("\nArea Under the Curve (AUC):", roc_auc)

    return results
'''
import statsmodels.api as sm
from sklearn.metrics import roc_curve, auc, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from functions.Z_fctn_WALD_TEST_JOINT import wald_test
# Add the previously defined wald_test function here (skip if it's in a separate file)

import statsmodels.api as sm
from sklearn.metrics import roc_curve, auc, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Add the previously defined wald_test function here (skip if it's in a separate file)

def logit_regression_roc_wald(data, dependent_var, independent_vars, pev_vars=None, ape_vars=None, hypotheses_variables=None):
    """
    Perform Logit regression, compute ROC curve, confusion matrix, Partial Effect At the Average (PEA),
    Average Partial Effect (APE), and Wald test for joint significance of variables.

    Args:
        data (DataFrame): The input DataFrame containing the data.
        dependent_var (str): The name of the dependent variable.
        independent_vars (list): A list of independent variables.
        pev_vars (list or None): A list of variables to compute Partial Effect At the Average (PEA).
                                 If None, no PEA will be computed.
        ape_vars (list or None): A list of variables to compute Average Partial Effect (APE).
                                 If None, no APE will be computed.
        hypotheses_variables (list or None): A list of variables to test for joint significance using the Wald test.
                                             If None, no Wald test will be performed.

    Returns:
        LogitResults: The fitted Logit regression results object.
    """

    # Step 1: Prepare the data
    X = data[independent_vars]
    y = data[dependent_var]
    X = sm.add_constant(X)  # Add a constant column for the intercept

    # Step 2: Fit the Logit model
    model = sm.Logit(y, X)
    results = model.fit()

    # Step 3: Calculate predicted probabilities
    predicted_probs = results.predict(X)

    # Step 4: Compute ROC curve and AUC
    fpr, tpr, thresholds = roc_curve(y, predicted_probs)
    roc_auc = auc(fpr, tpr)

    # Step 5: Plot ROC curve
    plt.plot(fpr, tpr, label='ROC curve (AUC = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], 'k--')  # Diagonal line
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.show()

    # Step 6: Compute confusion matrix
    y_pred = (predicted_probs > 0.5).astype(int)
    confusion_mat = pd.crosstab(index=y, columns=y_pred, rownames=['Actual'], colnames=['Predicted'])
    print("Confusion Matrix:")
    print(confusion_mat)

    # Step 7: Compute Partial Effect At the Average (PEA)
    if pev_vars:
        pev_results = results.get_margeff()
        print("\nPartial Effect At the Average (PEA):")
        print(pev_results.summary())

    # Step 8: Compute Average Partial Effect (APE)
    if ape_vars:
        ape_results = results.get_margeff(at='mean')
        print("\nAverage Partial Effect (APE):")
        print(ape_results.summary())

    # Step 9: Print the regression summary and AUC
    print("\nLogit Regression Summary:")
    print(results.summary())
    print("\nArea Under the Curve (AUC):", roc_auc)

    # Step 10: Perform the Wald test for joint significance of variables
    if hypotheses_variables:
        wald_statistic, p_value = wald_test(results, hypotheses_variables)
        print("\nWald Test Statistic:", wald_statistic)
        print("P-value:", p_value)

    return results

# Example usage:
'''
# Assuming the DataFrame is df_log_3, and you want to test the joint significance of certain variables using the Wald test.
# Define the variables for the joint significance test
hypotheses_variables = ['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate']

# Perform Logit regression, ROC curve, confusion matrix, PEA, APE, and Wald test
logit_results = logit_regression_roc_wald(df_log_3, dependent_var='rate_artifs_dummy', independent_vars=['log_experience', 'log_contributions'], hypotheses_variables=hypotheses_variables)
'''