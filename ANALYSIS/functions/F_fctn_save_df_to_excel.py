import pandas as pd

def save_dataframe_to_excel(df, file_path, sheet_name='Sheet1', index=False):
    """
    Save a Pandas DataFrame as an Excel file.
    
    Parameters:
        df (pandas.DataFrame): The DataFrame to be saved.
        file_path (str): The path to save the Excel file.
        sheet_name (str, default='Sheet1'): The name of the sheet in the Excel file.
        index (bool, default=False): Whether to include the DataFrame index in the file.
    
    Returns:
        None
    """
    df.to_excel(file_path, sheet_name=sheet_name, index=index)
