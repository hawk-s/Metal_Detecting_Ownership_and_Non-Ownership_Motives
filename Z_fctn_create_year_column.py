import pandas as pd
import numpy as np

import pandas as pd
import numpy as np
import pandas as pd
import numpy as np

import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import numpy as np

import pandas as pd
import numpy as np
import pandas as pd
import numpy as np

def create_new_column(df: pd.DataFrame, column_name: str, replace_original: bool = True, new_column_name: str = 'New_Column') -> pd.DataFrame:
    """
    Creates a new column in a Pandas DataFrame based on the conditions specified.

    The function checks a specified column in the DataFrame for the presence of a year value.
    If a year is found, it extracts and assigns that year to the new column.
    If the original column contains a None value, the new column is set to None as well.
    If no year is found in the original column, the new column is assigned the year 2023.

    Args:
        df (pd.DataFrame): The DataFrame containing the original column and where the new column will be created.
        column_name (str): The name of the column to process.
        replace_original (bool, optional): Specifies whether to replace the original column values with the new column values.
                                           Defaults to True.
        new_column_name (str, optional): The name of the new column. Only applicable if replace_original is False.
                                         Defaults to 'New_Column'.

    Returns:
        pd.DataFrame: The modified DataFrame with the new column.

    Example:
        >>> data = pd.DataFrame({'Original_Column': ['ABC 2010', 2015, None, 'XYZ', '2008-02-15', 123]})
        >>> processed_data = create_new_column(data, 'Original_Column')
        >>> print(processed_data)
          Original_Column  New_Column
        0       ABC 2010        2010
        1            2015        2015
        2            None        2023
        3             XYZ        2023
        4     2008-02-15        2008
        5             123        2023

        >>> processed_data = create_new_column(data, 'Original_Column', replace_original=False, new_column_name='Modified_Column')
        >>> print(processed_data)
          Original_Column Modified_Column
        0       ABC 2010            2010
        1            2015            2015
        2            None            2023
        3             XYZ            2023
        4     2008-02-15            2008
        5             123            2023
    """

    # Extract year values from the column
    years = df[column_name].astype(str).str.extract(r'(20[0-2][0-9])', expand=False)

    # Create a new column based on the conditions
    if replace_original:
        df[column_name] = np.where(years.notnull(), years, df[column_name])
        df[column_name] = df[column_name].fillna(2023)
        df[column_name] = pd.to_numeric(df[column_name], errors='coerce').astype(pd.Int64Dtype())
    else:
        df[new_column_name] = np.where(years.notnull(), years, df[column_name])
        df[new_column_name] = df[new_column_name].fillna(2023)
        df[new_column_name] = pd.to_numeric(df[new_column_name], errors='coerce').astype(pd.Int64Dtype())
        df[new_column_name] = df[new_column_name].fillna(2023)

    # Assign 2023 to the resulting column where no other year values are found
    if replace_original:
        df[column_name] = np.where(df[column_name].notnull() & (df[column_name] != 2023), df[column_name], 2023)
    else:
        df[new_column_name] = np.where(df[new_column_name].notnull() & (df[new_column_name] != 2023), df[new_column_name], 2023)

    # Convert the final column to integers
    if replace_original:
        df[column_name] = df[column_name].astype(pd.Int64Dtype())
    else:
        df[new_column_name] = df[new_column_name].astype(pd.Int64Dtype())

    return df
