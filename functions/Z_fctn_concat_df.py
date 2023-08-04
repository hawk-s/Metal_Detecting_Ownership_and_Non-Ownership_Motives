import pandas as pd

def concat_dataframes(dataframes):
    """
    Concatenates multiple DataFrames vertically while adding a new column to indicate the source DataFrame.

    Parameters:
    dataframes (list): List of DataFrames to concatenate.

    Returns:
    pd.DataFrame: Concatenated DataFrame with a new 'Source' column.

    """
    # Create an empty list to store modified DataFrames
    modified_dfs = []

    # Iterate over the input DataFrames
    for i, df in enumerate(dataframes, start=1):
        # Add a new column 'period' with the corresponding number
        df['period'] = i
        # Append the modified DataFrame to the list
        modified_dfs.append(df)

    # Concatenate the modified DataFrames vertically
    result = pd.concat(modified_dfs)

    # Reset the index and drop the old index column
    result = result.reset_index(drop=True)

    return result

#example: 
'''
# Sample DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
df3 = pd.DataFrame({'A': [13, 14, 15], 'B': [16, 17, 18]})

# Concatenate the DataFrames
result = concat_dataframes([df1, df2, df3])

# Display the result
print(result)

'''