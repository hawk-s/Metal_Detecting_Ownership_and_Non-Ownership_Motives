import pandas as pd

def drop_columns(df, columns):
    """
    Drop specified columns from a DataFrame.

    This function drops the specified columns from the given DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame from which the columns are to be dropped.
        columns (list): A list of column names to be dropped from the DataFrame.

    Returns:
        pandas.DataFrame: The DataFrame with the specified columns dropped.

    Example:
        df = pd.read_excel('summed_areas_pocet_final.xlsx')
        columns_to_drop = ['Unnamed: 0_x', 'Unnamed: 0', 'Unnamed: 0_y']
        result_df = drop_columns(df, columns_to_drop)
        print(result_df)
    """
    df.drop(columns=columns, inplace=True)
    return df
