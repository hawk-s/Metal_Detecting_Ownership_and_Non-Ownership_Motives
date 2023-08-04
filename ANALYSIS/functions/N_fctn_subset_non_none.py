import pandas as pd

def subset_non_none_values(df, column):
    """
    Subsets a Pandas DataFrame to rows that contain non-None values in a specific column.

    Args:
        df (pandas.DataFrame): The DataFrame to subset.
        column (str): The name of the column to check for non-None values.

    Returns:
        pandas.DataFrame: The subset DataFrame containing rows with non-None values in the specified column.
    """
    subset_df = df[df[column].notna()]
    return subset_df
