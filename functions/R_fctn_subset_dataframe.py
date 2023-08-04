import pandas as pd

def subset_dataframe(df, column_name):
    """
    Subsets a DataFrame based on a given criterion of values higher than 0 in a specific column.
    
    Args:
        df (pandas.DataFrame): The DataFrame to be subsetted.
        column_name (str): The name of the column used for subsetting.
    
    Returns:
        pandas.DataFrame: The subsetted DataFrame containing only the observations
                          that meet the criterion.
    """
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    # Subset the DataFrame based on the criterion
    subset = df[df[column_name] > 0]
    
    return subset
