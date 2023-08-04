import pandas as pd

def get_summary_statistics(df):
    """
    Calculates summary statistics for each column in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame for which to calculate the summary statistics.

    Returns:
        pandas.DataFrame: A DataFrame containing the count, unique, top, and frequency measures for each column.
    """
    summary = pd.DataFrame({
        'count': df.count(),
        'unique': df.nunique(),
        'mode': df.mode().iloc[0],
        'frequency': df.apply(lambda x: x.value_counts().iloc[0])
    })

    return summary

# Example usage:
'''
data = {
    'Column1': [1, 2, 2, 3, 3, 3],
    'Column2': [4, 4, 4, 5, 5, 6],
    'Column3': [7, 7, 8, 8, 9, 9]
}

df = pd.DataFrame(data)
summary = get_summary_statistics(df)
print(summary)
'''

import pandas as pd

def get_extended_summary_statistics(df):
    """
    Calculates extended summary statistics for each column in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame for which to calculate the summary statistics.

    Returns:
        pandas.DataFrame: A DataFrame containing count, mean, std, min, 25%, 50%, 75%, and max measures for each column.
    """
    summary = df.describe().transpose()
    summary = summary[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']]
    
    # Limit decimal places to 2
    summary = summary.round(2)
    
    return summary

