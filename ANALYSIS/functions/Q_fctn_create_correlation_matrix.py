import seaborn as sns
import matplotlib.pyplot as plt

def create_correlation_matrix(dataframe, columns, title):
    """
    Create a correlation matrix and plot a heatmap.

    Parameters:
        dataframe (pandas.DataFrame): The DataFrame containing the data.
        columns (list): List of column names to include in the correlation matrix.
        title (str): Title of the correlation matrix plot.

    Returns:
        None
    """

    # Calculate Correlation Matrix
    correlation_matrix = dataframe[columns].corr()

    # Plotting Correlation Matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5, vmin=-1, vmax=1)
    plt.title(title)
    plt.show()


# Example usage:
'''
columns = ['link', 'experience', 'contributions', 'comments', 'artifacts', 'coins',
           'residence_additional_info', 'real_net_monetary_index', 'finds_rate',
           'coins_rate', 'detector_expensive_dummy', 'localities_rate']
title = 'Correlation Matrix'

create_correlation_matrix(columns, title)
'''