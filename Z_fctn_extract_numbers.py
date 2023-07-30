import pandas as pd
import re
import pandas as pd
import re
import numpy as np

def extract_numbers(df, columns):
    """
    Extracts numbers from specified columns of a DataFrame and returns a modified DataFrame.

    Parameters:
        df (pandas.DataFrame): The input DataFrame.
        columns (list): A list of column names to apply the number extraction operation.

    Returns:
        pandas.DataFrame: A modified DataFrame with only the extracted numbers.

    Example:
        >>> df = pd.DataFrame({'Column1': ['123', 456, 'def789'], 'Column2': ['abc', 123.45, 456]})
        >>> extract_numbers(df, ['Column1', 'Column2'])
          Column1  Column2
        0     123      NaN
        1     456   123.45
        2     789    456.0
    """
    def extract_numbers_from_cell(value):
        if isinstance(value, str):
            numbers = re.findall(r'\d+', value)
            if numbers:
                return float(numbers[0]) if '.' in numbers[0] else int(numbers[0])
        elif isinstance(value, (int, float)):
            return value
        return np.nan

    df = df.copy()
    for column in columns:
        df[column] = df[column].apply(extract_numbers_from_cell)

    return df
