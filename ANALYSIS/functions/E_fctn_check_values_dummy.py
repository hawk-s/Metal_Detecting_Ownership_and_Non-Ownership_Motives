import pandas as pd

def check_values(data, search_values, column, result_column_name):
    """
    Checks if the given values are contained within the specified column of the input dataframe.

    Args:
        data (pandas.DataFrame): The dataframe to search within.
        search_values (list or pandas.DataFrame): The list or dataframe of values to search for.
        column (str): The name of the column in the dataframe to search within.
        result_column_name (str): The name of the resulting column.

    Returns:
        pandas.DataFrame: The updated dataframe with a new column indicating if the values are present (1) or not (0).
    """
    # Convert search_values to a list if it's a dataframe
    if isinstance(search_values, pd.DataFrame):
        search_values = search_values.squeeze().tolist()

    # Create a function to check if any value is contained within the column
    def check_value(row):
        for value in search_values:
            if value in row:
                return 1
        return 0

    # Apply the function to create a new column in the dataframe
    data[result_column_name] = data[column].apply(check_value)

    return data



#Example usage
'''

# Create the dataframe to search within
df = pd.DataFrame({'col': ['minelab', 'tesorotejon', 'vanguish540', 'lobost,nox800', 'manticoregpx5000']})

# Define the values to search for
values = ['manticore', 'ctx3030', 'gpx5000']

# Specify the name for the resulting column
result_column = 'contains_value'

# Use the function to check if the values are present in the dataframe
result = check_values(df, values, 'col', result_column)

# Print the updated dataframe
print(result)
'''
#output: 
'''
              col  contains_value
0         minelab               0
1     tesorotejon               0
2     vanguish540               0
3    lobost,nox800               0
4  manticoregpx5000               1
'''