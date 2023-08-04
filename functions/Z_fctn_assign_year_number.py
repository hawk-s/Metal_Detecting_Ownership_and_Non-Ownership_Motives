import pandas as pd
import numpy as np

def assign_year_numbers(df: pd.DataFrame, year_column: str, number_column: str) -> pd.DataFrame:
    """
    Creates a new column in a Pandas DataFrame assigning numbers to respective years.

    The function assigns numbers from 1 to 14 to the respective years in the specified column.

    Args:
        df (pd.DataFrame): The DataFrame containing the year column and where the number column will be created.
        year_column (str): The name of the column containing the years.
        number_column (str): The name of the new column to be created.

    Returns:
        pd.DataFrame: The modified DataFrame with the new number column.

    Example:
        >>> data = pd.DataFrame({'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]})
        >>> updated_data = assign_year_numbers(data, 'Year', 'Year_Number')
        >>> print(updated_data)
           Year  Year_Number
        0   2010            1
        1   2011            2
        2   2012            3
        3   2013            4
        4   2014            5
        5   2015            6
        6   2016            7
        7   2017            8
        8   2018            9
        9   2019           10
        10  2020           11
        11  2021           12
        12  2022           13
        13  2023           14
    """

    # Get unique years and sort them
    unique_years = np.sort(df[year_column].unique())

    # Create a dictionary mapping years to numbers
    year_number_map = {year: number for number, year in enumerate(unique_years, start=1)}

    # Create a new column with the assigned numbers
    df[number_column] = df[year_column].map(year_number_map)

    return df
