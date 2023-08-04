import pandas as pd

def merge_dataframes(df1, df2, column):
    """
    Merge two dataframes on a common column.

    Parameters:
        - df1 (pandas.DataFrame): The first dataframe.
        - df2 (pandas.DataFrame): The second dataframe.
        - column (str): The common column to merge on.

    Returns:
        pandas.DataFrame: The merged dataframe.

    Raises:
        ValueError: If the specified column does not exist in both dataframes.

    Example:
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': [2, 3, 4], 'age': [25, 30, 35]})
        merged_df = merge_dataframes(df1, df2, 'id')
        print(merged_df)

        Output:
           id     name  age
        0   2      Bob   25
        1   3  Charlie   30
    """
    if column not in df1.columns or column not in df2.columns:
        raise ValueError("The specified column does not exist in both dataframes.")

    merged_df = pd.merge(df1, df2, on=column)
    return merged_df
