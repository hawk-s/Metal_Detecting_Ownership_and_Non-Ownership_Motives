import pandas as pd

def load_excel_to_dataframe(file_path, sheet_name=0, header=0):
    """
    Load an Excel file into a Pandas DataFrame.
    
    Parameters:
        file_path (str): The path to the Excel file.
        sheet_name (str or int, default=0): The name or index of the sheet to load.
        header (int, default=0): The row number to be used as the column names.
    
    Returns:
        pandas.DataFrame: The loaded DataFrame.
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=header)
    return df
