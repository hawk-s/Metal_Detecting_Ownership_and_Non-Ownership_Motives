'''
def create_dummy_variable(data, column_name, missing_value=''):
    """
    Creates a dummy variable based on the condition that a cell in a specific column contains any value or is empty.

    Args:
        data (pandas.DataFrame): The dataframe containing the data.
        column_name (str): The name of the column to check for values.
        missing_value (optional, any): The value to be treated as missing or empty. Default is an empty string ('').

    Returns:
        pandas.DataFrame: A modified dataframe where the original variable is replaced with the resulting dummy variable.

    Example:
        >>> import pandas as pd
        >>> data = pd.DataFrame({'Name': ['John', 'Jane', '', 'Michael'],
        ...                      'Age': [25, 30, 35, 40]})
        >>> column_name = 'Name'
        >>> result = create_dummy_variable(data, column_name, missing_value='')
        >>> print(result)
             Name  Age
        0     1   25
        1     1   30
        2     0   35
        3     1   40

        >>> result = create_dummy_variable(data, column_name, missing_value='[]')
        >>> print(result)
             Name  Age
        0     1   25
        1     1   30
        2     1   35
        3     1   40
    """

    data[column_name] = data[column_name] != missing_value
    data[column_name] = data[column_name].astype(int)
    return data


import pandas as pd

def create_dummy_variable(data, column_name, missing_value=float('nan')):
    """
    Creates a dummy variable based on the condition that a cell in a specific column contains any value or is empty.
    Missing values (NaN) are replaced with the specified missing_value before creating the dummy variable.

    Args:
        data (pandas.DataFrame): The dataframe containing the data.
        column_name (str): The name of the column to check for values.
        missing_value (optional, any): The value to be treated as missing or empty. Default is NaN.

    Returns:
        pandas.DataFrame: A modified dataframe where the original variable is replaced with the resulting dummy variable.

    Example:
        >>> import pandas as pd
        >>> data = pd.DataFrame({'Name': ['John', 'Jane', '', 'Michael'],
        ...                      'Age': [25, 30, 35, 40]})
        >>> column_name = 'Name'
        >>> result = create_dummy_variable(data, column_name, missing_value='')
        >>> print(result)
           Name  Age
        0     1   25
        1     1   30
        2     0   35
        3     1   40

        >>> result = create_dummy_variable(data, column_name, missing_value='[]')
        >>> print(result)
           Name  Age
        0     1   25
        1     1   30
        2     1   35
        3     1   40
    """
    data[column_name] = data[column_name].fillna(missing_value)
    data[column_name] = data[column_name].notnull().astype(int)
    return data

'''
'''3rd attempt:
import pandas as pd

def create_dummy_variable(data, column_name, missing_value=None):
    """
    Creates a dummy variable based on the condition that a cell in a specific column contains any value or is empty.
    Missing values (NaN) or specific character values are replaced with the specified missing_value before creating the dummy variable.

    Args:
        data (pandas.DataFrame): The dataframe containing the data.
        column_name (str): The name of the column to check for values.
        missing_value (optional, any): The value to be treated as missing or empty. Default is None.

    Returns:
        pandas.DataFrame: A modified dataframe where the original variable is replaced with the resulting dummy variable.

    Example:
        >>> import pandas as pd
        >>> data = pd.DataFrame({'Name': ['John', 'Jane', '', 'Michael'],
        ...                      'Age': [25, 30, 35, 40]})
        >>> column_name = 'Name'
        >>> result = create_dummy_variable(data, column_name, missing_value='')
        >>> print(result)
           Name  Age
        0     1   25
        1     1   30
        2     0   35
        3     1   40

        >>> result = create_dummy_variable(data, column_name, missing_value='[]')
        >>> print(result)
           Name  Age
        0     1   25
        1     1   30
        2     1   35
        3     1   40
    """
    data[column_name] = data[column_name].fillna(missing_value)
    if missing_value is not None:
        data[column_name] = data[column_name] != missing_value
    data[column_name] = data[column_name].astype(int)
    return data
'''

'''
import pandas as pd
import numpy as np

def create_dummy_variable(data, column_name, missing_value=None):
    """
    Creates a dummy variable based on the condition that a cell in a specific column contains any value or is empty.
    Missing values (NaN) or specific character values are replaced with the specified missing_value before creating the dummy variable.

    Args:
        data (pandas.DataFrame): The dataframe containing the data.
        column_name (str): The name of the column to check for values.
        missing_value (optional, any): The value to be treated as missing or empty. Default is None.

    Returns:
        pandas.DataFrame: A modified dataframe where the original variable is replaced with the resulting dummy variable.

    Example:
        >>> import pandas as pd
        >>> data = pd.DataFrame({'Name': ['John', 'Jane', '', 'Michael'],
        ...                      'Age': [25, 30, 35, 40]})
        >>> column_name = 'Name'
        >>> result = create_dummy_variable(data, column_name, missing_value='')
        >>> print(result)
           Name  Age
        0     1   25
        1     1   30
        2     0   35
        3     1   40

        >>> result = create_dummy_variable(data, column_name, missing_value='[]')
        >>> print(result)
           Name  Age
        0     1   25
        1     1   30
        2     1   35
        3     1   40
    """
    if missing_value is None:
        data[column_name] = data[column_name].notnull().astype(int)
    else:
        data[column_name] = np.where(data[column_name].fillna('').eq(missing_value), 0, 1)
    return data
'''
#The final one:
'''
import pandas as pd
import numpy as np

def create_dummy_variable(data, column_name, missing_values=None, replace=True):
    """
    Creates a dummy variable based on the condition that a cell in a specific column contains any value or is empty.
    Missing values (NaN) or specific character values are replaced with the specified missing_values before creating the dummy variable.

    Args:
        data (pandas.DataFrame): The dataframe containing the data.
        column_name (str): The name of the column to check for values.
        missing_values (optional, list or None): The values to be treated as missing or empty. Default is None.
        replace (bool): Whether to replace the old column with the new dummy variable. Default is True.

    Returns:
        pandas.DataFrame: A modified dataframe where the original variable is replaced with the resulting dummy variable,
        if replace=True. Otherwise, a new column containing the dummy variable is added.

    Example:
        >>> import pandas as pd
        >>> data = pd.DataFrame({'Name': ['John', 'Jane', '', 'Michael'],
        ...                      'Age': [25, 30, 35, 40]})
        >>> column_name = 'Name'
        >>> result = create_dummy_variable(data, column_name, missing_values=['', np.nan])
        >>> print(result)
           Name  Age
        0     1   25
        1     1   30
        2     0   35
        3     1   40

        >>> result = create_dummy_variable(data, column_name, missing_values=['[]'], replace=False)
        >>> print(result)
           Name  Age  Name_dummy
        0     1   25            1
        1     1   30            1
        2     1   35            0
        3     1   40            1
    """
    if missing_values is None:
        dummy_variable = data[column_name].notnull().astype(int)
    else:
        dummy_variable = np.where(data[column_name].fillna('').isin(missing_values), 0, 1)

    if replace:
        data[column_name] = dummy_variable
    else:
        new_column_name = column_name + '_dummy'
        data[new_column_name] = dummy_variable

    return data
'''
#Example usage:
'''
df = create_dummy_variable(df, 'column_name', missing_values=[0, np.nan], replace=True)
#or:
df = create_dummy_variable(df, 'column_name', missing_values=[0, np.nan], replace=False)
'''

#Ok, well really final:
'''
import pandas as pd
import numpy as np

def create_dummy_variable(data, column_name, missing_values=None, replace=True):
    """
    Creates a dummy variable based on the condition that a cell in a specific column contains any value or is empty.
    Missing values (NaN) or specific values are replaced with the specified missing_values before creating the dummy variable.

    Args:
        data (pandas.DataFrame): The dataframe containing the data.
        column_name (str): The name of the column to check for values.
        missing_values (optional, list or None): The values to be treated as missing or empty. Default is None.
        replace (bool): Whether to replace the old column with the new dummy variable. Default is True.

    Returns:
        pandas.DataFrame: A modified dataframe where the original variable is replaced with the resulting dummy variable,
        if replace=True. Otherwise, a new column containing the dummy variable is added.

    Example:
        >>> import pandas as pd
        >>> data = pd.DataFrame({'Name': ['John', 'Jane', '', 'Michael'],
        ...                      'Age': [25, 30, 35, 40]})
        >>> column_name = 'Name'
        >>> result = create_dummy_variable(data, column_name, missing_values=['', None])
        >>> print(result)
           Name  Age
        0     1   25
        1     1   30
         2     0   35
        3     1   40

        >>> result = create_dummy_variable(data, column_name, missing_values=['[]'], replace=False)
        >>> print(result)
           Name  Age  Name_dummy
        0     1   25            1
        1     1   30            1
        2     1   35            0
        3     1   40            1
    """
    if missing_values is None:
        dummy_variable = data[column_name].notnull().astype(int)
    else:
        dummy_variable = np.where(data[column_name].fillna('').apply(lambda x: x in missing_values or pd.isna(x)), 0, 1)

    if replace:
        data[column_name] = dummy_variable
    else:
        new_column_name = column_name + '_dummy'
        data[new_column_name] = dummy_variable

    return data
'''

























#I really believe...: The best one so far:

import pandas as pd
import numpy as np

def create_dummy_variable(data, column_name, missing_values=None, replace=True):
    """
    Creates a dummy variable based on the condition that a cell in a specific column contains any value or is empty.
    Missing values (NaN) or specific values are replaced with the specified missing_values before creating the dummy variable.

    Args:
        data (pandas.DataFrame): The dataframe containing the data.
        column_name (str): The name of the column to check for values.
        missing_values (optional, single value, list, or None): The value(s) to be treated as missing or empty. Default is None.
        replace (bool): Whether to replace the old column with the new dummy variable. Default is True.

    Returns:
        pandas.DataFrame: A modified dataframe where the original variable is replaced with the resulting dummy variable,
        if replace=True. Otherwise, a new column containing the dummy variable is added.
    """
    if missing_values is None:
        dummy_variable = data[column_name].notnull().astype(int)
    elif isinstance(missing_values, list):
        if None in missing_values or np.nan in missing_values:
            dummy_variable = np.where(data[column_name].fillna('').apply(lambda x: x in missing_values or pd.isna(x) or x == ''), 0, 1)
        else:
            dummy_variable = np.where(data[column_name].fillna('').apply(lambda x: x in missing_values), 0, 1)
    else:
        dummy_variable = np.where(data[column_name].fillna('').eq(missing_values) | data[column_name].fillna('').eq(0), 0, 1)

    if replace:
        data[column_name] = dummy_variable
    else:
        new_column_name = column_name + '_dummy'
        data[new_column_name] = dummy_variable

    return data





#will see: 
import pandas as pd
import numpy as np

def create_dummy_variable_specific(data, column_name, missing_values=None, replace=True):
    """
    Creates a dummy variable based on the condition that a cell in a specific column contains any value, is zero, or is NaN.
    Missing values (NaN) or specific values are replaced with the specified missing_values before creating the dummy variable.

    Args:
        data (pandas.DataFrame): The dataframe containing the data.
        column_name (str): The name of the column to check for values.
        missing_values (optional, single value, list, or None): The value(s) to be treated as missing or empty. Default is None.
        replace (bool): Whether to replace the old column with the new dummy variable. Default is True.

    Returns:
        pandas.DataFrame: A modified dataframe where the original variable is replaced with the resulting dummy variable,
        if replace=True. Otherwise, a new column containing the dummy variable is added.
    """
    dummy_variable = np.where(data[column_name].eq(0), 0, np.where(data[column_name].isnull(), np.nan, 1))

    if replace:
        data[column_name] = dummy_variable
    else:
        new_column_name = column_name + '_dummy'
        data[new_column_name] = dummy_variable

    return data




















#ah...:)
'''
import pandas as pd
import numpy as np

def create_dummy_variable(data, column_name, missing_values=None, replace=True, empty_value='', true_value=1, false_value=0):
    """
    Creates a dummy variable based on the condition that a cell in a specific column contains any value, is empty, or is equal to 0.
    Missing values (NaN) or specific values are replaced with the specified missing_values before creating the dummy variable.

    Args:
        data (pandas.DataFrame): The dataframe containing the data.
        column_name (str): The name of the column to check for values.
        missing_values (optional, single value, list, or None): The value(s) to be treated as missing or empty. Default is None.
        replace (bool): Whether to replace the old column with the new dummy variable. Default is True.
        empty_value (optional): The value to assign to cells that are empty. Default is an empty string ('').
        true_value (optional): The value to assign to cells that satisfy the condition. Default is 1.
        false_value (optional): The value to assign to cells that do not satisfy the condition. Default is 0.

    Returns:
        pandas.DataFrame: A modified dataframe where the original variable is replaced with the resulting dummy variable,
        if replace=True. Otherwise, a new column containing the dummy variable is added.
    """
    if missing_values is None:
        dummy_variable = np.where(data[column_name].fillna('').eq('') | data[column_name].fillna('').eq(0), empty_value, true_value)
    elif isinstance(missing_values, list):
        dummy_variable = np.where(
            data[column_name].fillna('').apply(lambda x: x in missing_values or pd.isna(x) or x == ''),
            empty_value,
            np.where(data[column_name].fillna('').isin(missing_values), false_value, true_value)
        )
    else:
        dummy_variable = np.where(
            data[column_name].fillna('').eq(missing_values) | data[column_name].fillna('').eq(0),
            empty_value,
            np.where(data[column_name].fillna('').eq(missing_values), false_value, true_value)
        )

    if replace:
        data[column_name] = dummy_variable
    else:
        new_column_name = column_name + '_dummy'
        data[new_column_name] = dummy_variable

    return data
'''

#I really believe 30.5.23, 13.05
#predposledni, ta pred tou co je nad timto popisem byla nej...
'''
import pandas as pd
import numpy as np

def create_dummy_variable(data, column_name, missing_values=None, replace=True, empty_value='', true_value=1, false_value=0):
    """
    Creates a dummy variable based on the condition that a cell in a specific column contains any value, is empty, or is equal to 0.
    Missing values (NaN) or specific values are replaced with the specified missing_values before creating the dummy variable.

    Args:
        data (pandas.DataFrame): The dataframe containing the data.
        column_name (str): The name of the column to check for values.
        missing_values (optional, single value, list, or None): The value(s) to be treated as missing or empty. Default is None.
        replace (bool): Whether to replace the old column with the new dummy variable. Default is True.
        empty_value (optional): The value to assign to cells that are empty. Default is an empty string ('').
        true_value (optional): The value to assign to cells that satisfy the condition. Default is 1.
        false_value (optional): The value to assign to cells that do not satisfy the condition. Default is 0.

    Returns:
        pandas.DataFrame: A modified dataframe where the original variable is replaced with the resulting dummy variable,
        if replace=True. Otherwise, a new column containing the dummy variable is added.
    """
    if missing_values is None:
        dummy_variable = np.where(data[column_name].fillna('').eq('') | data[column_name].fillna('').eq(0), empty_value, true_value)
    elif isinstance(missing_values, list):
        dummy_variable = np.where(
            data[column_name].fillna('').apply(lambda x: x in missing_values or pd.isna(x) or x == ''),
            empty_value,
            np.where(data[column_name].fillna('').isin(missing_values), false_value, true_value)
        )
    else:
        dummy_variable = np.where(
            data[column_name].fillna('').eq(missing_values) | data[column_name].fillna('').eq(0),
            empty_value,
            np.where(data[column_name].fillna('').eq(missing_values), false_value, true_value)
        )

    if replace:
        data[column_name] = dummy_variable
    else:
        new_column_name = column_name + '_dummy'
        data[new_column_name] = dummy_variable

    return data

'''

#Not good...
'''
import pandas as pd

def create_dummy_variable(data, column, search_values, replace_column=False, new_column_name=None, dummy_values=None):
    """
    Create a dummy variable from a specified column in a pandas DataFrame.
    
    Args:
        data (pandas.DataFrame): The DataFrame containing the column.
        column (str): The name of the column to create a dummy variable from.
        search_values (list or str): The value(s) to search for in the column.
                                    If a list, each value corresponds to a specific dummy value.
                                    If a string, all occurrences will be replaced with the same dummy value.
                                    If None, missing values will be treated separately.
        replace_column (bool): True to replace the existing column with the dummy variable.
                               False (default) to create a new column for the dummy variable.
        new_column_name (str): The name of the new column (required if replace_column is False).
        dummy_values (list or str): The dummy value(s) corresponding to the search value(s).
                                    If a list, each value corresponds to a specific dummy value.
                                    If a string, all occurrences will be replaced with the same dummy value.
                                    If None, default dummy values will be used.
    
    Returns:
        pandas.DataFrame: The DataFrame with the dummy variable column.
    """
    # Make a copy of the DataFrame to avoid modifying the original data
    data_copy = data.copy()
    
    # Handle missing values (None)
    if search_values is None or (isinstance(search_values, list) and None in search_values):
        # Treat missing values as a separate case
        if replace_column:
            data_copy[column].fillna('', inplace=True)
        else:
            data_copy[new_column_name] = data_copy[column].fillna('')
        
    else:
        # Replace search values with dummy values
        if isinstance(search_values, list):
            if dummy_values is None:
                dummy_values = [0] * len(search_values)  # Default dummy values (0)
            
            for search_value, dummy_value in zip(search_values, dummy_values):
                data_copy[column] = data_copy[column].replace(search_value, dummy_value)
        else:
            if dummy_values is None:
                dummy_values = 1  # Default dummy value (1)
            
            data_copy[column] = data_copy[column].replace(search_values, dummy_values)
    
    # Rename or replace the column as required
    if replace_column:
        data_copy.rename(columns={column: new_column_name}, inplace=True)
    elif new_column_name is not None:
        data_copy[new_column_name] = data_copy[column]
    
    return data_copy
'''