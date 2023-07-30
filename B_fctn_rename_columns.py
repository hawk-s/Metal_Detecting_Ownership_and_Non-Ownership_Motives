import pandas as pd

def rename_columns(dataframe, column_map):
    """
    Renames the names of specified columns in a Pandas dataframe.

    Args:
        dataframe (pandas.DataFrame): The dataframe to be modified.
        column_map (dict): A dictionary mapping old column names to new column names.

    Returns:
        pandas.DataFrame: The modified dataframe with renamed columns.
    """

    # Create a copy of the dataframe to avoid modifying the original
    renamed_df = dataframe.copy()

    # Rename the columns using the column_map dictionary
    renamed_df.rename(columns=column_map, inplace=True)

    return renamed_df
