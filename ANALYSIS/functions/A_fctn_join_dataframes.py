import pandas as pd

def join_dataframes(excel_file1, excel_file2, output_file, merge_column, columns_to_delete=None):
    """
    Join two Excel files based on a common column, delete specified columns, and save the merged dataframe to an output Excel file.

    Args:
        excel_file1 (str): Path to the first Excel file.
        excel_file2 (str): Path to the second Excel file.
        output_file (str): Path to the output Excel file.
        merge_column (str): Column name to merge the dataframes on.
        columns_to_delete (list): List of column names to delete from the merged dataframe. Default is None.

    Returns:
        None
    """
    # Read the first Excel file
    df = pd.read_excel(excel_file2)

    # Read the second Excel file
    df_main = pd.read_excel(excel_file1)

    # Merge the dataframes based on the specified column
    joined = df_main.merge(df, on=merge_column, how='left')

    # Delete specified columns if any
    if columns_to_delete:
        joined.drop(columns=columns_to_delete, inplace=True)

    # Print the merged dataframe
    print(joined)

    # Save the merged dataframe to an output Excel file
    joined.to_excel(output_file)

'''
# Example usage
join_dataframes('lexikon_2018.xlsx', 'obce_na_join.xlsx', 'pou_joined_w_roz_final.xlsx', 'orp_obec', columns_to_delete=['column1', 'column2'])
'''