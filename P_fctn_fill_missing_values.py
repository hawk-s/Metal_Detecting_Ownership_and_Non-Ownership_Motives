import pandas as pd

def fill_missing_values(dataframe, fill_values):
    """
    Fill missing values in specified columns of a Pandas DataFrame with provided values.

    Args:
        dataframe (pandas.DataFrame): The DataFrame containing the columns to be filled.
        fill_values (dict): A dictionary specifying the values to fill for each column.
            The keys are the column names, and the values are the corresponding fill values.

    Returns:
        pandas.DataFrame: The updated DataFrame with filled missing values.

    Example:
        data = {'Column1': [1, 2, None, 4, 5],
                'Column2': [None, 10, None, 30, 40],
                'Column3': [100, 200, 300, None, 500]}
        df = pd.DataFrame(data)

        fill_values = {'Column1': 0,
                       'Column2': 'missing',
                       'Column3': -1}

        filled_df = fill_missing_values(df, fill_values)
        print(filled_df)
    """
    dataframe.fillna(fill_values, inplace=True)
    return dataframe
