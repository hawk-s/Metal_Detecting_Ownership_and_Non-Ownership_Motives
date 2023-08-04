import pandas as pd

def remove_spaces(df, column_name, create_new=False, new_column_name=None):
    """
    Removes spaces from the values in the specified column of a pandas DataFrame.
    
    Parameters:
        - df (pandas.DataFrame): The DataFrame containing the column.
        - column_name (str): The name of the column to remove spaces from.
        - create_new (bool): Whether to create a new column or update the existing column. Default is False.
        - new_column_name (str): The name of the new column (if create_new is True). Default is None.
    
    Returns:
        The modified DataFrame with spaces removed from the specified column.
    """
    if create_new:
        if new_column_name is None:
            raise ValueError("Please provide a new_column_name when create_new is set to True.")
        df[new_column_name] = df[column_name].str.replace(" ", "")
    else:
        df[column_name] = df[column_name].str.replace(" ", "")
    
    return df
