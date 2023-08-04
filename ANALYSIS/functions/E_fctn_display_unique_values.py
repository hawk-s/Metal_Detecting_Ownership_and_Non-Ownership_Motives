import pandas as pd

def display_unique_values(df, column_name):
    """
    Display the unique values and their counts for a specified column in a Pandas DataFrame.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the column.
        column_name (str): The name of the column to examine.

    Returns:
        pandas.DataFrame: A DataFrame with two columns: 'Value' and 'Count'.
                          Each row represents a unique value and its count in the column.
    """
    value_counts = df[column_name].value_counts()
    unique_values_df = pd.DataFrame({'Value': value_counts.index, 'Count': value_counts.values})
    return unique_values_df
